import logging
import json
from datetime import datetime
from enum import Enum
from .enums import LogCategory, Platform


class LogFormatter(logging.Formatter):
    def format(self, record):
        log_message = {
            'timeStamp': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ[GMT]'),
            'source': getattr(record, 'source', 'unknown-source'),
            'category': getattr(record, 'category', LogCategory.SYSTEM).name if isinstance(getattr(record, 'category', None), Enum) else 'unknown-category',
            'level': record.levelname,
            'code': getattr(record, 'code', 'unknown-code'),
            'message': record.getMessage(),
            'userAgent': getattr(record, 'userAgent', 'unknown-userAgent'),
            'eventData': getattr(record, 'eventData', '{}'),
            'platform': getattr(record, 'platform', Platform.WEB).name if isinstance(getattr(record, 'platform', None), Enum) else 'unknown-platform',
        }
        return json.dumps(log_message)
