from datetime import datetime
from time import sleep

import pytz
from celery.utils.log import get_task_logger
from peek_plugin_base.worker import CeleryDbConn
from peek_plugin_noop._private.storage.NoopTable import NoopTable
from sqlalchemy.sql.functions import func
from txcelery.defer import CeleryClient
from vortex.SerialiseUtil import toStr

from peek_plugin_base.worker.CeleryApp import celeryApp

logger = get_task_logger(__name__)


def add1(val):
    return val + 1


@CeleryClient
@celeryApp.task
def task1(inStr):
    logger.info("Received %s", inStr)
    sleep(1.0)
    return toStr(datetime.now(pytz.utc))


@CeleryClient
@celeryApp.task
def dbTask(string1):
    logger.info("Running")
    session = CeleryDbConn.getDbSession()
    session.add(NoopTable(string1=string1))
    session.commit()

    id = session.query(func.max(NoopTable.id))[0]

    return id
