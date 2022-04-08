from enum import Enum


class ErrorMessage(Enum):
    NEGATIVE_VALUE = "Resulting wei value must be between 1 and 2**256 - 1"
    INSUFFICIENT_FUNDS = "insufficient funds for transfer"
    GAS_LIMIT_REACHED = "ValueError: {'code': -32000, 'message': 'gas limit reached: have 1 want'}"
