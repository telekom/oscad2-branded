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

import oscad_data as data

@view_config(route_name='internal_use_form', 
             renderer='templates/oscad/internal_use.jinja2',
             request_method='GET')
def internal_use_form(request):
    return {
        'licenses': data.valid_licenses
    }

@view_config(route_name='internal_use_result', 
             renderer='templates/oscad/internal_use_result.jinja2',
             request_method='GET')
def internal_use_result(request):
    internal_use = request.params['2others'] == 'false'
    unmodified = request.params['modified'] == 'false'
    known_licenses = request.params['oslic'] == 'true'
    can_simplify = internal_use and unmodified and known_licenses
    return {
        'can_simplify': can_simplify
    }


def register_views(config):
    config.add_route('internal_use_form', 'internal_use')
    config.add_route('internal_use_result', 'internal_use_result')
    config.scan()

