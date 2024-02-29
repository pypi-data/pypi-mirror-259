import logging
import sys

def setup_logger():
    log = logging.getLogger('')
    log.setLevel(logging.INFO)

    logging.addLevelName(logging.ERROR, 'ERROR')
    logging.addLevelName(logging.WARNING, 'WARNING')
    logging.addLevelName(logging.INFO, 'INFO')
    logging.addLevelName(logging.DEBUG, 'DEBUG')

    data_fmt = f"%H:%M:%S"
    verbose_fmt = (
        "%(asctime)s,%(msecs)d %(levelname)s "
        "%(module)s:%(funcName)s():%(lineno)d   "
        "%(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(verbose_fmt, datefmt=data_fmt))
    log.addHandler(handler)

    return log