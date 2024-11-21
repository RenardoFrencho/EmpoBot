from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class GetMessageFromUser(StatesGroup):
    text = State()

class OrderData(StatesGroup):
    price = State()
    weight = State()
    delivery_type = State()
    
