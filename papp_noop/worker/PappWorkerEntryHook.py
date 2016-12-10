import logging

from twisted.internet import reactor

from papp_base.worker.PappWorkerEntryHookABC import PappWorkerEntryHookABC
from papp_base.worker.PeekWorkerPlatformHookABC import PeekWorkerPlatformHookABC

logger = logging.getLogger(__name__)

class PappWorkerEntryHook(PappWorkerEntryHookABC):

    @property
    def platform(self) -> PeekWorkerPlatformHookABC:
        return self._platform

    def load(self):
        logger.info("loaded")

    def start(self):
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
