__version__ = '0.7.6'

from peek_plugin_base.agent.PluginAgentEntryHookABC import PluginAgentEntryHookABC
from peek_plugin_base.client.PluginClientEntryHookABC import PluginClientEntryHookABC
from peek_plugin_base.server.PluginServerEntryHookABC import PluginServerEntryHookABC
from peek_plugin_base.worker.PluginWorkerEntryHookABC import PluginWorkerEntryHookABC
from typing import Type


def peekServerEntryHook() -> Type[PluginServerEntryHookABC]:
    from ._private.server.ServerEntryHook import ServerEntryHook
    return ServerEntryHook


def peekClientEntryHook() -> Type[PluginClientEntryHookABC]:
    from ._private.client.PluginClientEntryHook import PluginClientEntryHook
    return PluginClientEntryHook


def peekWorkerEntryHook() -> Type[PluginWorkerEntryHookABC]:
    from ._private.worker.PluginWorkerEntryHook import PluginWorkerEntryHook
    return PluginWorkerEntryHook


def peekAgentEntryHook() -> Type[PluginAgentEntryHookABC]:
    from ._private.agent.PluginAgentEntryHook import PluginAgentEntryHook
    return PluginAgentEntryHook
