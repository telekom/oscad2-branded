from pyramid.view import view_config
from pyramid.httpexceptions import HTTPSeeOther, HTTPNotFound
from pyramid.response import Response

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

