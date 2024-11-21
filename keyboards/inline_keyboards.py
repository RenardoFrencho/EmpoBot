from typing import Tuple
from random import sample, choice

from aiogram.types import (
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove,
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from loguru import logger

from utils.text import subscription_verification


subscription_verification_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=subscription_verification['button'], callback_data="subscription_verification")]])
