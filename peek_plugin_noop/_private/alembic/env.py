from peek_plugin_base.storage.AlembicEnvBase import AlembicEnvBase

from peek_plugin_noop._private.storage import DeclarativeBase

alembicEnv = AlembicEnvBase(DeclarativeBase.metadata)
alembicEnv.run()
