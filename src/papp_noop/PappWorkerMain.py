from __future__ import absolute_import

import logging

from twisted.internet import reactor

from papp_base.PappWorkerMainBase import PappWorkerMainBase
from papp_base.PeekWorkerApiBase import PeekWorkerApiBase
from rapui.DeferUtil import printFailure

logger = logging.getLogger(__name__)


def callWorkerLoop():
    logger.info("Ticking along")

    from papp_noop.worker.NoopWorkerTask import task1
    d = task1.delay("Some task")

    def cb(result):
        logger.info("Worker returned, result %s", result)
        reactor.callLater(5, callWorkerLoop)

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
            callWorkerLoop()

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


@property
def pappWorkerMain():
    return PappWorkerMain._instance
