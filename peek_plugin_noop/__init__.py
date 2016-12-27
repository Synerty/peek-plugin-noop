from typing import Type

from peek_plugin_base.agent.PluginAgentEntryHookABC import PluginAgentEntryHookABC
from peek_plugin_base.client.PluginClientEntryHookABC import PluginClientEntryHookABC
from peek_plugin_base.server.PluginServerEntryHookABC import PluginServerEntryHookABC
from peek_plugin_base.worker.PluginWorkerEntryHookABC import PluginWorkerEntryHookABC
from peek_plugin_noop.agent.PluginAgentEntryHook import PluginAgentEntryHook
from peek_plugin_noop.client.PluginClientEntryHook import PluginClientEntryHook
from peek_plugin_noop.server.PluginServerEntryHook import PluginServerEntryHook
from peek_plugin_noop.worker.PluginWorkerEntryHook import PluginWorkerEntryHook

__version__ = '0.0.18'


def peekServerEntryHook() -> Type[PluginServerEntryHookABC]:
    return PluginServerEntryHook


def peekClientEntryHook() -> Type[PluginClientEntryHookABC]:
    return PluginClientEntryHook


def peekWorkerEntryHook() -> Type[PluginWorkerEntryHookABC]:
    return PluginWorkerEntryHook


def peekAgentEntryHook() -> Type[PluginAgentEntryHookABC]:
    return PluginAgentEntryHook
