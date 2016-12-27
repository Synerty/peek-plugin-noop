import logging

from twisted.internet import reactor

from peek_plugin_base.server.PluginServerEntryHookABC import PluginServerEntryHookABC
from peek_plugin_base.server.PluginServerStorageEntryHookMixin import \
    PluginServerStorageEntryHookMixin
from peek_plugin_base.server.PluginServerWorkerEntryHookMixin import \
    PluginServerWorkerEntryHookMixin

logger = logging.getLogger(__name__)


class PluginServerEntryHook(PluginServerEntryHookABC,
                            PluginServerStorageEntryHookMixin,
                            PluginServerWorkerEntryHookMixin):
    _instance = None

    @property
    def platform(self):
        return self._platform

    def load(self) -> None:
        # Force migration

        self._startLaterCall = None

    def start(self):

        def started():
            self._startLaterCall = None
            logger.info("started")

            from peek_plugin_noop.server import NoopCeleryTaskMaster
            NoopCeleryTaskMaster.start()

        self._startLaterCall = reactor.callLater(3.0, started)
        logger.info("starting")

    def stop(self):
        from peek_plugin_noop.storage import DeclarativeBase
        DeclarativeBase.__unused = "Testing imports, after sys.path.pop() in register"

        if self._startLaterCall:
            self._startLaterCall.cancel()
        logger.info("stopped")

    def unload(self):
        logger.info("unloaded")

    ###### Implement PluginServerStorageEntryHookMixin

    @property
    def dbMetadata(self):
        from peek_plugin_noop.storage import DeclarativeBase
        return DeclarativeBase.metadata

    ###### Implement PluginServerWorkerEntryHookMixin

    @property
    def celeryApp(self):
        from peek_plugin_noop.worker.NoopCeleryApp import celeryApp
        return celeryApp


def pluginServerMain():
    return PluginServerEntryHook._instance
