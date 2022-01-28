import time
import cv2
from queue import Queue

from concurrent.futures import ThreadPoolExecutor, Future

_thread_pool: ThreadPoolExecutor = ThreadPoolExecutor(16)




def cv2_stream_dump(RTSP_URL, i):
    print('read stream', i)
    # build VideoCapture
    # rtsp_client = cv2.VideoCapture(RTSP_URL)
    frame_width = 1080
    frame_height = 1920
    # uri = f"rtspsrc location=rtsp://admin:hk123456@192.168.4.188 latency=0 ! queue ! rtph264depay ! h264parse ! nvv4l2decoder ! nvvideoconvert ! video/x-raw, width={frame_width}, height={frame_height}, format=RGB ! appsink"
    rtsp_client = cv2.VideoCapture(RTSP_URL)
    rtsp_client.set(cv2.CAP_PROP_FPS, 10)
    state, image = rtsp_client.read()
    # assert state, 'RTSP不能正常取流'
    # assert len(image.tobytes()) == 1920 * 1080 * 3, f'图像大小错误. {len(image.tobytes())}'

    failed_count = 0
    while failed_count < 10:
        try:
            state, image = rtsp_client.read()
            # assert state, 'RTSP无图像帧'

            # if state:
            # TODO: local import.
            #    from gas_arithmetic_service_50.shared_memory_tools import dump_image_into_shared_memory
            # 转为字节流存入共享内存
            #    dump_image_into_shared_memory(str(i), image)

            # 每10秒写入一次磁盘用于检查是否正常取流
            # if (int(time.time()) % 10 == 0) and not (platform.system() == 'Windows'):
            #    cv2.imwrite(rf'/gas/cache/{DEVICE_ID}.jpg', image)
            # print('read stream', i)
            # cv2.imshow("image", image)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                continue

        except AssertionError as ae:
            print(f'{ae} failed_count: {failed_count}')
            failed_count += 1

        except Exception as e:
            print('取流异常', exc_info=e)
            failed_count += 1


# def fetch_from_sharedMemory(i):
#     from gas_arithmetic_service_50.shared_memory_tools import load_image_from_shared_memory
#     print('read', i)
#     for i in range(20000):
#         image = load_image_from_shared_memory(str(i))
#
#     return True


def initial_callback_1():
    print("initial_callback")


def check_callback_1():
    print("check_callback")


def failed_callback_1():
    print("failed_callback")


test_producer_mapper = {
    'service_name': 'kafka_producer',
    'check_callback': check_callback_1,
    'failed_callback': failed_callback_1,
    'initial_callback': initial_callback_1,
    'callback_time_limit': 10,
    'check_cycle': 5 * 60,
}

if __name__ == '__main__':
    # RTSP_URL = 'rtsp://192.168.1.190/51342330001328100010/51342330001328100010'
    RTSP_URL = 'rtsp://admin:hk123456@192.168.4.188'
    # RTSP_URL = 'rtsp://192.168.2.92/51342330001328100002/51342330001328100002'
    # RTSP_URL = 'rtsp://192.168.2.241/6ee9206f-5955-43bb-9bc3-c3d104355934/6ee9206f-5955-43bb-9bc3-c3d104355934'
    # DEVICE_ID = '51342330001328100010'
    # DEVICE_ID = '51342330001328100002'

    '''
    manager = DaemonServiceManager()
    manager.register_service(**test_producer_mapper)
    '''

    for i in range(1):
        _thread_future = _thread_pool.submit(cv2_stream_dump, RTSP_URL, i)
        print('开启RTSP取流服务', i)
        time.sleep(1)

    time.sleep(2)

    # for i in range(0) :
    #    _thread_future = _thread_pool.submit(fetch_from_sharedMemory, i)
    #    print('开启ShareMemory取服务', i)
    #    time.sleep(1)

    input('Enter any key to Exit.')
