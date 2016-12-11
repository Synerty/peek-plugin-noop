from typing import Type

from papp_base.agent.PappAgentEntryHookABC import PappAgentEntryHookABC
from papp_base.client.PappClientEntryHookABC import PappClientEntryHookABC
from papp_base.server.PappServerEntryHookABC import PappServerEntryHookABC
from papp_base.worker.PappWorkerEntryHookABC import PappWorkerEntryHookABC
from papp_noop.agent.PappAgentEntryHook import PappAgentEntryHook
from papp_noop.client.PappClientEntryHook import PappClientEntryHook
from papp_noop.server.PappServerEntryHook import PappServerEntryHook
from papp_noop.worker.PappWorkerEntryHook import PappWorkerEntryHook

__version__ = '0.0.9'


def peekServerEntryHook() -> Type[PappServerEntryHookABC]:
    return PappServerEntryHook


def peekClientEntryHook() -> Type[PappClientEntryHookABC]:
    return PappClientEntryHook


def peekWorkerEntryHook() -> Type[PappWorkerEntryHookABC]:
    return PappWorkerEntryHook


def peekAgentEntryHook() -> Type[PappAgentEntryHookABC]:
    return PappAgentEntryHook
