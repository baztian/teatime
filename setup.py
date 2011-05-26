# Copyright 2010 Bastian Bowe
#
# This file is part of TeaTime.
# TeaTime is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# TeaTime is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with TeaTime.  If not, see <http://www.gnu.org/licenses/>.
# 

import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
try:
    import py2exe
except ImportError:
    pass

print find_packages('src')
setup(
    #basic package data
    name = 'TeaTime',
    version = '0.1',
    author = 'Bastian Bowe',
    author_email = 'bastian.bowe@gmail.com',
    license = 'GNU GPL',
    url='https://launchpad.net/teatime',
    description=('A tea timer for your task bar.'),
    long_description=file('README.rst').read(),
    keywords = ('tea time timer wxpython wx'),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Library or General Public License (GPL)',
        'Programming Language :: Python',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Utilities',
        'Topic :: Home Automation',
        ],

    packages=find_packages('src'),
    package_dir={ '': 'src' },
    entry_points = {
    'console_scripts': [
    'teatime = teatime:main'
    ]
    },
    data_files=[('',['src/teatime.ico',])],
    # install_requires = [
    # 'wxPython',
    # ],
    # py2exe parameters
    windows=[{'script': 'src/teatime.py',
              'icon_resources': [(0, 'src/teatime.ico')]
              }],
    )
