# -*- coding: utf-8 -*-
"""服务线程管理器。

把特定的代码封装为全局线程，自动在后台周期性运行特定的函数。

主要用于数据库连接，Kafka连接或者socket长连接等等。


"""
import time
from typing import List, Optional, Callable, Dict
from types import FunctionType
from logging import getLogger

from threading import Thread
from concurrent.futures import ThreadPoolExecutor, TimeoutError


def execute_callback(callback: Callable, timeout):
    try:
        with ThreadPoolExecutor(1) as pool:
            future = pool.submit(callback)
            result = future.result(timeout)
    except Exception as e:
        return e
    else:
        return result


class ServiceThread(Thread):

    def __init__(self,
                 name: str,
                 check_callback: Callable[..., bool],
                 success_callback: Optional[Callable[..., bool]] = None,
                 failed_callback: Optional[Callable[..., bool]] = None,
                 initial_callback: Optional[Callable] = None,
                 callback_time_limit: int = 5,
                 check_cycle: int = 5 * 60,
                 ) -> None:
        super().__init__(name=name, daemon=True)
        self.logger = getLogger(name)

        self.check_callback = check_callback if isinstance(check_callback, FunctionType) else lambda: True
        self.success_callback = success_callback if isinstance(success_callback, FunctionType) else lambda: True
        self.failed_callback = failed_callback if isinstance(failed_callback, FunctionType) else lambda: True

        # TODO: initial callback in thread?
        self.initial_callback = initial_callback if isinstance(initial_callback, FunctionType) else lambda: True

        self.callback_time_limit = callback_time_limit
        self.check_cycle = check_cycle

        self.exit_flag = True

    def run(self) -> None:

        while self.exit_flag:
            check_result = execute_callback(self.check_callback, self.callback_time_limit)

            try:
                if isinstance(check_result, Exception) or not check_result:
                    self.logger.info('Failed in check', exc_info=check_result)
                    action_result = execute_callback(self.failed_callback, self.callback_time_limit)
                else:
                    self.logger.info(f'Success in check: {check_result}')
                    action_result = execute_callback(self.success_callback, self.callback_time_limit)

                if isinstance(action_result, Exception):
                    self.logger.info('Failed in action', exc_info=action_result)
                else:
                    self.logger.info('Success in action')
            except:
                pass

            time.sleep(self.check_cycle)


class DaemonServiceManager(object):

    def __init__(self,
                 callback_time_limit: int = 5,
                 check_cycle: int = 5 * 60,
                 ) -> None:
        self.callback_time_limit = callback_time_limit
        self.check_cycle = check_cycle

        self.service_mapper: Dict[str, Thread] = {}

    def register_service(self,
                         service_name: str,
                         check_callback: Callable[..., bool],
                         success_callback: Optional[Callable[..., bool]] = None,
                         failed_callback: Optional[Callable[..., bool]] = None,
                         initial_callback: Optional[Callable] = None,
                         callback_time_limit: int = None,
                         check_cycle: int = None,
                         ):

        callback_time_limit = callback_time_limit if callback_time_limit is not None else self.callback_time_limit
        check_cycle = check_cycle if check_cycle is not None else self.check_cycle

        if not self.service_mapper.get(service_name):
            execute_callback(initial_callback, self.callback_time_limit)

            thread = ServiceThread(
                name=service_name,
                check_callback=check_callback,
                success_callback=success_callback,
                failed_callback=failed_callback,
                # initial_callback=initial_callback,
                callback_time_limit=callback_time_limit,
                check_cycle=check_cycle
            )
            thread.start()

            self.service_mapper[service_name] = thread
