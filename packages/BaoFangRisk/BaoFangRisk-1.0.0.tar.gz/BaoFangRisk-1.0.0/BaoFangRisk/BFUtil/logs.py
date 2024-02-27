import configparser
import datetime
import os
import sys
from zenlog import logging

path = os.path.expanduser('~')
bf_path = '{}{}{}'.format(path, os.sep, '.bfrisk')


def generate_path(name):
    return '{}{}{}'.format(bf_path, os.sep, name)


def make_dir(path, exist_ok=True):
    os.makedirs(path, exist_ok=exist_ok)


setting_path = generate_path('setting')
cache_path = generate_path('cache')
log_path = generate_path('log')
download_path = generate_path('downloads')
bin_path = generate_path('bin')  # 给一些dll文件存储用
data_path = generate_path('data')  # 本地数据


make_dir(bf_path, exist_ok=True)
make_dir(setting_path, exist_ok=True)
make_dir(cache_path, exist_ok=True)
make_dir(download_path, exist_ok=True)
make_dir(log_path, exist_ok=True)
make_dir(bin_path, exist_ok=True)
make_dir(data_path, exist_ok=True)


try:
    _name = '{}{}bfRisk{}-{}-.log'.format(
        log_path,
        os.sep,
        os.path.basename(sys.argv[0]).split('.py')[0],
        str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    )
except:
    _name = '{}{}bfRisk-{}-.log'.format(
        log_path,
        os.sep,
        str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    )

logger = logging.getLogger()
while len(logger.handlers)>0:
    for h in logger.handlers:
        logger.removeHandler(h)

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s bfRisk>>>%(message)s',
    datefmt='%H:%M:%S',
    filename=_name,
    filemode='w',
)
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
formatter = logging.Formatter('bfRisk>>>%(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def bf_util_log_debug(logs, ui_log=None, ui_progress=None):
    logging.debug(logs)


def bf_util_log_info(logs, ui_log=None, ui_progress=None, ui_progress_int_value=None):
    logging.warning(logs)

    # 给GUI使用，更新当前任务到日志和进度
    if ui_log is not None:
        if isinstance(logs, str):
            ui_log.emit(logs)
        if isinstance(logs, list):
            for iStr in logs:
                ui_log.emit(iStr)

    if ui_progress is not None and ui_progress_int_value is not None:
        ui_progress.emit(ui_progress_int_value)


def bf_util_log_expection(logs, ui_log=None, ui_progress=None):
    logging.exception(logs)