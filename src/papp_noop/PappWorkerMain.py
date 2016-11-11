import logging

from twisted.internet import reactor

from papp_base.PappWorkerMainBase import PappWorkerMainBase

logger = logging.getLogger(__name__)


class PappWorkerMain(PappWorkerMainBase):
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

        if self._startLaterCall:
            self._startLaterCall.cancel()
        logger.info("stopped")

    def unload(self):
        logger.info("unloaded")


@property
def pappWorkerMain():
    return PappWorkerMain._instance
