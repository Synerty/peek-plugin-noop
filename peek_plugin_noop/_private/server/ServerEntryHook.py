import logging

from peek_plugin_base.server.PluginServerEntryHookABC import PluginServerEntryHookABC
from peek_plugin_base.server.PluginServerStorageEntryHookABC import \
    PluginServerStorageEntryHookABC
from peek_plugin_base.server.PluginServerWorkerEntryHookABC import \
    PluginServerWorkerEntryHookABC
from peek_plugin_noop._private.server.MainController import MainController
from peek_plugin_noop._private.storage import DeclarativeBase
from twisted.internet.defer import inlineCallbacks

logger = logging.getLogger(__name__)


class ServerEntryHook(PluginServerEntryHookABC,
                      PluginServerStorageEntryHookABC,
                      PluginServerWorkerEntryHookABC):

    def load(self) -> None:
        DeclarativeBase.loadStorageTuples()
        logger.debug("Loaded")

        self._mainController = MainController()

    @inlineCallbacks
    def start(self):
        yield self._mainController.start()

        logger.debug("starting")

    def stop(self):
        from peek_plugin_noop._private.storage import DeclarativeBase
        DeclarativeBase.__unused = "Testing imports, after sys.path.pop() in register"

        self._mainController.shutdown()

        self._mainController = None
        logger.debug("stopped")

    def unload(self):
        logger.debug("unloaded")

    ###### Implement PluginServerStorageEntryHookABC

    @property
    def dbMetadata(self):
        return DeclarativeBase.metadata

    ###### Implement PluginServerWorkerEntryHookABC
