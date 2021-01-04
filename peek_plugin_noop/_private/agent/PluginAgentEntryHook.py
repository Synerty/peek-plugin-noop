import logging

from peek_plugin_base.agent.PluginAgentEntryHookABC import PluginAgentEntryHookABC
from twisted.internet import reactor

logger = logging.getLogger(__name__)


class PluginAgentEntryHook(PluginAgentEntryHookABC):
    def load(self):
        logger.debug("loaded")

    def start(self):
        def started():
            self._startLaterCall = None
            logger.debug("started")

        self._startLaterCall = reactor.callLater(3.0, started)
        # logger.debug("starting")

    def stop(self):
        if self._startLaterCall:
            self._startLaterCall.cancel()
        logger.debug("stopped")

    def unload(self):
        logger.debug("unloaded")
