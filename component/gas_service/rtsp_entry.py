from collections import deque
from logging import getLogger
from typing import List, Optional, Callable, Dict
from threading import Thread
from multiprocessing import Process, Manager

from component.gas_service.daemon_service import execute_callback, ServiceThread
from component.gas_service.rtsp_service import set_rtsp_url, set_rtsp_device_id, rtsp_stream_service_mapper

logger = getLogger('defence')

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

class Defence(Process):
    def __init__(self, device_id: str, station_key: str, org_id: int, rtsp_url: str):
        # self.daemon = False

        self.frame_cache = deque(maxlen=4)
        self.cutter_cache = deque(maxlen=4)
        self.processor_cache = deque(maxlen=4)

        self.device_id: str = device_id
        self.station_key: str = station_key
        self.rtsp_url: str = rtsp_url
        self.org_id: int = org_id

        Process.__init__(self, daemon=True, name=self.device_id)
        self.start()

        logger.info(f'布防进程启动 {str(self.pid)} 设备ID: {self.device_id} 站点Key: {self.station_key}')

    def run(self) -> None:

        # 设置取流service线程
        self.rtsp_url = 'rtsp://admin:hk123456@192.168.2.25'       # 直接走摄像头
        # self.rtsp_url = 'rtsp://192.168.2.92/51342330001328100002/51342330001328100002'    # 走姚的流媒体
        # self.rtsp_url = f'rtsp://{RTSP_HOST}/{self.device_id}/{self.device_id}'
        set_rtsp_url(rtsp_url=self.rtsp_url)
        set_rtsp_device_id(device_id=self.device_id)

        manager = DaemonServiceManager()
        manager.register_service(**rtsp_stream_service_mapper)

if __name__ == '__main__':
    de = Defence()
    de.start()
