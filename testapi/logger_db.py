import logging
import datetime


class SmsLogHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
            from testapi.models import SmsLog
            logEntry = SmsLog(level=record.levelname,
                              message=record.msg,
                              info=record.info,
                              timestamp=datetime.datetime.now())
            logEntry.save()
