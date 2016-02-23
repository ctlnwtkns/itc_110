try:
	from setuptools import setup:
except ImportError:
	from distutils.core import setup
	
config = {
	'description':'Group Project',
	'author':'caitlin',
	'url':'http://edison.seattlecentral.edu/~cwatki06',
	'download_url':'https://github.com/ctlnwtkns/itc_110/tree/master/lpthw',
	'author_email':'ctlnwtkns@gmail.com',
	'version':'0.1',
	'install_requires':'[nose]',
	'packages':'[NAME]',
	'scripts':'[]',
	'name':'itc_110'
}

set(**config)