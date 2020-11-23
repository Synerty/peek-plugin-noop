__version__ = '0.0.0'

from peek_plugin_base.agent.PluginAgentEntryHookABC import PluginAgentEntryHookABC
from peek_plugin_base.client.PluginClientEntryHookABC import PluginClientEntryHookABC
from peek_plugin_base.server.PluginLogicEntryHookABC import PluginLogicEntryHookABC
from peek_plugin_base.worker.PluginWorkerEntryHookABC import PluginWorkerEntryHookABC
from typing import Type


def peekLogicEntryHook() -> Type[PluginLogicEntryHookABC]:
    from ._private.server.LogicEntryHook import LogicEntryHook
    return LogicEntryHook


def peekFieldEntryHook() -> Type[PluginClientEntryHookABC]:
    from ._private.client.PluginClientEntryHook import PluginClientEntryHook
    return PluginClientEntryHook


def peekOfficeEntryHook() -> Type[PluginClientEntryHookABC]:
    from ._private.client.PluginClientEntryHook import PluginClientEntryHook
    return PluginClientEntryHook


def peekWorkerEntryHook() -> Type[PluginWorkerEntryHookABC]:
    from ._private.worker.PluginWorkerEntryHook import PluginWorkerEntryHook
    return PluginWorkerEntryHook


def peekAgentEntryHook() -> Type[PluginAgentEntryHookABC]:
    from ._private.agent.PluginAgentEntryHook import PluginAgentEntryHook
    return PluginAgentEntryHook
