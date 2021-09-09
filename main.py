import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(236236)

if __name__ == '__main__':
    print('hello world')
    while 1:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(2)
    print('print hello world again')
