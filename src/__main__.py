# region [Imports]

import src.utility.gidlogger.logger_functions as glog

# endregion [Imports]

__updated__ = '2020-10-03 09:47:47'

_log_file = glog.log_folderer('__main__')
log = glog.main_logger(_log_file, 'debug')
log.info(glog.NEWRUN())


if __name__ == '__main__':
    pass
