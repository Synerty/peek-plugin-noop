import logging

from twisted.internet import reactor

from papp_base.PappAgentMainBase import PappAgentMainBase

logger = logging.getLogger(__name__)


class PappAgentMain(PappAgentMainBase):
    _instance = None

    def _initSelf(self):
        self._instance = self

    @property
    def platform(self):
        return self._platform

    def start(self):
        # Force migration
        def started():
            self._startLaterCall = None
            logger.info("started")

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
def pappAgentMain():
    return PappAgentMain._instance
