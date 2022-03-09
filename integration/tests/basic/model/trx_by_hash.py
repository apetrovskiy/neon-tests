from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json
from typing import Union


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TrxByHashResponse:
    # blockHash: str
    # blockNumber: Union[int, None]
    # from_: str
    # gas: int
    # gasPrice: int
    # hash: str
    # input: str
    # nonce: int
    # to: str
    # transactionIndex: Union[int, None]
    # value: int
    # v: int
    # r: str
    # s: str
    block_hash: str
    block_number: Union[int, None]
    from_: str
    gas: int
    gas_price: int
    hash: str
    input: str
    nonce: int
    to: str
    transaction_index: Union[int, None]
    value: int
    v: int
    r: str
    s: str