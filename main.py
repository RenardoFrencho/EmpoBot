import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault

from handlers.user import setup_user_routers
from setup import BOT_TOKEN, bot, dp

commands = [
    BotCommand(command='start', description='Начало пользованием ботом'),
    # BotCommand(command='new_order', description="Оформить заказ (НЕ РАБОТАЕТ)"),
    BotCommand(command='ordering_guide', description="Мануал по оформлению заказа"),
    BotCommand(command='calculate_price', description="Расчитать стоимость заказа"),
    BotCommand(command='reviews', description="Отзывы наших покупателей"),
    # BotCommand(оcommand='order_status', description="Узнать статус заказа"),
    BotCommand(command='contact_support', description="Связаться с поддержкой")
]


async def main(bot: Bot, dp: Dispatcher) -> None:

    logger.info("Setup commands...")
    await bot.set_my_commands(commands, BotCommandScopeDefault())

    logger.info("Configure handlers & routers...")
    setup_user_routers(dp)

    logger.info("Configure webhook...")
    await bot.delete_webhook(drop_pending_updates=True)

    logger.info("Start bot")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main(bot, dp))
