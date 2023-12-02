from aiogram.dispatcher.filters.state import State, StatesGroup


class UserDate(StatesGroup):
    telefon_raqam = State()
    kasallik_turi = State()
    nechchinchi_tur = State()
    yosh = State()
    yil = State()
    insulin = State()
    vazn = State()
    buy = State()
    
    yosh_3 = State()
    memory = State()
    vazn_ = State()
    buy_ = State()
    where = State()

    age = State()
    vazn_1 = State()
    buyi = State()
    where_1 = State()