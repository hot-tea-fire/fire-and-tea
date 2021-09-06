import time
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 2, 3)
    print(future.result())  # 8


import shutil
t1 = time.time()
with ThreadPoolExecutor(max_workers=1) as e:
    e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
    e.submit(shutil.copy, 'src1.txt', 'dest2.txt')
    e.submit(shutil.copy, 'src1.txt', 'dest3.txt')
    e.submit(shutil.copy, 'src1.txt', 'dest4.txt')
print(time.time() - t1)     # 0.00396418571472168
t2 = time.time()
with ThreadPoolExecutor(max_workers=4) as e:
    e.submit(shutil.copy, 'src1.txt', 'dest11.txt')
    e.submit(shutil.copy, 'src1.txt', 'dest21.txt')
    e.submit(shutil.copy, 'src1.txt', 'dest31.txt')
    e.submit(shutil.copy, 'src1.txt', 'dest41.txt')
print(time.time()-t2)       # 0.0009965896606445312
