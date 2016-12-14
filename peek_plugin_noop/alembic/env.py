from peek_plugin_base.storage.AlembicEnvBase import AlembicEnvBase

from peek_plugin_noop.storage import DeclarativeBase

alembicEnv = AlembicEnvBase(DeclarativeBase.metadata)
alembicEnv.run()
