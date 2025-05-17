import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import os

class LogConfig:

    LOG_DIR = "runtime/logs"
    LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
    LOG_LEVEL = logging.INFO
    
    @classmethod
    def setup_logging(cls):
        """配置全局日志记录"""
        os.makedirs(cls.LOG_DIR, exist_ok=True)
        
        logger = logging.getLogger()
        logger.setLevel(cls.LOG_LEVEL)
        
        # 清除现有的处理器（防止重复添加）
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        
        # 创建文件处理器
        file_handler = TimedRotatingFileHandler(
            filename=os.path.join(cls.LOG_DIR, cls.LOG_FILE),
            when="midnight",
            backupCount=30,
            encoding="utf-8"
        )

        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        
        # 控制台处理器
        console_handler = logging.StreamHandler(sys.stdout)
        console_formatter = ColoredFormatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

class ColoredFormatter(logging.Formatter):
    """带颜色的日志格式器"""
    COLORS = {
        logging.DEBUG: "\033[36m",    # 青色
        logging.INFO: "\033[32m",     # 绿色
        logging.WARNING: "\033[33m",  # 黄色
        logging.ERROR: "\033[31m",    # 红色
        logging.CRITICAL: "\033[1;31m"  # 粗体红色
    }
    RESET = "\033[0m"
    
    def format(self, record):
        color = self.COLORS.get(record.levelno, "")
        message = super().format(record)
        return f"{color}{message}{self.RESET}"
