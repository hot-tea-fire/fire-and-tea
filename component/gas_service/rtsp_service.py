# -*- coding: utf-8 -*-
"""RTSP取流服务.

"""
import time
import platform

import cv2

from concurrent.futures import ThreadPoolExecutor, Future
from typing import Optional
from logging import getLogger

logger = getLogger('rtsp')

_thread_pool: ThreadPoolExecutor = ThreadPoolExecutor(1)
"""ThreadPoolExecutor: 模块线程池"""

RTSP_URL: Optional[str] = None
"""Optional[str]: RTSP 地址"""
DEVICE_ID: Optional[str] = None
"""Optional[str]: 设备ID"""

_thread_future: Optional[Future] = None
"""Optional[Future]: 当前图像处理线程的Future"""

_rtsp_client: Optional[cv2.VideoCapture] = None
"""Optional[cv2.VideoCapture]: cv2取流对象"""


def set_rtsp_url(rtsp_url) -> str:
    global RTSP_URL
    RTSP_URL = rtsp_url
    logger.info(f'RTSP取流地址设置为 {RTSP_URL}')
    return RTSP_URL


def set_rtsp_device_id(device_id) -> str:
    global DEVICE_ID
    DEVICE_ID = device_id
    return DEVICE_ID


def build_rtsp_stream_service():
    global _rtsp_client, _thread_future

    # build VideoCapture
    _rtsp_client = cv2.VideoCapture(RTSP_URL)
    _rtsp_client.set(cv2.CAP_PROP_FPS, 10)
    state, image = _rtsp_client.read()
    assert state, 'RTSP不能正常取流'
    # assert len(image.tobytes()) == 1920 * 1080 * 3, f'图像大小错误. {len(image.tobytes())}'

    _thread_future = _thread_pool.submit(cv2_stream_dump, _rtsp_client)

    assert _thread_future.running(), 'RTSP线程异常'

    logger.info('开启RTSP取流服务')
    return True


def check_rtsp_stream_service() -> bool:
    if not _rtsp_client.isOpened():
        logger.error('RTSP取流对象已关闭')
        return False

    # state, image = _rtsp_client.read()
    # if not state:
    #     logger.error('RTSP取流对象不能正常取流')
    #     return False

    if not _thread_future.running():
        logger.error('RTSP取流线程已退出')
        return False
    logger.info('取流服务正常')
    return True


def cv2_stream_dump(rtsp_client: cv2.VideoCapture):
    failed_count = 0
    from gas_arithmetic_service_50.shared_memory_tools import dump_image_into_shared_memory
    logger.info(f'摄像机  开始取流')
    while failed_count < 2:
        try:
            state, image = rtsp_client.read()
            assert state, 'RTSP无图像帧'

            if state:
                # 转为字节流存入共享内存
                dump_image_into_shared_memory(DEVICE_ID, image)

                # 每10秒写入一次磁盘用于检查是否正常取流
                # if (int(time.time()) % 10 == 0) and not (platform.system() == 'Windows'):
                #     cv2.imwrite(rf'/gas/cache/{DEVICE_ID}.jpg', image)

        except AssertionError as ae:
            logger.error(f'{ae} failed_count: {failed_count}')
            failed_count += 1

        except Exception as e:
            logger.error('取流异常', exc_info=e)
            failed_count += 1
    rtsp_client.release()


rtsp_stream_service_mapper = {
    'service_name': 'rtsp',
    'check_callback': check_rtsp_stream_service,
    'failed_callback': build_rtsp_stream_service,
    'initial_callback': build_rtsp_stream_service,
    'callback_time_limit': 5,
    'check_cycle': 60,
}

if __name__ == '__main__':
    # RTSP_URL = 'rtsp://192.168.1.190/51342330001328100010/51342330001328100010'
    RTSP_URL = 'rtsp://admin:hk123456@192.168.2.25'
    RTSP_URL = 'rtsp://192.168.2.241/6ee9206f-5955-43bb-9bc3-c3d104355934/6ee9206f-5955-43bb-9bc3-c3d104355934'
    DEVICE_ID = '51342330001328100010'
    # DEVICE_ID = '51342330001328100002'
    from gas_arithmetic_service_50.daemon_service import DaemonServiceManager

    manager = DaemonServiceManager()

    manager.register_service(**rtsp_stream_service_mapper)

    time.sleep(2)
    for i in range(2000):
        from gas_arithmetic_service_50.shared_memory_tools import load_image_from_shared_memory

        image = load_image_from_shared_memory(DEVICE_ID)

        cv2.imshow('show', image)
        cv2.waitKey(50)
