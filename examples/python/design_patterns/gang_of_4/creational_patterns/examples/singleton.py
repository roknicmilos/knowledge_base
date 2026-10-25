"""
Singleton Pattern

What it does:
    Ensures a class has only one instance and provides a global
    point of access to it.
"""

import threading
from datetime import datetime


class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # Thread-safe singleton using double-checked locking
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize the logger (called only once)"""
        self._log_buffer = []
        self._buffer_lock = threading.Lock()
        self.log("Logger initialized")

    def log(self, message):
        """Log a message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"

        with self._buffer_lock:
            self._log_buffer.append(log_entry)
            print(log_entry)

    def error(self, message):
        """Log an error message"""
        self.log(f"ERROR: {message}")

    def info(self, message):
        """Log an info message"""
        self.log(f"INFO: {message}")

    def warning(self, message):
        """Log a warning message"""
        self.log(f"WARNING: {message}")

    def get_log(self):
        """Return all logged messages"""
        with self._buffer_lock:
            return "\n".join(self._log_buffer)

    def clear(self):
        """Clear the log buffer"""
        with self._buffer_lock:
            self._log_buffer.clear()


# Usage example
if __name__ == "__main__":
    # Create logger instance
    logger = Logger()

    logger.info("Application started")
    logger.log("Processing data...")
    logger.warning("Low memory")
    logger.error("File not found")

    # Same instance everywhere
    same_logger = Logger()
    same_logger.info("Still the same logger")

    # Verify it's the same instance
    print(f"\nSame instance? {logger is same_logger}")

    print("\n=== Full Log ===")
    print(logger.get_log())
