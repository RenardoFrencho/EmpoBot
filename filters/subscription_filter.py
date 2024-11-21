from typing import Sequence

from aiogram import Bot
from aiogram.filters import BaseFilter
from aiogram.types import Message

from setup import ADMIN_ID, bot
from utils import text
from keyboards.inline_keyboards import subscription_verification_keyboard

from loguru import logger


class SubscriptionVerificationFilter(BaseFilter):
    
    def __init__(self, bot: Bot = bot) -> None:
        self.bot = bot

    async def __call__(self, message: Message) -> bool:
        try:
            subscription_status = await self.bot.get_chat_member('https://t.me/+KuzLRBHg--83YTU6', message.from_user.id)
            if subscription_status.status != 'left': return True
            return False
        except:
            logger.error("Cannot check subscription status")
            return True
