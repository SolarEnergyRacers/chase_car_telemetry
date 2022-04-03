from dataclasses import dataclass

@dataclass
class DataPoint:
    timestamp: int
    measurement: str
    type: str
    value_f: float
    value_i: int
    value_b: bool
