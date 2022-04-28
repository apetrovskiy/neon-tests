from enum import Enum


class Unit(Enum):
    WEI = "wei"
    KWEI = "kwei"
    MWEI = "mwei"
    GWEI = "gwei"
    MICRO_ETHER = "microether"
    MILLI_ETHER = "milliether"
    ETHER = "ether"

    def __str__(self):
        return self.value

    def lower(self):
        return self.value
