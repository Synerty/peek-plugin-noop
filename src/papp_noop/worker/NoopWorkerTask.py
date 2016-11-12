from celery.utils.log import get_task_logger
from datetime import datetime
from time import sleep
from txcelery.defer import CeleryClient

from papp_noop.worker.NoopCeleryApp import celeryApp

logger = get_task_logger(__name__)


@CeleryClient
@celeryApp.task
def task1(inStr):
    logger.info("Received %s", inStr)
    sleep(2)
    return "it's been precseed %s " % datetime.utcnow()
