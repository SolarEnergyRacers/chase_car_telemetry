from dataclasses import dataclass

@dataclass
class DataPoint:
    measurement: str
    type: str
    value_f: float
    value_i: int
    value_b: bool
    timestamp: int
