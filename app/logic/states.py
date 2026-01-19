from aiogram.fsm.state import State, StatesGroup


class ProposePost(StatesGroup):
    waiting_for_post = State()
