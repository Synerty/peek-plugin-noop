from __future__ import absolute_import

import logging

from twisted.internet import reactor

from papp_base.PappWorkerMainBase import PappWorkerMainBase
from papp_base.PeekWorkerApiBase import PeekWorkerApiBase

logger = logging.getLogger(__name__)

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
