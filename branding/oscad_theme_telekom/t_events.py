from __future__ import print_function

from pyramid.events import BeforeRender
from pyramid.events import subscriber

# This method needs to run after the add_renderer_globals event handler
# and depends on the menu entries defined by that method.  
#
# Currently this probably works, because this handler is registered after
# add_renderer_globals.  And is is register later, because config.scan is
# called after config.add_subscriber
@subscriber(BeforeRender)
def add_menu_entries(event):
    request = event['request']
    toplevel_links = event['toplevel_links']
    if toplevel_links is not None:
        toplevel_links[0:0] = [(request.route_path('internal_use_form'),
                               request.translate('Common Cases'))]

@subscriber(BeforeRender)
def set_oslic_url(event):
    request = event['request']
    request.oscad_settings.oslic_url = request.static_url('oscad:static/pdf/oslic-0.99.3.pdf')
