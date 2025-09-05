from sonic_engine.model.extension import LogConfig
from sonic_engine.util.dataclass import nested_dataclass
from typing import Literal
import logging

logging.basicConfig(format="%(name)s [%(levelname)s] %(message)s")


@nested_dataclass
class LogOptions:
    "Extension log options"

    level: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"] = "DEBUG"
    "Log level"

    dir: str = "./logs"
    "Path to the logs folder"
