try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'name': 'Sun Angle Calculator',
	'version': '0.1',
	'url': 'https://github.com/parnellj/sun_angle_calculator',
	'download_url': 'https://github.com/parnellj/sun_angle_calculator',
	'author': 'Justin Parnell',
	'author_email': 'parnell.justin@gmail.com',
	'maintainer': 'Justin Parnell',
	'maintainer_email': 'parnell.justin@gmail.com',
	'classifiers': [],
	'license': 'GNU GPL v3.0',
	'description': 'Calculates the angle and position of the Sun in the sky at a given epoch.',
	'long_description': 'Calculates the angle and position of the Sun in the sky at a given epoch.',
	'keywords': '',
	'install_requires': ['nose'],
	'packages': ['sun_angle_calculator'],
	'scripts': []
}
	
setup(**config)
