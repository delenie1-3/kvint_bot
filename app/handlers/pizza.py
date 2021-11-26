from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

#списки диалога
available_sizes = ["большую", "маленькую"]
available_payment = ["наличкой", "по карте"]

#класс состояний
class OrderPizza(StatesGroup):
    waiting_for_sizes = State()
    waiting_for_payment = State()

#функция начала диалога заказа пиццы (размер пиццы)
async def pizza_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in available_sizes:#выборка из списка диалога
        keyboard.add(size)
    await message.answer("Выберите размер пиццы:", reply_markup=keyboard)
    await OrderPizza.waiting_for_sizes.set()

#функция проверки ввода и выбора размера
async def pizza_chosen_size(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_sizes:#проверка на случай ввода с клавиатуры
        await message.answer("Пожалуйста, выберите размер пиццы (большую или маленькую), используя кнопки ниже.")
        return
    await state.update_data(chosen_size=message.text.lower())#установка состояния о размере

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for payment in available_payment:#выборка из списка диалога
        keyboard.add(payment)
    await OrderPizza.next()#ожидание и переход к следующему вопросу
    await message.answer("Теперь выберите способ оплаты:", reply_markup=keyboard)

#функция проверки ввода и выбора способа оплаты
async def pizza_payment_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_payment:#проверка на случай ввода с клавиатуры
        await message.answer("Пожалуйста, выберите способ оплаты (по карте или наличкой), используя кнопки ниже.")
        return
    await state.update_data(chosen_payment=message.text.lower())#установка состояния об оплате
    user_data = await state.get_data()
    await message.answer(f"Вы заказали {user_data['chosen_size']} пиццу, оплата {message.text.lower()}.\n",
                        reply_markup=types.ReplyKeyboardRemove())#вывод заказа
    await state.finish()

def register_handlers_pizza(dp: Dispatcher):#регистрация хендлеров диалога
    dp.register_message_handler(pizza_start, commands="pizza", state="*")
    dp.register_message_handler(pizza_chosen_size, state=OrderPizza.waiting_for_sizes)
    dp.register_message_handler(pizza_payment_chosen, state=OrderPizza.waiting_for_payment)