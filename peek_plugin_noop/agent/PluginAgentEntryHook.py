import logging

from twisted.internet import reactor

from peek_plugin_base.agent.PluginAgentEntryHookABC import PluginAgentEntryHookABC
from peek_plugin_base.agent.PeekAgentPlatformHookABC import PeekAgentPlatformHookABC

logger = logging.getLogger(__name__)


class PluginAgentEntryHook(PluginAgentEntryHookABC):

    @property
    def platform(self) -> PeekAgentPlatformHookABC:
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
