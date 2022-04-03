from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class DataPoint:
    measurement: str
    tags: Dict
    timestamp: int = 0
    value: Any = None

    def asInfluxString(self):
        return ""