import logging

from twisted.internet import reactor

from peek_plugin_base.worker.PluginWorkerEntryHookABC import PluginWorkerEntryHookABC
from peek_plugin_base.worker.PeekWorkerPlatformHookABC import PeekWorkerPlatformHookABC

logger = logging.getLogger(__name__)

class PluginWorkerEntryHook(PluginWorkerEntryHookABC):

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
        return ["peek_plugin_noop.worker.NoopWorkerTask"]

    @property
    def celeryApp(self):
        from peek_plugin_noop.worker.NoopCeleryApp import celeryApp
        return celeryApp
