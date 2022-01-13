# -*- coding: utf-8 -*-
"""涉及共享内存的工具函数

提供数个工具函数，可以优雅地将图片保存为字节流放入共享内存，或者从共享内存保存的图片。

Note:
    此模块涉及到multiprocessing.Manager。一般情况下需要在程序入口执行initial_shared_memory_lock函数

函数:

    1. initial_shared_memory_lock::

        在程序的入口调用此函数

    2. dump_image_into_shared_memory(shared_memory_name: str, image: numpy.ndarray) -> memoryview::

        "不需要其他任何操作，只需要将图片放入即可"

        raw_image = cv2.imread('image.jpg')
        dump_image_into_shared_memory("camera_01", raw_image)

    3. load_image_from_shared_memory(shared_memory_name: str) -> numpy.ndarray::

        "同样不需要其他任何操作，只需要读取同样的共享内存名即可"

        image = load_image_from_shared_memory("camera_01")
        # raw_image == image

Note:
    所有涉及到的图片都默认为1920*1080*3大小的图片!

"""
import time
from multiprocessing.shared_memory import SharedMemory
from multiprocessing import Manager, Lock
from typing import Dict, Tuple, Optional

import numpy
import cv2

manager: Optional[Manager] = None
"""共享内存的Manager，主要用于同一个memory写入读取的锁控制"""

_share_memory_cache_mapper: Dict[str, SharedMemory] = {}
"""Dict[str, SharedMemory]: 共享内存名和共享内存对象的映射关系表"""

_share_memory_lock_mapper: Optional[Dict[str, Lock]] = {}
"""Dict[str, Lock]: 共享内存名和对应的锁的映射关系表"""


def initial_shared_memory_lock():
    """初始化共享内存和锁的映射，需要在使用前执行。

    不执行此函数时，会产生一个普通的跨进程锁
    """
    global manager, _share_memory_lock_mapper
    manager = Manager()
    _share_memory_lock_mapper = manager.dict()


def _get_device_model_share_memory(shared_memory_name: str) -> Tuple[SharedMemory, Lock]:
    """从共享内存映射表中加载一个共享内存，返回共享内存对象和对应的锁。

    如果不存在（第一次加载一个）共享内存，则会创建一个1920*1080*3大小的共享内存，和相应的锁。

    Note:
        如果不在同一个进程下也可以相互访问共享内存，但会创建不一样的锁对象。

    Args:
        shared_memory_name (str): 共享内存名字，一般为device_id

    Returns:
        Tuple[SharedMemory, Lock]: 共享内存和锁的元组
    """
    # 如果不存在此共享内存键，则创建一个新的内存名-内存键值对
    if shared_memory_name not in _share_memory_cache_mapper:
        try:
            shared = SharedMemory(name=shared_memory_name, create=True, size=1920 * 1080 * 3 + 900)
        except FileExistsError:
            shared = SharedMemory(name=shared_memory_name, create=False)
            # shared.close()
            # shared.unlink()
        _share_memory_cache_mapper[shared_memory_name] = shared

    # 如果不存在锁对象，则创建一个锁对象
    if shared_memory_name not in _share_memory_lock_mapper:
        # 如果没有manager，则会创建一个普通的进程锁
        lock = manager.Lock() if manager is not None else Lock()
        _share_memory_lock_mapper[shared_memory_name] = lock

    return _share_memory_cache_mapper[shared_memory_name], _share_memory_lock_mapper[shared_memory_name]


# def dump_image_into_shared_memory(shared_memory_name: str, image: numpy.ndarray) -> memoryview:
#     """将当前的图片dump成共享内存放入当前的共享内存映射中，此操作加锁
#
#     Args:
#         shared_memory_name (str): 共享内存名
#         image (numpy.ndarray): numpy格式图片
#
#     Returns:
#         memoryview: 内存对象
#     """
#     shared_memory, lock = _get_device_model_share_memory(shared_memory_name)
#
#     with lock:
#         shared_memory.buf[:] = image.tobytes()
#     return shared_memory.buf


# def load_image_from_shared_memory(shared_memory_name: str) -> numpy.ndarray:
#     """从当前的共享内存映射中读取相应的共享内存并转换为图像，此操作加锁
#
#     Args:
#         shared_memory_name (str): 共享内存名
#
#     Returns:
#         numpy.ndarray: numpy格式图片
#     """
#     shared_memory, lock = _get_device_model_share_memory(shared_memory_name)
#
#     with lock:
#         image = numpy.frombuffer(shared_memory.buf, dtype=numpy.uint8).reshape((1080, 1920, 3))
#     return image


def dump_image_into_shared_memory(shared_memory_name: str, base64_bytes: bytes):
    """Abort 保存base64数据
    """
    shared_memory, lock = _get_device_model_share_memory(shared_memory_name)

    memory_length = len(shared_memory.buf)
    base64_bytes_length = base64_bytes.size

    assert memory_length > base64_bytes_length

    # current_time = int(1642056694)
    current_time = int(time.time())
    compress_bytes = bytearray().join([
        base64_bytes,
        bytearray(memory_length - base64_bytes_length - 7),
        current_time.to_bytes(length=4, byteorder='big'),
        base64_bytes_length.to_bytes(length=3, byteorder='big'),
    ])
    with lock:
        # print(len(shared_memory.buf))
        # print(len(compress_bytes))
        # print(f'base64_bytes_length  {base64_bytes_length}')
        shared_memory.buf[:] = compress_bytes


# abort
def load_image_from_shared_memory(shared_memory_name: str):
    """Abort 读取base64数据
    return:
        flag: 是否取到的是实时图片
        image： 图片，若非实时
    """
    shared_memory, lock = _get_device_model_share_memory(shared_memory_name)

    with lock:
        memory_bytes = shared_memory.buf.tobytes()

    base64_bytes_length = int.from_bytes(memory_bytes[-3:], byteorder='big')
    dum_time = int.from_bytes(memory_bytes[-7:-3], byteorder='big')

    if time.time() - dum_time > 5:
        print(f'从摄像头{shared_memory_name} 的共享内存中读图时，当前图片已停留超过5s，不再具有实现性，放弃本次推导')
        return False, numpy.frombuffer(memory_bytes[:base64_bytes_length], numpy.uint8).reshape((1080, 1920, 3))

    # TODO: common buffer in numpy arrays.
    # ref: https://docs.python.org/zh-cn/3/library/multiprocessing.shared_memory.html
    raw_array = numpy.frombuffer(memory_bytes[:base64_bytes_length], numpy.uint8).reshape((1080, 1920, 3))
    # image = cv2.imdecode(raw_array, cv2.IMREAD_COLOR)
    # print(f'size ------ {raw_array.shape}')
    return True, raw_array


if __name__ == '__main__':
    img = cv2.imread('/home/hadoop/car1.jpg')
    print(img.size)
    dump_image_into_shared_memory('34020000001320000006', img)

    flag, res = load_image_from_shared_memory('34020000001320000006')
    print(f'res   {res.shape}')
