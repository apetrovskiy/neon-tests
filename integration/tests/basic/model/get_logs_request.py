from dataclasses import dataclass
from typing import List, Union


@dataclass
class GetLogsRequest:
    fromBlock: Union[int, str]
    toBlock: Union[int, str]
    address: List[str]
    topics: List[str]
    blockhash: List[str]
