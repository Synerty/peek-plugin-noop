""" 
 * subcontent.__init__.py
 *
 *  Copyright Synerty Pty Ltd 2013
 *
 *  This software is proprietary, you are not free to copy
 *  or redistribute this code in any format.
 *
 *  All rights to this software are reserved by 
 *  Synerty Pty Ltd
 *
"""

import os.path as p
from rapui import addClientSideResourceDir
from rapui.Util import filterModules

__modPath = p.dirname(__file__)
addClientSideResourceDir(__modPath, autoloadjs=False)

for mod in filterModules(__file__):
    __import__(mod, locals(), globals())