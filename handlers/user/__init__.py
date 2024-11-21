from aiogram import Router, Dispatcher

from filters import BasicFilter

from handlers.user.basic import router as basic_user_router
from handlers.user.order import router as order_user_router

__all__ = [
    'setup_user_routers'
]


def setup_user_routers(dp: Dispatcher) -> None:
    dp.include_routers(
        basic_user_router,
        order_user_router
    )
