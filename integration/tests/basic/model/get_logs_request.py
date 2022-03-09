from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json
from typing import List, Union


@dataclass_json #(letter_case=LetterCase.CAMEL)
@dataclass
class GetLogsRequest:
    # fromBlock: Union[int, str] = None
    # toBlock: Union[int, str] = None
    from_block: Union[int, str] = None
    to_block: Union[int, str] = None
    address: List[str] = None
    topics: List[str] = None
    blockhash: List[str] = None
