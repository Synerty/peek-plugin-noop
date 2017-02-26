import logging

from peek_plugin_base.server.PluginServerEntryHookABC import PluginServerEntryHookABC
from peek_plugin_base.server.PluginServerStorageEntryHookABC import \
    PluginServerStorageEntryHookABC
from peek_plugin_base.server.PluginServerWorkerEntryHookABC import \
    PluginServerWorkerEntryHookABC
from twisted.internet import reactor

logger = logging.getLogger(__name__)


class PluginServerEntryHook(PluginServerEntryHookABC,
                            PluginServerStorageEntryHookABC,
                            PluginServerWorkerEntryHookABC):


    def load(self) -> None:
        # Force migration

        self._startLaterCall = None

    def start(self):

        def started():
            self._startLaterCall = None
            logger.debug("started")

            from peek_plugin_noop._private.server import NoopCeleryTaskMaster
            NoopCeleryTaskMaster.start()

        self._startLaterCall = reactor.callLater(3.0, started)
        logger.debug("starting")

    def stop(self):
        from peek_plugin_noop._private.storage import DeclarativeBase
        DeclarativeBase.__unused = "Testing imports, after sys.path.pop() in register"

        if self._startLaterCall:
            self._startLaterCall.cancel()
        logger.debug("stopped")

    def unload(self):
        logger.debug("unloaded")

    ###### Implement PluginServerStorageEntryHookABC

    @property
    def dbMetadata(self):
        from peek_plugin_noop._private.storage import DeclarativeBase
        return DeclarativeBase.metadata

    ###### Implement PluginServerWorkerEntryHookABC

    @property
    def celeryApp(self):
        from peek_plugin_noop._private.worker.NoopCeleryApp import celeryApp
        return celeryApp
