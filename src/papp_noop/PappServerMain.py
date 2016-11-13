import logging

from twisted.internet import reactor

from papp_base.PappServerMainBase import PappServerMainBase
from papp_noop.server import NoopCeleryTaskMaster

logger = logging.getLogger(__name__)

class PappServerMain(PappServerMainBase):
    _instance = None

    def _initSelf(self):
        self._instance = self

    @property
    def platform(self):
        return self._platform

    def start(self):
        from papp_noop.storage import DeclarativeBase
        self._initialiseDb(DeclarativeBase.metadata, __file__)

        # Force migration
        def started():
            self._startLaterCall = None
            logger.info("started")
            NoopCeleryTaskMaster.start()

        self._startLaterCall = reactor.callLater(3.0, started)
        logger.info("starting")

    def stop(self):
        from papp_noop.storage import DeclarativeBase
        DeclarativeBase.__unused="Testing imports, after sys.path.pop() in register"

        if self._startLaterCall:
            self._startLaterCall.cancel()
        logger.info( "stopped")

    def unload(self):
        logger.info("unloaded")

    def configUrl(self):
        return 'peek_noop'

    @property
    def dbOrmSession(self):
        return self._dbConn.getPappOrmSession()

    @property
    def dbEngine(self):
        return self._dbConn._dbEngine


@property
def pappServerMain():
    return PappServerMain._instance
