from datetime import datetime, timezone

from fluent import handler as fluenthandler

__version__ = '1.0.0'



class ISO8601FluentRecordFormatter(fluenthandler.FluentRecordFormatter):

    def formatTime(self, record, datefmt=None):
        created = datetime.fromtimestamp(record.created, timezone.utc)
        return created.isoformat()
