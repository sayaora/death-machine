import time
import logging

from aiogram import Bot, Dispatcher, executor, types # из айограма нужные библиотеки
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as fmt
from aiogram.types import CallbackQuery,Message,InlineKeyboardButton,InlineKeyboardMarkup
import asyncio
TOKEN = "6296077569:AAGFXEBgyWlbaTIUNQ0lU2ZTpfa-ZHFKnw0"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

privki=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text="выход",callback_data='1'),
    InlineKeyboardButton(text="Обучится обязаностям", callback_data='2'),
    InlineKeyboardButton(text="информация о компании", callback_data='3'),
    InlineKeyboardButton(text="ознакомится с офисом и сотрудникам",callback_data='4'),
)
@dp.callback_query_handler(lambda c: c.data=='1')
async def callback(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=viidi,
        text='досвиданья'

    )


@dp.callback_query_handler(lambda c: c.data == '2')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=neob,
        text='хорошо вот'

    )

viidi=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='жаль',callback_data='5')
    )

neob=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='нежаль',callback_data='6')
)

@dp.message_handler(commands=['start'])
async def callback_start(message:Message):
    await bot.send_message(
        chat_id=message.chat.id,
        reply_markup=privki,
        text='привет'
    )


if __name__=='__main__':
    executor.start_polling(dp)