import logging
from datetime import datetime

import pytz
from twisted.internet.defer import DeferredList, inlineCallbacks
from vortex.DeferUtil import vortexLogFailure
from vortex.SerialiseUtil import fromStr, T_DATETIME

logger = logging.getLogger(__name__)


class MainController:
    REPEAT = 0.5

    def __init__(self):
        self._running = False

    def start(self):
        self._running = True
        self._startWorkerSleepLoop()
        self._startWorkerDbLoop()

    def shutdown(self):
        self._running = False

    def _startWorkerSleepLoop(self):
        d = DeferredList(
            [self._workerSleepLoopStrand(n) for n in range(50)], fireOnOneErrback=True
        )
        d.addErrback(vortexLogFailure, logger, consumeError=True)

    @inlineCallbacks
    def _workerSleepLoopStrand(self, strandNum):
        # logger.info("Sleep Only Task - Ticking along")

        from peek_plugin_noop._private.worker.NoopWorkerTask import task1

        startTime = datetime.now(pytz.utc)
        while self._running:
            resultStr = yield task1.delay("Some task arg str")

            resultDate = fromStr(resultStr, T_DATETIME)
            logger.info(
                "Sleep Only Task started %s, returned %s",
                resultDate - startTime,
                datetime.now(pytz.utc) - startTime,
            )

    def _startWorkerDbLoop(self):
        d = DeferredList(
            [self._workerDbLoopStrand(n) for n in range(50)], fireOnOneErrback=True
        )
        d.addErrback(vortexLogFailure, logger, consumerError=True)

    @inlineCallbacks
    def _workerDbLoopStrand(self, strandNum):
        # logger.info("DB Update Task - Ticking along")

        from peek_plugin_noop._private.worker.NoopWorkerTask import dbTask

        startTime = datetime.now(pytz.utc)

        while self._running:
            yield dbTask.delay("db update task str arg")
            logger.info(
                "DB Update Task, returned %s", datetime.now(pytz.utc) - startTime
            )
