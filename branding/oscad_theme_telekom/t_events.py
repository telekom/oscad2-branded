# -*- coding: utf-8 -*-
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

def _isgerman(request):
    return request.locale_name == "de"

def _localize(request, german, english):
    if _isgerman(request):
        return german
    else:
        return english

def _german(g, e):
    return g

def _english(g, e):
    return e

# This method needs to run after the add_renderer_globals event handler
#
# Currently this probably works, because this handler is registered after
# add_renderer_globals.  
def add_menu_entries(event):
    request = event['request']
    
    def entry(route, german, english):
        return (request.route_path(route), _localize(request, german, english))

    toplevel_links = [
        entry('request',           u'Standardanfrage',   u'Standard Request'),
        entry('matrix_request',    u'Taxononie-Anfrage', u'Taxonomy request'),
        entry('internal_use_form', u'Sonderanfrage',     u'Special Request'),
        entry('about',             u'Über OSCAd',        u'About'),
        entry('components',        u'Komponenten',       u'Components'),
        entry('imprint',           u'Impressum',         u'Imprint'),
        entry('help',              u'Hilfe',             u'Help')]
    
    event['toplevel_links'] = toplevel_links
                

def set_oslic_url(event):
    request = event['request']
    request.oscad_settings.oslic_url = request.static_url('oscad:static/pdf/oslic-0.99.3.pdf')
    
def add_translation_method(event):
    request = event['request']

    if _isgerman(request):
        request.select = _german
        request.is_german = True
    else:
        request.select = _english
        request.is_german = False


def register_events(config):
    def before_render(methodname):
        config.add_subscriber(__name__ + '.' + methodname, 
                              'pyramid.events.BeforeRender')

    before_render('add_menu_entries')
    before_render('set_oslic_url')
    before_render('add_translation_method')

