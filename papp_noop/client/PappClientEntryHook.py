import logging

from twisted.internet import reactor

from papp_base.client.PappClientEntryHookABC import PappClientEntryHookABC
from papp_base.client.PeekClientPlatformABC import PeekClientPlatformABC

logger = logging.getLogger(__name__)


class PappClientEntryHook(PappClientEntryHookABC):

    @property
    def platform(self) -> PeekClientPlatformABC:
        return self._platform

    def load(self):
        logger.debug("loaded")

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

