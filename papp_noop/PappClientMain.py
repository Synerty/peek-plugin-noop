import logging

from twisted.internet import reactor

from papp_base.client.PappClientEntryHookABC import PappClientEntryHookABC

logger = logging.getLogger(__name__)


class PappClientMain(PappClientEntryHookABC):
    _instance = None

    def _initSelf(self):
        self._instance = self

    def load_(self) -> None:
        self._startLaterCall = None

    @property
    def platform(self):
        return self._platform

    def start(self):
        # Force migration
        from papp_noop.storage import DeclarativeBase
        self._initialiseDb(DeclarativeBase.metadata, __file__)
        self._setupDirs(__file__)

        def started():
            self._startLaterCall = None
            logger.info("started")

            from papp_noop.server import NoopCeleryTaskMaster
            NoopCeleryTaskMaster.start()

        self._startLaterCall = reactor.callLater(3.0, started)
        logger.info("starting")

    def stop(self):
        from papp_noop.storage import DeclarativeBase
        DeclarativeBase.__unused = "Testing imports, after sys.path.pop() in register"

        if self._startLaterCall:
            self._startLaterCall.cancel()
        logger.info("stopped")

    def unload(self):
        logger.info("unloaded")

    @property
    def dbOrmSession(self):
        return self._dbConn.getPappOrmSession()

    @property
    def dbEngine(self):
        return self._dbConn._dbEngine

    @property
    def celeryApp(self):
        from papp_noop.worker.NoopCeleryApp import celeryApp
        return celeryApp


def pappServerMain():
    return PappServerMain._instance
