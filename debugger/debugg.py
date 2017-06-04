from logging import basicConfig, getLogger, DEBUG
import pdb
import sys
from collections import deque

log_file = 'teste.log'
basicConfig(filename=log_file, filemode='w', level=DEBUG)
log = getLogger(__name__)


def debug(debug=False):
    def tail_log(func):
        def execute_func(*args):
            try:
                func(*args)
            except Exception as e:
                log.info('{} args:{} error:{}'.format(func.__name__, args, e))
                if debug:
                    for x in deque(open(log_file), 10):
                        print(x)
                    pdb.post_mortem(sys.exc_info()[2])
        return execute_func
    return tail_log
