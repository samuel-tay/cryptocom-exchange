import asyncio
import platform

from . import coins, pairs, networks
from .api import ApiError, ApiProvider
from .market import Exchange
from .private import Account
from .structs import (
    Candle,
    Coin,
    Deposit,
    DepositStatus,
    MarketTrade,
    Network,
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
    Pair,
    Period,
    PrivateTrade,
    Timeframe,
    Withdrawal,
    WithdrawalStatus,
)

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

__all__ = [
    "Order",
    "OrderSide",
    "OrderStatus",
    "OrderType",
    "pairs",
    "Pair",
    "coins",
    "Coin",
    "Period",
    "Candle",
    "MarketTrade",
    "networks",
    "Network",
    "PrivateTrade",
    "Timeframe",
    "Deposit",
    "Withdrawal",
    "DepositStatus",
    "WithdrawalStatus",
    "Exchange",
    "Account",
    "ApiError",
    "ApiProvider",
]
