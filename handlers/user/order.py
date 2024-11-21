from aiogram import F, Router, Dispatcher
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from setup import bot, CNY_PRICE
import utils.text as text
from keyboards.inline_keyboards import subscription_verification_keyboard
from keyboards.reply_keyboards import type_of_product, type_of_delivery, menu
from fsm.fsm import OrderData
from utils.utils import DataForOrder
from filters import BasicFilter, SubscriptionVerificationFilter
  
from loguru import logger


router = Router(name="order_user_router")
router.message.filter(
    BasicFilter('private', 'user'),
    SubscriptionVerificationFilter(bot)
)

@router.message(Command(commands=["cancel"]))
@router.message(F.text == "Отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=menu
    )

@router.message(Command('ordering_guide'))
@router.message(F.text == "Как оформить заказ?")
async def start(message: Message) -> None:
    await message.answer("В процессе создания статьи, пожалуйста подождите\\. \nА пока, вы можете посмотреть мануал в нашем основном канале \\(закрепленное сообщение\\)")

@router.message(Command('calculate_price'))
@router.message(F.text == "Расчитать стоимость заказа")
async def get_price(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        text.calculate_price[0], 
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(OrderData.price)

@router.message(OrderData.price)
async def get_weight(message: Message, state: FSMContext) -> None:
    await state.set_data({'price': int(message.text)})
    await message.answer(text.calculate_price[1].format(int(int(message.text) * CNY_PRICE + (600 if int(message.text) * 0.4 > 600 else int(message.text) * 0.4))), reply_markup=type_of_product)
    await state.set_state(OrderData.weight)

@router.message(lambda message : message.text in ["Одежда👔", "Кроссовки👟", "Аксессуары💍", "Другое🎩"])
async def get_delivery(message: Message, state: FSMContext) -> None:
    if message.text == "Одежда👔":
        await state.update_data(weight=0.4)
    elif message.text == "Кроссовки👟":
        await state.update_data(weight=1.5)
    elif message.text == "Аксессуары💍":
        await state.update_data(weight=0.2)
    else:
        await state.update_data(weight=1)
    
    await message.answer(text.calculate_price[2], reply_markup=type_of_delivery)
    await state.set_state(OrderData.delivery_type)
    

@router.message(OrderData.delivery_type)
async def get_delivery_type(message: Message, state: FSMContext) -> None:
    price = int(await state.get_value('price') * CNY_PRICE + (600 if int(await state.get_value('price')) * 0.4 > 600 else int(await state.get_value('price')) * 0.4))
    weight = await state.get_value('weight')
    product_type = await state.get_value('product_type')
    if product_type == 'clothes':
        delivery_price = weight * 1300 if message.text == "Авиа✈️ (9-14 дней)" else 600
    elif product_type == 'shoes':
        delivery_price = weight * 1300 if message.text == "Авиа✈️ (9-14 дней)" else 600
    elif product_type == 'accessories':
        delivery_price = weight * 1300 if message.text == "Авиа✈️ (9-14 дней)" else 600
    else:
        delivery_price = 1 * 1300 if message.text == "Авиа✈️ (9-14 дней)" else 600

    await message.answer(text.calculate_price[3].format(price + delivery_price, price, delivery_price), reply_markup=menu)
    await state.clear()

@router.message(Command('reviews'))
@router.message(F.text == "Отзывы")
async def ordering_guide(message: Message) -> None:
    await message.answer(text.reviews)

@router.message(Command('contact_support'))
@router.message(F.text == "Связаться с поддержкой")
async def ordering_guide(message: Message) -> None:
    await message.answer(text.contact_support)


