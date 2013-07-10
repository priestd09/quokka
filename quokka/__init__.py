#!/usr/bin/env python
# -*- coding: utf-8 -*-

VERSION = (0, 1, 0)

__version__ = ".".join(map(str, VERSION))
__status__ = "Development"
__description__ = u"Flexible & modular CMS powered by Flask and MongoDB"
__author__ = u"Bruno Rocha"
__credits__ = []
__email__ = u"quokka-developers@googlegroups.com"
__license__ = u"MIT License"
__copyright__ = u"Copyright 2013, Quokka Project"

from flask import Flask
from utils.blueprints import load_blueprints_from_packages
from utils.blueprints import load_blueprints_from_folder

app = Flask(__name__)
app.config.from_object('settings')

load_blueprints_from_packages(app)
load_blueprints_from_folder(app)

if __name__ == "__main__":
    app.run()
