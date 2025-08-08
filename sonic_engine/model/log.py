from sonic_engine.model.extension import LogConfig
from sonic_engine.util.dataclass import nested_dataclass
from typing import Literal
import logging

logging.basicConfig(format="%(name)s [%(levelname)s] %(message)s")


class Logger:
    def __init__(self, config: LogConfig, ctx: str):
        self.ctx = ctx
        self.config = config
        self.level = getattr(logging, config.level)
        self.l = logging.getLogger(name=ctx)
        self.l.setLevel(self.level)

    def log(self, level: int, msg: str, *args):
        msg = " ".join((str(arg) for arg in (msg,) + args))
        self.l.log(level, msg)

    def debug(self, msg: str, *args):
        self.log(logging.DEBUG, str(msg), *args)

    def info(self, msg: str, *args):
        self.log(logging.INFO, str(msg), *args)

    def warning(self, msg: str, *args):
        self.log(logging.WARNING, str(msg), *args)

    def error(self, msg: str, *args):
        self.log(logging.ERROR, str(msg), *args)

    def critical(self, msg: str, *args):
        self.log(logging.CRITICAL, str(msg), *args)
