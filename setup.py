#!/usr/bin/env python
# encoding:utf-8
#
# ./setup.py bdist_wheel upload
# ./setup.py bdist_wininst   

import glob, sys, subprocess, os, re, shutil
from setuptools import setup

import download_npo
version = download_npo.GetVersion()[0]

setup(
	name = 'download-npo',
	version = version,
	author = 'Martin Tournoij',
	author_email = 'martin@arp242.net',
	url = 'http://arp242.net/code/download-npo',
	description = 'download videos from the Dutch npo.nl site.',
	long_description = '''
	Download-npo downloads videos from the Dutch npo.nl site. The rest of
the documentation is in Dutch.

Download-npo (voorheen download-gemist) download videos van de NPO site
van de publieke omroep. In principe zouden alle sites die gebruik maken
van de zogeheten “NPOPlayer” zouden moeten werken, zoals bv. ncrv.nl of
nrc.nl (al zijn deze niet allemaal getest).
	''',
	packages = ['download_npo'],
	scripts = ['download-npo', 'download-npo-gui', 'play-npo'],
	license = 'MIT',
	#platforms = [],
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: Dutch',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
	data_files = [
		('share/doc/download-npo', ['README.markdown']),
		('share/download-npo', ['icon.gif', 'icon.svg']),
		('share/applications', ['download-npo-gui.desktop']),
		('/usr/share/icons/hicolor/scalable/apps/', ['download-npo-gui.svg']),
	],
)
