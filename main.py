import logging
from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from config import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from state import *
storge = MemoryStorage()
bot =Bot(token=API_TOKEN)
dp=Dispatcher(bot, storage=storge)


logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Tilni tanlang", reply_markup=til)
    

@dp.message_handler(text="🇺🇿O'zbekcha")
async def exo(message: types.Message, state: FSMContext):
    await message.answer('Raqamingizni yuboring',reply_markup=contact)
    await UserDate.telefon_raqam.set()
    

@dp.message_handler(content_types='contact', state=UserDate.telefon_raqam)
async def exo(message: types.Message, state:FSMContext):
    phone_number = message.contact['phone_number']
    await state.update_data(telefon_raqam=phone_number)
    await message.answer('Sizni qaysi kasallik bezovta qilayapti', reply_markup=kasallik)
    await UserDate.kasallik_turi.set()

@dp.message_handler(text='Qandli diabet', state=UserDate.kasallik_turi)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(kasallik_turi = message.text)
    await message.answer('Sizda qandli diabetning nechanchi turi',reply_markup=qandli_tur)
    await UserDate.nechchinchi_tur.set()
    
@dp.message_handler(text='I tip', state=UserDate.nechchinchi_tur)
async def exo(message: types.Message, state=FSMContext):
    await state.update_data(nechchinchi_tur = message.text)
    await message.answer('Mumkin emas', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await state.reset_data()  

@dp.message_handler(text='II tip',state=UserDate.nechchinchi_tur)
async def exo(message: types.Message, state=FSMContext):
    await state.update_data(nechchinchi_tur = message.text)
    await message.answer('Yoshingiz nechida?')
    await UserDate.yosh.set()

@dp.message_handler(state=UserDate.yosh)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(yosh = message.text)
    await message.answer('Kasallikka necha yil bo\'ldi?') 
    await UserDate.yil.set()   

@dp.message_handler(state = UserDate.yil)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(yil = message.text)
    await message.answer('Insulin ukol boshlandimi?',reply_markup=insulin_choice)    
    await UserDate.insulin.set()   
    
@dp.message_handler(text = "Xa", state = UserDate.insulin)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(insulin = message.text)
    await message.answer('Vazningizni kiriting')    
    await UserDate.vazn.set()   

@dp.message_handler(text = "Yo'q", state=UserDate.insulin)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(insulin = message.text)
    await message.answer('Tez orada mutaxasis siz bilan bog\'lanadi!!!')
    data = await state.get_data()
    tel_n = data.get("telefon_raqam")
    ill = data.get("kasallik_turi")
    nech_ = data.get("nechchinchi_tur")
    yosh11 = data.get("yosh")
    year_ = data.get("yil")
    tanlaa = data.get("insulin")
    info_1 = f"""Telefon raqam: {tel_n}
Kasallik turi: {ill}
Bosqich: {nech_}
Yoshi: {yosh11}
Qachondan beri: {year_}
Insulin: {tanlaa}"""
    await bot.send_message(6102894311, info_1)
    await message.answer("Tez orada mutaxasis siz bilan bog'lanadi",reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await state.reset_data()    

@dp.message_handler(state = UserDate.vazn)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(vazn = message.text)
    await message.answer("Bo'yingizni kiriting")
    await UserDate.buy.set() 

@dp.message_handler(state = UserDate.buy)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(buy = message.text)
    data = await state.get_data()
    tel_ = data.get("telefon_raqam")
    k_tur = data.get("kasallik_turi")
    turi = data.get("nechchinchi_tur")
    age = data.get("yosh")
    year = data.get("yil")
    insul = data.get("insulin")
    vaz = data.get("vazn")
    buy = data.get("buy")
    info = f"""Telefon raqam: {tel_}
Kasallik turi: {k_tur}
Bosqich: {turi}
Yoshi: {age}
Qachondan beri: {year}
Insulin: {insul}
Vazni: {vaz}
Bo'yi: {buy}"""
    
    await bot.send_message(6102894311, info)
    await message.answer("Tez orada mutaxasis siz bilan bog'lanadi")
    await state.finish()
    await state.reset_data()

@dp.message_handler(text='Bilmayman🤷',state=UserDate.nechchinchi_tur)
async def exo(message: types.Message, state=FSMContext):
    await state.update_data(nechchinchi_tur = message.text)
    await message.answer('Yoshingiz nechida?', reply_markup=await yoshi__())
    await UserDate.yosh_3.set()

@dp.message_handler(text='1 dan 25 yoshgacha',state=UserDate.yosh_3)
async def exo(message: types.Message, state=FSMContext):
    await state.update_data(yoshi_3 = message.text)
    await message.answer('Mumkin emas', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await state.reset_data()
    

   
@dp.message_handler(text='25 va undan yuqori',state=UserDate.yosh_3)
async def yoshi(message: types.Message, state=FSMContext):
    await state.update_data(yosh_3 = message.text)
    text = "Kasallik aniqlangan kundan boshlab insulinga o'tganmisiz"
    await message.answer(text, reply_markup=await info_())
    await UserDate.memory.set() 

@dp.message_handler(text='xa',state=UserDate.memory)
async def yoshi(message: types.Message, state=FSMContext):
    await state.update_data(memory = message.text)
    text = "Mumkin emas"
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await state.reset_data()

@dp.message_handler(text='yo\'q',state=UserDate.memory)
async def yoshi(message: types.Message, state=FSMContext):
    await state.update_data(memory = message.text)
    text = "Vazningiz qancha? "
    await message.answer(text)
    await UserDate.vazn_.set()

@dp.message_handler(state=UserDate.vazn_)
async def yoshi(message: types.Message, state=FSMContext):
    await state.update_data(vazn_ = message.text)
    text = "Bo'yingiz qancha? "
    await message.answer(text)
    await UserDate.buy_.set()

@dp.message_handler(state=UserDate.buy_)
async def yoshi(message: types.Message, state=FSMContext):
    await state.update_data(buy_ = message.text)
    text = "Qayerdansiz"
    await message.answer(text)
    await UserDate.where.set()

@dp.message_handler(state=UserDate.where)
async def yoshi(message: types.Message, state=FSMContext):
    await state.update_data(where = message.text)
    data = await state.get_data()
    nech_tur = data.get("nechchinchi_tur")
    yosh_nech = data.get("yosh_3")
    xa_yoq = data.get("memory")
    vazn__ = data.get("vazn_")
    hight = data.get("buy_")
    qayer = data.get("where")
    info_1 = f"""Turi: {nech_tur}
Yoshi: {yosh_nech}
Insulin: {xa_yoq}
Vazni: {vazn__}
Bo'yi: {hight}
Qayerda: {qayer}
"""
    await bot.send_message(6102894311, info_1)
    await message.answer("Tez orada mutaxasis siz bilan bog'lanadi")
    await state.finish()
    await state.reset_data()
    
@dp.message_handler(text='Semizlik', state=UserDate.kasallik_turi)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(kasallik_turi = message.text)
    await message.answer('Yoshingizni kiriting...')
    await UserDate.age.set()

@dp.message_handler(state=UserDate.age)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(age = message.text)
    await message.answer('Vazningizni kiriting...')
    await UserDate.vazn_1.set()    

@dp.message_handler(state=UserDate.vazn_1)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(vazn_1 = message.text)
    await message.answer('Bo\'yingizni kiriting...')
    await UserDate.buyi.set() 

@dp.message_handler(state=UserDate.buyi)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(buyi = message.text)
    await message.answer('Manzilingizni kiriting...')
    await UserDate.where_1.set() 

@dp.message_handler(state=UserDate.where_1)
async def exo(message: types.Message, state = FSMContext):
    await state.update_data(where_1 = message.text)     
    data = await state.get_data()
    tur_3 = data.get("kasallik_turi")
    yosh = data.get("age")
    vazn_1 = data.get("vazn_1")
    buyi_3 = data.get("buyi")
    qayda = data.get("where_1")
    info_2 = f"""Turi: {tur_3}
Yoshi: {yosh}
Vazni: {vazn_1}
Bo'yi: {buyi_3}
Qayerlik: {qayda}
"""
    await bot.send_message(6102894311, info_2)
    await message.answer("Tez orada mutaxasiz siz bilan bog'lanadi", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await state.reset_data()
    
    








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)