#!/usr/bin/env python
# -*- coding: utf-8 -*-

activate_this = '/opt/inventario/CheckUpdate3/bin/activate_this.py'

execfile(activate_this, dict(__file__=activate_this))

import sys

sys.path.insert(0, "/opt/inventario/CheckUpdate3")

from app import app as application


