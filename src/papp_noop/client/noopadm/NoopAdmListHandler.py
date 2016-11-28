'''
Created on 09/07/2014

@author: synerty
'''

from peek.core.orm import getNovaOrmSession

from papp_noop.storage.NoopTable import NoopTable
from txhttputil import OrmCrudHandler

__datKey = {
    'papp': 'papp_noop',
    'key': 'noopadm.list.data'}


class CoordSetListHandler(OrmCrudHandler):
    pass


coordSetListHandler = CoordSetListHandler(getNovaOrmSession(),
                                          NoopTable,
                                          __datKey,
                                          retreiveAll=True)
