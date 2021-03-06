# -*- coding:utf-8 -*-

import os
import logging
from datetime import datetime
import threading
import readConfig


class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, 'result')
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(os.path.join(logPath, 'output.log'))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_log(self):
        return self.logger

    def build_start_line(self, case_no):
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        self.logger.info(case_name + " - Code:" + code + " - msg:" + msg)

    def get_report_path(self):
        report_path = os.path.join(logPath, "report.html")
        return report_path

    def get_result_path(self):
        return logPath

    def write_result(self, result):
        result_path = os.path.join(logPath, "report.txt")
        try:
            with open(result_path, "wb") as fb:
                fb.write(result)
        except FileNotFoundError as ex:
            self.logger.error(str(ex))


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log


if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_log()
    logger.debug("test debug")
    logger.info("test info")
