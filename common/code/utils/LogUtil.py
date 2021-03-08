# Author Jill
# Date 2021/3/8
import datetime
import logging
# 操作系统交互
import os
import platform

cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
LOG_PATH = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)  # 如果不存在这个logs文件夹，就自动创建一个
log_file = os.path.join(LOG_PATH, 'asm.log')
if not os.path.exists(log_file):
    os.system(r"touch {}".format(log_file))  # 如果不存在这个文件，就自动创建一个


def get_logging_file():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    dir_name = 'python_log'
    if platform.platform().startswith('Window'):
        # 主盘符 系统对应的文件位置格式
        log_file_path = os.path.join(os.getenv('HOMEDRIVE'), dir_name)
    else:
        log_file_path = os.path.join(os.getenv('HOME'), dir_name)
    if not os.path.exists(log_file_path):
        os.mkdir(log_file_path)
    log_path = os.path.join(log_file_path, today + '.log')
    if not os.path.exists(log_path):
        os.system(r"touch {}".format(log_path))  # 如果不存在这个文件，就自动创建一个
    return log_path


print(get_logging_file())

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s :%(levelname)s:%(message)s', filename=get_logging_file(), filemode='a'
)

logging.debug("start")
logging.info("abc")
logging.warning("end")
