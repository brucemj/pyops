# -*- coding: UTF-8 -*-
import logging

def console_set(logFilename='pylog.log' , lvl=0):
    '''
       Output log to file and console
       args :  logFilename='pylog.log' , lvl=1-5 : DEBUG, INFO, WARNING, ERROR, CRITICAL
    '''

    # Define a Handler and set a format which output to file
    lvl_info = [ logging.DEBUG, logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    logging.basicConfig(
                    level    = lvl_info[lvl],              # 定义输出到文件的log级别，
                    format   = '%(asctime)s  %(filename)s : %(levelname)s  %(message)s',    # 定义输出log的格式
                    datefmt  = '%Y-%m-%d %A %H:%M:%S',                                     # 时间
                    filename = logFilename,                # log文件名
                    filemode = 'a')                        # 写入模式“w”或“a”
    # Define a Handler and set a format which output to console
    console = logging.StreamHandler()                  # 定义console handler
    console.setLevel(logging.INFO)                     # 定义该handler级别
    formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  #定义该handler格式
    console.setFormatter(formatter)
    # Create an instance
    logging.getLogger().addHandler(console)           # 实例化添加handler
    return logging
