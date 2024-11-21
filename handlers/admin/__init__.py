from aiogram import Router, Dispatcher

from filters import BasicFilter

__all__ = [
    'setup'
]


admin_router = Router(name="admin_router")
admin_router.message.filter(
    BasicFilter('private', 'admin')
)
