import time
import logging

from aiogram import Bot, Dispatcher, executor, types # из айограма нужные библиотеки
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as fmt

TOKEN = "6296077569:AAGFXEBgyWlbaTIUNQ0lU2ZTpfa-ZHFKnw0"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start']) #реакция на команду
async def start_coma(message:types.Message):   # пришло сооьщение : тип сообщение (ну написали в общем да) (async=means асинхронно)

    usid = message.from_user.id
    keyboard=types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text='Выход')
    keyboard.add(button_1)
    """button_2="обучится обязаностям"
    keyboard.add(button_2)
    button_3="информация о компании"
    keyboard.add(button_3)
    button_4= "ознакомится с офисом и сотрудниками"
    keyboard.add(button_4)"""

    await message.answer("что вы хотите сделать ?",reply_markup=keyboard)


@dp.message_handler(Text(equals='Выход'))
async def vihod(message: types.Message):
    await message.reply("досвидания")

@dp.message_handler(Text(equals='ознакомится с офисом и сотрудниками'))
async def with_hidden_link(message: types.message):
    await message.answer(
        f"{fmt.hide_link('kartinka.png')}",parse_mode=types.ParseMode.HTML)


@dp.message_handler(Text(equals='обучится обязаностям'))
async def vihod(message: types.Message):
    await message.reply("выберете обязанность")

@dp.message_handler(Text(equals='информация о компании'))
async def vihod(message: types.Message):
    await message.reply("очень важная компания")

if __name__=='__main__':
    executor.start_polling(dp)
