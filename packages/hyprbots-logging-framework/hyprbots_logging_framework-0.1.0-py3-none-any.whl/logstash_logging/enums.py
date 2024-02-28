from enum import Enum


class LogCategory(Enum):
    SECURITY = 'SECURITY'
    PERFORMANCE = 'PERFORMANCE'
    SYSTEM = 'SYSTEM'
    APPLICATION = 'APPLICATION'


class LogLevel(Enum):
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


class Platform(Enum):
    WEB = 'WEB'
    ANDROID = 'ANDROID'
    IOS = 'IOS'
