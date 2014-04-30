import oscad.views
from oslic_export import update_oslic_data

def includeme(config):
    update_oslic_data()

    if oscad.views.DEFAULT_LICENSE == 'GPLv2.0':
        oscad.views.DEFAULT_LICENSE = 'GPL-2.0'

    config.add_route('internal_use_form', 'internal_use')
    config.add_route('internal_use_result', 'internal_use_result')
    config.scan()

    
