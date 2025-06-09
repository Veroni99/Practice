import sys
from datetime import datetime
from typing import List, Protocol

class Formatter(Protocol):
    def format(self, message: str) -> str:
        ...

class SimpleFormatter:
    def format(self, message: str) -> str:
        return message

class TimeFormatter:
    def __init__(self, time_format: str = "%Y-%m-%d %H:%M:%S"):
        self.time_format = time_format

    def format(self, message: str) -> str:
        timestamp = datetime.now().strftime(self.time_format)
        return f"[{timestamp}] {message}"

class Handler(Protocol):
    def handle(self, message: str):
        ...

class StreamHandler:
    def __init__(self, stream):
        self.stream = stream

    def handle(self, message: str):
        self.stream.write(message + "\n")

class Logger:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter
        self.handlers: List[Handler] = []

    def add_handler(self, handler: Handler):
        self.handlers.append(handler)

    def log(self, message: str):
        formatted = self.formatter.format(message)
        for handler in self.handlers:
            handler.handle(formatted)

if __name__ == "__main__":
    formatter = TimeFormatter("%H:%M:%S")
    logger = Logger(formatter)

    stderr_handler = StreamHandler(sys.stderr)
    stdout_handler = StreamHandler(sys.stdout)

    logger.add_handler(stderr_handler)
    logger.add_handler(stdout_handler)

    logger.log("Це тестове повідомлення")
