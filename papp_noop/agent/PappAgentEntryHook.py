import logging

from twisted.internet import reactor

from papp_base.agent.PappAgentEntryHookABC import PappAgentEntryHookABC
from papp_base.agent.PeekAgentPlatformABC import PeekAgentPlatformABC

logger = logging.getLogger(__name__)


class PappAgentEntryHook(PappAgentEntryHookABC):

    @property
    def platform(self) -> PeekAgentPlatformABC:
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
