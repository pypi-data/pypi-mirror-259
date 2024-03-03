import asyncio as aio
import inspect
import traceback
from asyncio import iscoroutine, iscoroutinefunction
from pathlib import Path

from ..types.core import IActionResponder
from ..types.exceptions import *
from ..types.models import (
    HandlerArgs,
    HookRunnerArgs,
    IEventHandler,
    ShareCbArgs,
    ShareObjArgs,
    SignalHandlerArgs,
)
from ..types.typing import *
from ..types.utils import BotChecker, BotMatcher, BotParser, Logger, WrappedLogger
from ..utils.checker import AtChecker
from .action import msg_action
from .bot import BotHookBus, HookRunner, PluginProxy
from .event import MsgEvent
from .ipc import PluginBus, PluginSignalHandler, PluginStore
from .session import SESSION_LOCAL, BotSession, BotSessionManager, SessionRule


class Plugin:
    """
    bot 插件基类。所有自定义插件必须继承该类实现。
    """

    # 标记了该类有哪些实例属性需要被共享。每个元素是一个共享对象构造参数元组
    __share__: List[ShareObjArgs] = []
    # 插件 id 和 version 标记
    __id__: str = None
    __version__: str = "1.0.0"
    # 插件类所在的文件路径，PosicPath 对象
    ROOT: Path
    # 被二次包装的全局日志器
    LOGGER: WrappedLogger

    def __init__(self) -> None:
        self.__handlers: List[IEventHandler]
        self.__proxy: PluginProxy

    def __build(
        self, root_path: Path, logger: Logger, responder: IActionResponder
    ) -> None:
        """
        初始化当前插件
        """
        if self.__class__.__id__ is None:
            self.__class__.__id__ = self.__class__.__name__
        for idx, val in enumerate(self.__class__.__share__):
            if isinstance(val, str):
                self.__class__.__share__[idx] = val, self.__class__.__name__, val
        self.__handlers = []

        self.__class__.ROOT = root_path
        self.__class__.LOGGER = WrappedLogger(logger, self.__class__.__id__)

        attrs_map = {
            k: v for k, v in inspect.getmembers(self) if not k.startswith("__")
        }
        for val in self.__class__.__share__:
            property, namespace, id = val
            if property not in attrs_map.keys() and property is not None:
                raise BotRuntimeError(
                    f"插件 {self.__class__.__name__} 尝试共享一个不存在的属性 {property}"
                )
            PluginStore._create_so(property, namespace, id, self)

        members = inspect.getmembers(self)
        for attr_name, val in members:
            if isinstance(val, HandlerArgs):
                executor, handler_class, params = val
                if not iscoroutinefunction(executor):
                    raise BotTypeError(f"事件处理器 {executor.__name__} 必须为异步方法")
                overtime_cb_maker, conflict_cb_maker = params[-1], params[-2]
                if overtime_cb_maker and not callable(overtime_cb_maker):
                    raise BotTypeError(
                        f"超时回调方法 {overtime_cb_maker.__name__} 必须为可调用对象"
                    )
                if conflict_cb_maker and not callable(conflict_cb_maker):
                    raise BotTypeError(
                        f"冲突回调方法 {conflict_cb_maker.__name__} 必须为可调用对象"
                    )
                handler = handler_class(executor, self, responder, logger, *params)
                self.__handlers.append(handler)
                BotSessionManager.register(handler)

            elif isinstance(val, HookRunnerArgs):
                hook_func, type = val
                if not iscoroutinefunction(hook_func):
                    raise BotTypeError(f"hook 方法 {hook_func.__name__} 必须为异步函数")
                runner = HookRunner(type, hook_func, self)
                BotHookBus._register(type, runner)

            elif isinstance(val, ShareCbArgs):
                namespace, id, cb = val
                if not iscoroutinefunction(cb):
                    raise BotTypeError(
                        f"{namespace} 命名空间中，id 为 {id} 的共享对象，它的回调 {cb.__name__} 必须为异步函数"
                    )
                PluginStore._bind_cb(namespace, id, cb, self)

            elif isinstance(val, SignalHandlerArgs):
                func, namespace, signal = val
                if not iscoroutinefunction(func):
                    raise BotTypeError(f"信号处理方法 {func.__name__} 必须为异步函数")
                handler = PluginSignalHandler(namespace, signal, func, self)
                PluginBus._register(namespace, signal, handler)

        self.__proxy = PluginProxy(self)

    @classmethod
    def on_msg(
        cls,
        matcher: BotMatcher = None,
        parser: BotParser = None,
        checker: BotChecker = None,
        priority: PriorityLevel = PriorityLevel.MEAN,
        timeout: int = None,
        block: bool = False,
        temp: bool = False,
        session_rule: SessionRule = None,
        session_hold: bool = False,
        direct_rouse: bool = False,
        conflict_wait: bool = False,
        conflict_cb: Callable[[None], Coroutine] = None,
        overtime_cb: Callable[[None], Coroutine] = None,
    ) -> Callable:
        """
        使用该装饰器，将方法标记为消息事件执行器
        """

        def make_args(executor: AsyncFunc[None]) -> HandlerArgs:
            return HandlerArgs(
                executor=executor,
                type=MsgEventHandler,
                params=[
                    matcher,
                    parser,
                    checker,
                    priority,
                    timeout,
                    block,
                    temp,
                    session_rule,
                    session_hold,
                    direct_rouse,
                    conflict_wait,
                    conflict_cb,
                    overtime_cb,
                ],
            )

        return make_args

    @classmethod
    def on_any_msg(
        cls,
        checker: BotChecker = None,
        priority: PriorityLevel = PriorityLevel.MEAN,
        timeout: int = None,
        block: bool = False,
        temp: bool = False,
        session_rule: SessionRule = None,
        session_hold: bool = False,
        direct_rouse: bool = False,
        conflict_wait: bool = False,
        conflict_cb: Callable[[None], Coroutine] = None,
        overtime_cb: Callable[[None], Coroutine] = None,
    ) -> Callable:
        """
        使用该装饰器，将方法标记为消息事件执行器。
        任何消息经过校验后，不进行匹配和解析即可触发处理方法
        """

        def make_args(executor: AsyncFunc[None]) -> HandlerArgs:
            return HandlerArgs(
                executor=executor,
                type=MsgEventHandler,
                params=[
                    None,
                    None,
                    checker,
                    priority,
                    timeout,
                    block,
                    temp,
                    session_rule,
                    session_hold,
                    direct_rouse,
                    conflict_wait,
                    conflict_cb,
                    overtime_cb,
                ],
            )

        return make_args

    @classmethod
    def on_at_msg(
        cls,
        qid: int = None,
        matcher: BotMatcher = None,
        parser: BotParser = None,
        checker: BotChecker = None,
        priority: PriorityLevel = PriorityLevel.MEAN,
        timeout: int = None,
        block: bool = False,
        temp: bool = False,
        session_rule: SessionRule = None,
        session_hold: bool = False,
        direct_rouse: bool = False,
        conflict_wait: bool = False,
        conflict_cb: Callable[[None], Coroutine] = None,
        overtime_cb: Callable[[None], Coroutine] = None,
    ) -> Callable:
        at_checker = AtChecker(qid)
        if checker is not None:
            the_checker = at_checker & checker
        else:
            the_checker = at_checker

        def make_args(executor: AsyncFunc[None]) -> HandlerArgs:
            return HandlerArgs(
                executor=executor,
                type=MsgEventHandler,
                params=[
                    matcher,
                    parser,
                    the_checker,
                    priority,
                    timeout,
                    block,
                    temp,
                    session_rule,
                    session_hold,
                    direct_rouse,
                    conflict_wait,
                    conflict_cb,
                    overtime_cb,
                ],
            )

        return make_args


# TODO: 考虑事件处理器是否有更多部分可以放到基类中
class MsgEventHandler(IEventHandler):
    def __init__(
        self,
        executor: AsyncFunc[None],
        plugin: Plugin,
        responder: IActionResponder,
        logger: Logger,
        matcher: BotMatcher = None,
        parser: BotParser = None,
        checker: BotChecker = None,
        priority: PriorityLevel = PriorityLevel.MEAN,
        timeout: float = None,
        set_block: bool = False,
        temp: bool = False,
        session_rule: SessionRule = None,
        session_hold: bool = False,
        direct_rouse: bool = False,
        conflict_wait: bool = False,
        conflict_cb_maker: Callable[[None], Coroutine] = None,
        overtime_cb_maker: Callable[[None], Coroutine] = None,
    ) -> None:
        super().__init__(priority, timeout, set_block, temp)

        self.executor = executor
        self.responder = responder
        self.logger = logger
        self.matcher = matcher
        self.parser = parser
        self.checker = checker

        self._run_lock = aio.Lock()
        self._rule = session_rule
        self._hold = session_hold
        self._plugin = plugin
        self._direct_rouse = direct_rouse
        self._conflict_cb_maker = conflict_cb_maker
        self._overtime_cb_maker = overtime_cb_maker
        self._wait_flag = conflict_wait

        # matcher 和 parser 不能同时存在
        if matcher and parser:
            raise BotRuntimeError("参数 matcher 和 parser 不能同时存在")

        if session_rule is None:
            if session_hold or direct_rouse or conflict_wait or conflict_cb_maker:
                raise BotRuntimeError(
                    "使用 session_rule 参数后才能使用以下参数：session_hold， direct_rouse, \
                                      conflict_wait, conflict_callback"
                )

        if conflict_wait and conflict_cb_maker:
            raise BotRuntimeError(
                "参数 conflict_wait 为 True 时，conflict_callback 永远不会被调用"
            )

    def _verify(self, event: MsgEvent) -> bool:
        """
        验证事件是否有触发执行的资格（验权）
        """
        if self.checker:
            return self.checker.check(event)
        return True

    def _match(self, event: MsgEvent) -> bool:
        """
        通过验权后，尝试对事件进行匹配。
        有普通的匹配器（matcher）匹配，也可以使用解析器（parser）匹配
        """
        if self.matcher:
            return self.matcher.match(event.text)
        if self.parser:
            args_group = event._get_args(self.parser.id)
            if args_group == -1:
                args_group = self.parser.parse(event.text)
                event._store_args(self.parser.id, args_group)
            res, cmd_name, args = self.parser.test(args_group)
            if not res:
                return False
            try:
                if self.parser.need_format:
                    self.parser.format(args)
                return True
            except BotFormatFailed as e:
                msg = f"命令 {cmd_name} 参数格式化失败：\n" + e.__str__()
                action = msg_action(
                    msg, event.is_private(), event.sender.id, event.group_id
                )
                aio.create_task(self.responder.take_action(action))
                return False
        return True

    async def _run_on_ctx(
        self, coro: Coroutine, session: BotSession = None, timeout: float = None
    ) -> None:
        """
        在指定 session 上下文中运行协程。异常将会抛出
        """
        if session._handler is None:
            BotSessionManager.inject(session, self)
        try:
            s_token = SESSION_LOCAL._add_ctx(session)
            await aio.wait_for(aio.create_task(coro), timeout=timeout)
        finally:
            SESSION_LOCAL._del_ctx(s_token)
            # 这里可能因 bot 停止运行，导致退出事件执行方法时 session 为挂起态。因此需要强制唤醒
            if session._hup_signal.is_set():
                BotSessionManager._rouse(session)

    async def _run(self, event: MsgEvent) -> None:
        """
        获取 session 然后准备运行 executor
        """
        try:
            session = None
            if not self._direct_rouse:
                res = await BotSessionManager.try_attach(event, self)
                if res:
                    return
            session = await BotSessionManager.get(event, self.responder, self)
            # 如果因为冲突没有获得 session，且指定了冲突回调
            if session is None and self._conflict_cb_maker:
                temp_session = BotSessionManager.make_temp(event, self.responder)
                await self._run_on_ctx(self._conflict_cb_maker(), temp_session)
            # 如果因为冲突没有获得 session，但没有冲突回调
            if session is None:
                return
            # 如果没有冲突，正常获得到了 session
            try:
                exec_coro = self.executor(self._plugin)
                await self._run_on_ctx(exec_coro, session, self.timeout)
            except aio.TimeoutError:
                if self._overtime_cb_maker:
                    await self._run_on_ctx(self._overtime_cb_maker(), session)
        except BotExecutorQuickExit:
            pass
        except Exception as e:
            e_name = e.__class__.__name__
            executor_name = self.executor.__qualname__
            self.logger.error(
                f"插件 {self._plugin.__class__.__id__} 事件处理方法 {executor_name} 发生异常：[{e_name}] {e}"
            )
            self.logger.debug(f"异常点的事件记录为：{event.raw}")
            self.logger.debug("异常回溯栈：\n" + traceback.format_exc().strip("\n"))
        finally:
            if session is None:
                return
            BotSessionManager.recycle(session, alive=self._hold)

    async def evoke(self, event: MsgEvent) -> bool:
        """
        接收总线分发的事件的方法。返回是否决定处理的判断。
        便于 disptacher 进行优先级阻断。校验通过会自动处理事件。
        """
        if not self._verify(event):
            return False

        if self._direct_rouse:
            res = await BotSessionManager.try_attach(event, self)
            if res:
                return True

        if not self.is_valid:
            return False

        if not self._match(event):
            return False

        if not self.is_temp:
            aio.create_task(self._run(event))
            return True

        async with self._run_lock:
            if self.is_valid:
                aio.create_task(self._run(event))
                self.is_valid = False
                return True
            else:
                return False


class ReqEventHandler(IEventHandler):
    pass


class NoticeEventHandler(IEventHandler):
    pass
