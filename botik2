import time
import logging

from aiogram import Bot, Dispatcher, executor, types # из айограма нужные библиотеки
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery,Message,InlineKeyboardButton,InlineKeyboardMarkup
import asyncio
TOKEN = "6296077569:AAGFXEBgyWlbaTIUNQ0lU2ZTpfa-ZHFKnw0"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
k=int(0)

mainWindow=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text="выход",callback_data='1'),
    InlineKeyboardButton(text="Обучится обязаностям", callback_data='2'),
    InlineKeyboardButton(text="информация о компании", callback_data='3'),
    InlineKeyboardButton(text="ознакомится с офисом и сотрудникам",callback_data='4'),
)
@dp.callback_query_handler(lambda c: c.data=='1')
async def callback(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=escape,
        text='досвиданья'

    )
escape=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='в главное меню',callback_data='5')
    )
@dp.callback_query_handler(lambda c: c.data=='5')
async def callback(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=mainWindow,
        text='привет'
    )

@dp.callback_query_handler(lambda c: c.data == '2')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=studing,
        text='хорошо вот'

    )
studing=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1тест', callback_data='a1'),
    InlineKeyboardButton(text='2тест', callback_data='b1'),
    InlineKeyboardButton(text='ссылка', callback_data='c1'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
    )

if Text(equals='1вар'):
    k += 1
@dp.callback_query_handler(lambda c: c.data == 'a1')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question1,
        text='вопрос1'
    )
question1=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1вар', callback_data='z'),
    InlineKeyboardButton(text='2вар', callback_data='x'),
    InlineKeyboardButton(text='3вар', callback_data='x'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)

if Text(equals='1вар'):
    k += 1
@dp.callback_query_handler(lambda c: c.data == 'z' or c.data == 'x')
async def callback(message: Message, ):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question2,
        text='вопрос2'
    )
question2=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1вар', callback_data='z1'),
    InlineKeyboardButton(text='2вар', callback_data='x1'),
    InlineKeyboardButton(text='3вар', callback_data='x1'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c:  c.data == 'z1' or c.data == 'x1')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question3,
        text='вопрос3'
    )

question3=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1вар', callback_data='z2'),
    InlineKeyboardButton(text='2вар', callback_data='x2'),
    InlineKeyboardButton(text='3вар', callback_data='x2'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c:  c.data == 'z2' or c.data == 'x2')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question4,
        text='вопрос4'
    )

question4=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1вар', callback_data='z3'),
    InlineKeyboardButton(text='2вар', callback_data='x3'),
    InlineKeyboardButton(text='3вар', callback_data='x3'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c:  c.data == 'z3' or c.data == 'x3')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question5,
        text='вопрос5'
    )

question5=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1вар', callback_data='z4'),
    InlineKeyboardButton(text='2вар', callback_data='x4'),
    InlineKeyboardButton(text='3вар', callback_data='x4'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c:  c.data == 'z4' or c.data == 'x4')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question6,
        text='вопрос6'
    )

question6=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1вар', callback_data='z5'),
    InlineKeyboardButton(text='2вар', callback_data='x5'),
    InlineKeyboardButton(text='3вар', callback_data='x5'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c:  c.data == 'z5' or c.data == 'x5')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question7,
        text='вопрос7'
    )

question7=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1вар', callback_data='z6'),
    InlineKeyboardButton(text='2вар', callback_data='x6'),
    InlineKeyboardButton(text='3вар', callback_data='x6'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c: c.data ==   'z6' or c.data == 'x6')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question8,
        text='вопрос8'
    )

question8=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1вар', callback_data='z7'),
    InlineKeyboardButton(text='2вар', callback_data='x7'),
    InlineKeyboardButton(text='3вар', callback_data='x7'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c:  c.data == 'z7' or c.data == 'x7')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question9,
        text='вопрос9'
    )

question9=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1вар', callback_data='z8'),
    InlineKeyboardButton(text='2вар', callback_data='x8'),
    InlineKeyboardButton(text='3вар', callback_data='x8'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c: c.data == 'z8' or c.data == 'x8')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question10,
        text='вопрос10'
    )

question10=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1вар', callback_data='z9'),
    InlineKeyboardButton(text='2вар', callback_data='x9'),
    InlineKeyboardButton(text='3вар', callback_data='x9'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c:  c.data == 'z9' or c.data == 'x9')

async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=final,
        text=f"вы набрали {k} баллов"
    )

final=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='пройти снова', callback_data='a1'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
)


@dp.message_handler(commands=['start'])
async def callback_start(message:Message):
    await bot.send_message(
        chat_id=message.chat.id,
        reply_markup=mainWindow,
        text='привет'
    )


if __name__=='__main__':
    executor.start_polling(dp)
