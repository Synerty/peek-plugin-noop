import logging

from peek_plugin_base.worker.PluginWorkerEntryHookABC import PluginWorkerEntryHookABC
from peek_plugin_noop._private.worker import NoopWorkerTask
from twisted.internet import reactor

logger = logging.getLogger(__name__)

class PluginWorkerEntryHook(PluginWorkerEntryHookABC):

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
        return [NoopWorkerTask.__name__]

    @property
    def celeryApp(self):
        from peek_plugin_noop._private.worker.NoopCeleryApp import celeryApp
        return celeryApp
