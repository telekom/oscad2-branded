# ------------------------------------------------------------------------------
#    OSCAd - the Open Source Compliance Advisor
#    Copyright (C) 2014 Deutsche Telekom AG
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPSeeOther

from oscad.views import extract_params, results_for_osuc_and_license
from oscad.models import OSUC

import oscad_data as data

@view_config(route_name='advice', 
             renderer='templates/oscad/advice.jinja2',
             request_method='GET')
def result(request):
    license = request.matchdict['license']
    osuc = OSUC.from_number(request.matchdict['osuc'])
    return results_for_osuc_and_license(request, osuc, license)


@view_config(route_name='result', request_method='POST')
def process_form_submission(request):

    license, = extract_params(request, ['license'])

    if 'osuc' in request.params:
        osuc_number, = extract_params(request, ['osuc'])
        osuc = OSUC.from_number(osuc_number)

    else:
        recipient, type_, state, form, context = extract_params(
            request,
            ['recipient', 'type', 'state', 'form', 'context']
        )

        osuc = OSUC.from_attrs(recipient=recipient, type=type_, state=state,
                               form=form, context=context)

    target = request.route_path('advice', osuc=osuc.number, license=license)
    return HTTPSeeOther(location = target)


@view_config(route_name     = 'internal_use_form', 
             renderer       = 'templates/oscad/internal_use.jinja2',
             request_method = 'GET')
def internal_use_form(request):
    return {
        'licenses': data.valid_licenses
    }


@view_config(route_name     = 'internal_use_result', 
             renderer       = 'templates/oscad/internal_use_result.jinja2',
             request_method = 'GET')
def internal_use_result(request):
    internal_use = request.params['2others'] == 'false'
    unmodified = request.params['modified'] == 'false'
    known_licenses = request.params['oslic'] == 'true'
    can_simplify = internal_use and unmodified and known_licenses
    return {
        'can_simplify': can_simplify
    }

@view_config(route_name     = 'javascript_licenses',
             renderer       = 'templates/oscad/javascript_licenses.jinja2',
             request_method = 'GET')
def javascript_licenses(request):
    jquery = {
        'file_name'   : 'jquery-2.0.3.min.js',
        'file_url'    : request.static_url('oscad:jquery/jquery-2.0.3.min.js'),
        'license_name': 'MIT',
        'license_url' : request.static_url('oscad:static/jquery/MIT-LICENSE.txt'),
        'source_name' : 'jquery-2.0.3.js',
        'source_url'  : request.static_url('oscad:static/jquery/jquery-2.0.3.js')
    }
    bootstrap = {
        'file_name'   : 'bootstrap.min.js',
        'file_url'    : request.static_url('oscad:bootstrap/js/bootstrap.min.js'),
        'license_name': 'Apache-2.0',
        'license_url' : 'http://www.apache.org/licenses/LICENSE-2.0',
        'source_name' : 'bootstrap.js',
        'source_url'  : request.static_url('oscad:bootstrap/js/bootstrap.js')
    }
    return { 
        'javascript_libraries': [ jquery, bootstrap ]
    }

def register_views(config):
    config.add_route('internal_use_form', 'internal_use')
    config.add_route('internal_use_result', 'internal_use_result')
    config.add_route('javascript_licenses', 'javascript_licenses')
    config.add_route('advice', 'advice/{license}/{osuc}')
    config.scan()

