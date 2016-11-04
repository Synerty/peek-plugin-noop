import os
from twisted.internet import reactor

from papp_base.PappMainBase import PappMainBase
from papp_base.storage import DbConn


class PappMain(PappMainBase):
    _instance = None

    def _initSelf(self):
        self._instance = self

    @property
    def platform(self):
        return self._platform

    def start(self):

        # Configure database
        p = os.path
        alembicDir = p.join(p.dirname(p.dirname(__file__)), "alembic")

        from papp_noop.storage import DeclarativeBase
        DbConn.setup(
            dbConnectString=self.platform.dbConnectString,
            metadata=DeclarativeBase.metadata,
            alembicDir=alembicDir
        )

        # Force migration
        DbConn.getPappOrmSession()
        def started():
            self._startLaterCall = None
            print "PappClient started"

        self._startLaterCall = reactor.callLater(3.0, started)

    def stop(self):
        from papp_noop.storage import DeclarativeBase
        DeclarativeBase.__unused="Testing imports, after sys.path.pop() in register"
        if self._startLaterCall:
            self._startLaterCall.cancel()
        print "PappClient stop"

    def configUrl(self):
        return 'peek_noop'


@property
def pappMain():
    return PappMain._instance
