from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class DataPoint:
    measurement: str
    tags: Dict
    time: int
    fields: Dict


    def asInfluxString(self):
        return ""