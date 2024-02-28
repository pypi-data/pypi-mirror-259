import json
import logging
import unittest
from unittest.mock import patch, MagicMock
from logstash_logging import async_custom_log, setup_logging, LogEvent, LogLevel, LogFormatter, Platform, LogCategory


class CustomLoggerTest(unittest.TestCase):
    def setUp(self):
        self.logger = MagicMock()  # Using MagicMock to simulate logger behavior

    @patch('logstash_logging.logstash_logger.logging.getLogger')
    def test_setup_logging(self, mock_get_logger):
        """Test that setup_logging configures the logger correctly."""
        configured_logger = setup_logging(logstash_host="localhost", logstash_port=5959)
        self.assertTrue(configured_logger.is_configured)

    async def test_async_custom_log_info(self):
        """Test async_custom_log with INFO level LogEvent."""
        event = LogEvent(
            message="Test info",
            level=LogLevel.INFO,
            category=LogCategory.APPLICATION,
            code="REQUEST"
        )
        await async_custom_log(self.logger, event)
        self.logger.info.assert_called_once()

    async def test_async_custom_log_warn(self):
        """Test async_custom_log with WARN level LogEvent."""
        event = LogEvent(
            message="Test warn",
            level=LogLevel.WARN,
            category=LogCategory.APPLICATION,
            code="WARNING"
        )
        await async_custom_log(self.logger, event)
        self.logger.warning.assert_called_once()

    async def test_async_custom_log_error(self):
        """Test async_custom_log with ERROR level LogEvent."""
        event = LogEvent(
            message="Test error",
            level=LogLevel.ERROR,
            category=LogCategory.APPLICATION,
            code="ERROR"
        )
        await async_custom_log(self.logger, event)
        self.logger.error.assert_called_once()

    async def test_async_custom_log_critical(self):
        """Test async_custom_log with CRITICAL level LogEvent."""
        event = LogEvent(
            message="Test critical",
            level=LogLevel.CRITICAL,
            category=LogCategory.APPLICATION,
            code="CRITICAL"
        )
        await async_custom_log(self.logger, event)
        self.logger.critical.assert_called_once()

    async def test_async_custom_log_with_extra_fields(self):
        """Test async_custom_log with extra fields."""
        event = LogEvent(
            message="Test message with extra",
            level=LogLevel.INFO,
            category=LogCategory.APPLICATION,
            code="REQUEST_EXTRA"
        )
        extra_fields = {'userAgent': 'test-agent', 'eventData': {'key': 'value'}}
        await async_custom_log(self.logger, event, **extra_fields)
        self.logger.info.assert_called_once()
        args, kwargs = self.logger.info.call_args
        self.assertIn('extra', kwargs)
        self.assertIn('category', kwargs['extra'])
        self.assertEqual(kwargs['extra']['category'], event.category)
        self.assertIn('code', kwargs['extra'])
        self.assertEqual(kwargs['extra']['code'], event.code)

    def test_log_formatter(self):
        """Test the LogFormatter class."""
        formatter = LogFormatter()
        record = logging.makeLogRecord({
            'levelname': 'INFO',
            'msg': 'Test message',
            'args': (),
            'source': 'test-source',
            'category': LogCategory.APPLICATION,
            'code': 'test-code',
            'userAgent': 'test-agent',
            'eventData': json.dumps({'key': 'value'}),
            'platform': Platform.WEB,
        })
        formatted = formatter.format(record)
        log_message = json.loads(formatted)
        self.assertEqual(log_message['message'], 'Test message')
        self.assertEqual(log_message['platform'], "WEB")
        self.assertEqual(log_message['category'], "APPLICATION")
        self.assertTrue('timeStamp' in log_message)


if __name__ == '__main__':
    unittest.main()
