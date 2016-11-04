from papp_base.storage import AlembicEnv

from papp_noop.storage import DeclarativeBase

AlembicEnv.target_metadata = DeclarativeBase.metadata
AlembicEnv.run_migrations_online()
