import logging

log_path = '../logs/log_test.log'
logging.basicConfig(filename=log_path, encoding='utf-8', filemode='w', level=logging.DEBUG)

# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
#
# log2.do_something()

logging.warning('%s before is %s', 'start', 'after')


