from aiogram import F, Router, Dispatcher
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from setup import bot 
import utils.text as text
from keyboards.inline_keyboards import subscription_verification_keyboard
from keyboards.reply_keyboards import type_of_product, type_of_delivery, menu
from fsm.fsm import GetMessageFromUser
from utils.utils import DataForOrder
from filters import BasicFilter

  
from loguru import logger


router = Router(name="basic_user_router")
router.message.filter(
    BasicFilter('private', 'user')
)


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply(text.welcome.format(message.from_user.first_name), reply_markup=menu)
    invite_link = await bot.export_chat_invite_link(chat_id=-1002428126004)
    # await message.answer(text.subscription_verification['start'].format(invite_link), reply_markup=subscription_verification_keyboard)

# @router.callback_query(F.data == 'subscription_verification')
# async def subscription_verification(callback: CallbackQuery) -> None:
#     try:
#         subscription_status = await bot.get_chat_member(-1002428126004, callback.from_user.id)
#         if subscription_status.status == 'left': 
#             await callback.message.answer(text.subscription_verification['fail'], reply_markup=subscription_verification_keyboard)
#         else:
#             await callback.answer(reply_markup=menu)
#     except Exception as error:
#         await callback.answer(text.subscription_verification['error'], show_alert=True, reply_markup=menu)
#         logger.error(f"Cannot check subscription status, error: {error}")
#     finally:
#         await callback.answer(text.subscription_verification['error'], show_alert=True, reply_markup=menu)
