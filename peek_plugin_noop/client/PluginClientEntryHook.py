import logging

from twisted.internet import reactor

from peek_plugin_base.client.PluginClientEntryHookABC import PluginClientEntryHookABC
from peek_plugin_base.client.PeekClientPlatformHookABC import PeekClientPlatformHookABC

logger = logging.getLogger(__name__)


class PluginClientEntryHook(PluginClientEntryHookABC):

    @property
    def platform(self) -> PeekClientPlatformHookABC:
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

