from aiogram.dispatcher.filters.state import StatesGroup, State


class USER(StatesGroup):
    payment = State()
    phone_number = State()
