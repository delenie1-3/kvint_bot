from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

async def cmd_start(message: types.Message, state: FSMContext):
    #функция начала диалога
    await state.finish()
    await message.answer(
        "Начало диалога для заказа пиццы (/pizza).",
        reply_markup=types.ReplyKeyboardRemove()
    )

async def cmd_cancel(message: types.Message, state: FSMContext):
    #функция отмены
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())

def register_handlers_common(dp: Dispatcher):#регистрация хендлеров начала и отмены
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")