import logging
from datetime import datetime

from twisted.internet import reactor

from vortex.SerialiseUtil import fromStr, T_DATETIME
from txhttputil.util.DeferUtil import printFailure

logger = logging.getLogger(__name__)


REPEAT = 0.5


def callWorkerSleepLoop():
    # logger.info("Sleep Only Task - Ticking along")

    from papp_noop.worker.NoopWorkerTask import task1
    startTime = datetime.utcnow()

    d = task1.delay("Some task arg str")

    def cb(resultStr):
        resultDate = fromStr(resultStr, T_DATETIME)
        logger.info("Sleep Only Task started %s, returned %s",
                    resultDate - startTime,
                    datetime.utcnow() - startTime)

        reactor.callLater(REPEAT, callWorkerSleepLoop)

    d.addCallback(cb)
    d.addErrback(printFailure)
    return d


def callWorkerDbLoop():
    # logger.info("DB Update Task - Ticking along")

    from papp_noop.worker.NoopWorkerTask import dbTask
    startTime = datetime.utcnow()
    d = dbTask.delay("db update task str arg")

    def cb(newId):
        logger.info("DB Update Task newId %s, returned %s",
                    newId,
                    datetime.utcnow() - startTime)
        reactor.callLater(REPEAT, callWorkerDbLoop)

    d.addCallback(cb)
    d.addErrback(printFailure)
    return d



def start():
    pass
    # for _ in range(4):
    #     callWorkerSleepLoop()
    #
    # for _ in range(2):
    #     callWorkerDbLoop()