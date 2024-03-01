# TODO: 此脚本包装成公共package
from aliyun.log import LogClient, PutLogsRequest, LogItem
import time
from enum import Enum


DEFAULT_SCENARIO = "default"


class LogLevel(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class AliyunLogger:
    def __init__(self, endpoint, accessKeyId, accessKey, project_name, logstore_name):

        self.project_name = project_name
        self.logstore_name = logstore_name
        self.client = LogClient(endpoint, accessKeyId, accessKey)

    def put_log(self, contents, level, compress=False):
        topic = level
        source = ""

        logitemList = []  # LogItem list
        logItem = LogItem()
        logItem.set_time(int(time.time()))
        logItem.set_contents(contents)
        logitemList.append(logItem)
        request = PutLogsRequest(
            self.project_name,
            self.logstore_name,
            topic,
            source,
            logitemList,
            compress=compress,
        )

        self.client.put_logs(request)

    def info(self, contents):
        self.put_log(contents, LogLevel.INFO.value)

    def warning(self, contents):
        self.put_log(contents, LogLevel.WARNING.value)

    def error(self, contents):
        self.put_log(contents, LogLevel.ERROR.value)
