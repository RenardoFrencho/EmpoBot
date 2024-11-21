from typing import Sequence

from aiogram.filters import BaseFilter
from aiogram.types import Message

from setup import ADMIN_ID

from loguru import logger


class BasicFilter(BaseFilter):
    
    def __init__(self, chat_type: str, role: str) -> None:
        self.chat_type = chat_type
        self.role = role

    async def __call__(self, message: Message) -> bool:
        if message.chat.type == self.chat_type:
            if self.role == 'admin' and message.from_user.id == ADMIN_ID: return True
            elif self.role == 'user' and message.from_user.id != ADMIN_ID: return True
            return True
        return False
