import time
import logging
import json

from aiogram import Bot, Dispatcher, executor, types # из айограма нужные библиотеки
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
TOKEN = "6296077569:AAGFXEBgyWlbaTIUNQ0lU2ZTpfa-ZHFKnw0"

#storage = MemoryStorage

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

# class FMSAdmin(StatesGroup):
#     counter = 0
#     counter_true = 0


mainWindow=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text="выход",callback_data='1'),
    InlineKeyboardButton(text="Обучится обязаностям", callback_data='2'),
    InlineKeyboardButton(text="информация о компании", callback_data='3'),
    InlineKeyboardButton(text="ознакомится с офисом и сотрудникам",callback_data='4'),
)
@dp.callback_query_handler(lambda c: c.data=='1') #выход
async def callback(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=escape,
        text='досвиданья'

    )

@dp.callback_query_handler(lambda c: c.data == '2') #тест
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=studing,
        text='хорошо вот'

    )

@dp.callback_query_handler(lambda c: c.data == '4') #вывод картинки
async def callback(message: types.Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        reply_markup=mainWindow,
        photo=open('kartinka.png', 'rb')
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


studing=InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='1тест', callback_data='a1'),
    InlineKeyboardButton(text='2тест', callback_data='b1'),
    InlineKeyboardButton(text='ссылка', callback_data='c1'),
    InlineKeyboardButton(text='в глaавное меню', callback_data='5')
    )



counter = 1
counter_true = 0

#print(questions)


@dp.callback_query_handler(lambda c: c.data == 'a1')
async def callback(message: Message):
        global counter
        await bot.send_message(
            chat_id=message.from_user.id,
            reply_markup=question,
            text=f'вопрос {counter}'
        )

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('t'))
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    global counter
    global counter_true
    if(callback.data == 't1'):
        counter += 1
        counter_true += 1
    elif(callback.data == 't2'):
        counter += 1
    print(counter)
    await bot.send_message(
        chat_id=user_id,
        reply_markup=question,
        text=f"Вопрос {counter}"
    )
        
    print("Не работает")

question=InlineKeyboardMarkup().row(
        InlineKeyboardButton(text='1вар', callback_data=f't1'),
        InlineKeyboardButton(text='2вар', callback_data=f't2'),
        InlineKeyboardButton(text='3вар', callback_data=f't2'),
        InlineKeyboardButton(text='в глaавное меню', callback_data='5')
    )


# @dp.callback_query_handler(lambda c: c == 't1')
# async def increase(message: Message):
#     #await message.reply(FMSAdmin.states.count)
#     await bot.send_message(
#         chat_id=message.from_user.id,
#         reply_markup=question,
#         text=f"вопрос {FMSAdmin.states.count}"
#     )

#@dp.message_handler()
#async def increase(message: Message):
    #print(message.)
    #if message.values == 't1':
    #   count_ind += 1

# @dp.callback_query_handler(lambda c: c.data == 't2' or c.data == 't3')
# async def callback(message: Message, ):
#     await bot.send_message(
#         chat_id=message.from_user.id,
#         reply_markup=question,
#         text=f"вопрос {FMSAdmin.states.count.__get__}"
#     )
#     FMSAdmin.states.count += 1


print(question.values.items)

@dp.callback_query_handler(lambda c:  c.data == 'c')
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
    global user_id
    user_id = message.from_user.id

    questions = []
    # for i in range(10):
    #     questions[i] = [0]*5
    #     for j in range(3):
    #         questions[i][j] = j + 1

    schet = 5
    with open("qwest_1.txt", encoding="utf-8") as r:
        for i in r:
            questions.append(i.split('\n')[0])
    max_schet = range(len(questions))
    for i in range(schet, schet + 5):
        print(questions[i])

    await bot.send_message(
        chat_id=message.chat.id,
        reply_markup=mainWindow,
        text='привет'
    )


if __name__=='__main__':
    executor.start_polling(dp)
