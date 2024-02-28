"""事件处理核心模块"""

import logging
from typing import List, Dict, Callable, Any, DefaultDict, Optional, Union
from collections import defaultdict
from multiprocessing import Event
from vxsched.event import VXEvent, VXEventQueue
from vxsched.handlers import VXHandlers
from vxutils import VXContext


class VXScheduler:
    """事件调度器"""

    def __init__(
        self,
        context: Optional[Union[Dict[str, Any], VXContext]] = None,
        *,
        handlers: Optional[VXHandlers] = None,
    ) -> None:
        self._handlers: VXHandlers = handlers or VXHandlers()
        self._context: VXContext = VXContext(**c1ontext)
        self._queue: VXEventQueue = VXEventQueue()
        self._is_active: bool = False

    @property
    def handlers(self) -> VXHandlers:
        return self._handlers

    @property
    def context(self) -> VXContext:
        return self._context

    @property
    def is_active(self) -> bool:
        return self._is_active

    def start(self) -> None:
        """启动事件调度器"""
        self._is_active = True
