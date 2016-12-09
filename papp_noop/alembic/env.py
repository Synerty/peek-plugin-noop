from papp_base.storage.AlembicEnvBase import AlembicEnvBase

from papp_noop.storage import DeclarativeBase

alembicEnv = AlembicEnvBase(DeclarativeBase.metadata)
alembicEnv.run()
