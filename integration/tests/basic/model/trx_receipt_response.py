from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json
from typing import Any, List, Union


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TrxReceiptResponse:
    # transactionHash: str
    # transactionIndex: int
    # blockHash: str
    # blockNumber: int
    # from_: str
    # to: str
    # cumulativeGasUsed: int
    # gasUsed: int
    # contractAddress: Union[str, None]
    # logs: List[Any]
    # logsBloom: str
    # root: Any
    # status: Union[1, 0]
    transaction_hash: str
    transaction_index: int
    block_hash: str
    block_number: int
    from_: str
    to: str
    cumulative_gas_used: int
    gas_used: int
    contract_address: Union[str, None]
    logs: List[Any]
    logs_bloom: str
    root: Any
    status: Union[1, 0]