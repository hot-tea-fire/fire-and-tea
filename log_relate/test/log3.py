import logging

# 记录器、处理器、过滤器和格式器。


# create logger     记录器
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug  处理器
# 常见的有StreamHandler 和 FileHandler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter      格式器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 2021-08-24 15:40:55,914 - simple_example - DEBUG - critical message

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger   addHandler 用于给记录器添加0个或多个处理器
logger.addHandler(ch)


# create console handler and set level to debug  处理器
# 常见的有StreamHandler 和 FileHandler
dh = logging.StreamHandler()
dh.setLevel(logging.DEBUG)

# create formatter      格式器
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# 2021-08-24 15:40:55,914 - simple_example - DEBUG - critical message

# add formatter to ch
dh.setFormatter(formatter)

# add ch to logger   addHandler 用于给记录器添加0个或多个处理器
logger.addHandler(dh)


# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

