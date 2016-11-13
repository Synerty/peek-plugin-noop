from __future__ import absolute_import

import logging
from datetime import datetime

from twisted.internet import reactor

from papp_base.PappWorkerMainBase import PappWorkerMainBase
from papp_base.PeekWorkerApiBase import PeekWorkerApiBase
from rapui.DeferUtil import printFailure
from rapui.vortex.SerialiseUtil import fromStr, T_DATETIME

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


class PappWorkerMain(PappWorkerMainBase):
    _instance = None

    def _initSelf(self):
        self._instance = self

    @property
    def platform(self):
        assert isinstance(self._platform, PeekWorkerApiBase)
        return self._platform

    def start(self):
        # Force migration
        def started():
            self._startLaterCall = None
            logger.info("started")
            for _ in range(3):
                callWorkerSleepLoop()

            for _ in range(3):
                callWorkerDbLoop()

        self._startLaterCall = reactor.callLater(3.0, started)
        logger.info("starting")

    def stop(self):
        if self._startLaterCall:
            self._startLaterCall.cancel()
        logger.info("stopped")

    def unload(self):
        logger.info("unloaded")

    @property
    def celeryAppIncludes(self):
        return ["papp_noop.worker.NoopWorkerTask"]

    @property
    def celeryApp(self):
        from papp_noop.worker.NoopCeleryApp import celeryApp
        return celeryApp


def getPappWorkerMain():
    return PappWorkerMain._instance
