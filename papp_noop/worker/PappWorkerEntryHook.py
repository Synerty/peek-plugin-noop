import logging

from twisted.internet import reactor

from papp_base.worker.PappWorkerEntryHookABC import PappWorkerEntryHookABC
from papp_base.worker.PeekWorkerPlatformABC import PeekWorkerPlatformABC

logger = logging.getLogger(__name__)

class PappWorkerEntryHook(PappWorkerEntryHookABC):
    _instance = None

    def load(self):
        self._instance = self

    @property
    def platform(self):
        assert isinstance(self._platform, PeekWorkerPlatformABC)
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
