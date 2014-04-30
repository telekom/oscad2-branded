# coding=utf-8

from setuptools import setup

setup(name='t-oscad',
      version='2.0.1-telekom',
      description='oscad 2 - telekom branded',
      author='Ronald Dauster, GIDO GmbH',
      author_email='rpd@gido.de',
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
      },
      entry_points={
          'babel.extractors': [
              'oscad_lsuc       = oslic_export.extractors:extract_lsuc',
              'oscad_osuc       = oslic_export.extractors:extract_osuc',
              'oscad_parameters = oslic_export.extractors:extract_parameters',
          ],
      },
      message_extractors={
          'oscad_theme_telekom': [
              ('**.py', 'python', None),
              ('**.jinja2', 'jinja2', None),
              ('static/**', 'ignore', None),
          ],
      },
  )
