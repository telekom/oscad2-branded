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
import oscad.views
import oslic_export

import oscad_theme_telekom.t_views
import oscad_theme_telekom.t_events

def includeme(config):
    # Workaround to fix the hard-coded name of the default license
    # This should really be fixed in oscad.views in std-oscad 
    if oscad.views.DEFAULT_LICENSE == 'GPLv2.0':
        oscad.views.DEFAULT_LICENSE = 'GPL-2.0'

    # Replace the in-memory content of the std-oscad YAML files
    # with our Oslic export 
    oslic_export.update_oslic_data()

    # Call the registration methods of the other packages
    oscad_theme_telekom.t_events.register_events(config)
    oscad_theme_telekom.t_views.register_views(config)
