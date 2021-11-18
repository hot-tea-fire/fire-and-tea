import numpy
from multiprocessing.shared_memory import SharedMemory

def get_target_shared_memory(name: str) -> SharedMemory:
    try:
        share = SharedMemory(create=True, size=10, name=name)
    except FileExistsError:
        share = SharedMemory(create=False, name=name)
    return share


shm_a = get_target_shared_memory(name='fire')
buffer = shm_a.buf

buffer[:4] = bytes([1,2,3,45])

buffer[4] = 5
buffer[5:] = bytes(numpy.array([3,4,5,67,9]))

for i in buffer:
    print(i)

