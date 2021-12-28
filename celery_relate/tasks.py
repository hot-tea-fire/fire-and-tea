from celery import Celery

app = Celery('tasks',
             broker='redis://:123456@127.0.0.1:6379/1',
             backend='redis://:123456@127.0.0.1:6379/1')


@app.task
def add(x, y):
    print('加法', x, y)
    return x + y
