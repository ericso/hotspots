import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = [
  'pyramid',
  'WebError',
  'pymongo',
  'pyramid_jinja2'
]

setup(name='hotspots',
      version='0.0',
      description='hotspots',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author="Eric So",
      author_email='me@eric.so',
      url='https://github.com/ericso/hotspots',
      keywords='web pyramid pylons mongodb jinja2',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="hotspots",
      entry_points = """\
      [paste.app_factory]
      main = hotspots:main
      """,
      paster_plugins=['pyramid'],
      )

