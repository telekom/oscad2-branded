# coding=utf-8
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

from setuptools import setup

setup(name='t-oscad',
      version='2.0.1-telekom',
      description='oscad 2 - telekom branded',
      url='https://github.com/dtag-dbu/oscad2-branding',
      packages=[
          'oslic_export',
          'oscad_theme_telekom',
      ],
      package_data={
          '': [
              'static/bootstrap/js/*.js',
              'static/bootstrap/fonts/*.eot',
              'static/bootstrap/fonts/*.svg',
              'static/bootstrap/fonts/*.ttf',
              'static/bootstrap/fonts/*.woff',
              'static/jquery/*.js',
              'static/img/*.png',
              'static/img/*.svg',
              'static/agpl-3.0.txt',
              'assets/scss/*.scss',
              'assets/scss/bootstrap/*.scss',
              'templates/*.jinja2',
              'templates/*/*.jinja2',
              'locale/*.pot',
              'locale/*/LC_MESSAGES/*.po',
              'locale/*/LC_MESSAGES/*.mo',
          ],
          'oslic_export': [
              'data/*.yml',
          ],
      }
  )
