from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton( text="Как оформить заказ?" ),
        KeyboardButton( text="Расчитать стоимость заказа" )
    ],
    [
        KeyboardButton( text="Отзывы" ),
        KeyboardButton( text="Связаться с поддержкой")
    ]],
    resize_keyboard=True
)


type_of_product = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton( text="Одежда👔" ),
    KeyboardButton( text="Кроссовки👟" )],
    [KeyboardButton( text="Аксессуары💍" ),
     KeyboardButton( text="Другое🎩")],
    [KeyboardButton( text="Отмена" )]
    ],
    resize_keyboard=True
)

type_of_delivery = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton( text="Авиа✈️ (9-14 дней)" ),
    KeyboardButton( text="Авто🚚 (17-25 дней)" )],
    [KeyboardButton( text="Отмена" )]
    ],
    resize_keyboard=True
)
