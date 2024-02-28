import asyncio
import logging
import json
from dataclasses import dataclass
from logstash_async.handler import AsynchronousLogstashHandler
from .enums import LogLevel, LogCategory
from .formatter import LogFormatter


@dataclass
class LogEvent:
    message: str
    level: LogLevel
    category: LogCategory
    code: str


def setup_logging(logstash_host, logstash_port):
    # Use a consistent name to retrieve the same logger instance
    logger = logging.getLogger('python-logstash-logger')

    # Check if the logger has already been configured
    if not hasattr(logger, 'is_configured') or not logger.is_configured:
        logger.setLevel(logging.DEBUG)

        # Create and configure the Logstash handler only once
        logstash_handler = AsynchronousLogstashHandler(
            host=logstash_host,
            port=logstash_port,
            database_path='logstash.db',
            event_ttl=3000
        )
        logstash_handler.setFormatter(LogFormatter())
        logger.addHandler(logstash_handler)

        # Mark the logger as configured
        logger.is_configured = True
    else:
        # Optionally, log that the logger is already configured or take other appropriate actions
        pass

    return logger


async def async_custom_log(logger, event: LogEvent, **kwargs):
    """
    Asynchronously logs a message encapsulated within a LogEvent object,
    along with customizable parameters.

    Parameters:
    - logger: The logger instance to use for logging.
    - event (LogEvent): The event object containing the log message, level, category, and code.
    - Any other keyword arguments are treated as extra fields for the log.
    """

    def sync_log():
        try:
            level_to_logging_func = {
                LogLevel.INFO: logger.info,
                LogLevel.WARN: logger.warning,
                LogLevel.ERROR: logger.error,
                LogLevel.CRITICAL: logger.critical,
            }

            logging_func = level_to_logging_func.get(event.level, lambda msg, **kw: logger.error(
                f"Unknown log level: {event.level}, {msg}", **kw))

            # Prepare extra fields for structured logging
            extra_fields = {
                'category': event.category,
                'code': event.code,
                **kwargs
            }

            # Serialize eventData safely if present in kwargs
            if 'eventData' in extra_fields:
                extra_fields['eventData'] = json.dumps(extra_fields['eventData'], default=str)

            logging_func(event.message, extra=extra_fields)
        except Exception as e:
            logger.error(f"Failed to log event due to an error: {e}", exc_info=True)

    await asyncio.to_thread(sync_log)

