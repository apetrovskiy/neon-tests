from dataclasses import dataclass
from typing import List


@dataclass
class CallRequest:
    from1: List[str]
    to: List[str]
    gas: int
    gasPrice: int
    value: int
    data: List[str]
