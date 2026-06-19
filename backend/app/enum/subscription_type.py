from enum import Enum


class SubscriptionType(str, Enum):
    FULL = "FULL"
    HALF = "HALF"
    BASIC = "BASIC"