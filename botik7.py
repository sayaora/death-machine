import time
import logging
import json

from aiogram import Bot, Dispatcher, executor, types  # из айограма нужные библиотеки
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
import aiogram.utils.markdown as fmt
import asyncio

TOKEN = "6296077569:AAGFXEBgyWlbaTIUNQ0lU2ZTpfa-ZHFKnw0"

# storage = MemoryStorage

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

# class FMSAdmin(StatesGroup):
#     counter = 0
#     counter_true = 0


mainWindow = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="Обучиться обязаностям", callback_data='2'),
    InlineKeyboardButton(text="Информация о компании", callback_data='3'),
    InlineKeyboardButton(text="Ознакомиться с офисом и сотрудникам", callback_data='4'),
    InlineKeyboardButton(text="Выход", callback_data='1')
)


@dp.callback_query_handler(lambda c: c.data == '1')  # выход
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=escape,
        text='Досвиданья'
    )


@dp.callback_query_handler(lambda c: c.data == '2')  # тест
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=studing,
        text='Обучиться обязаностям'
    )

@dp.callback_query_handler(lambda c: c.data == '3')  # информация
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=office,
        text='Офис и сотрудники'
    )

@dp.callback_query_handler(lambda c: c.data == '4')  # офис
async def callback(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=mainWindow,
        photo=open('images\kartinka.png', 'rb')
    )

# @dp.callback_query_handler(lambda c: c.data == '4')  # вывод картинки
# async def callback(message: types.Message):
#     await bot.send_photo(
#         chat_id=message.from_user.id,
#         reply_markup=mainWindow,
#         photo=open('kartinka.png', 'rb')
#     )


escape = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='Главное меню', callback_data='5')
)


@dp.callback_query_handler(lambda c: c.data == '5')
async def callback(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=mainWindow,
        text='Главное меню'
    )


studing = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='Тест на знание сотрудников', callback_data='a1'),
    InlineKeyboardButton(text='Тест на знание агенства', callback_data='b1'),
    InlineKeyboardButton(text='Доп образование', callback_data='c1'),
    InlineKeyboardButton(text='Глaавное меню', callback_data='5')
)

counter = 0
counter_true = 0

questions_1 = []
with open("text\qwest_1.txt", encoding="utf-8") as r:
    for i in r:
        questions_1.append(i.split('\n')[0])

questions_2 = []
with open("text\qwest_2.txt", encoding="utf-8") as r:
    for i in r:
        questions_2.append(i.split('\n')[0])

quest_ind = 0


# print(questions)


@dp.callback_query_handler(lambda c: c.data == 'a1')
async def callback(message: Message):
    global counter
    global counter_true
    global questions_1
    global quest_ind

    counter_true = 0
    questions_1 = []
    with open("text\qwest_1.txt", encoding="utf-8") as r:
        for i in r:
            questions_1.append(i.split('\n')[0])
    

    if (counter == 10):
        counter = 0
        quest_ind = 0

    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question_1,
        text=f"{questions_1[quest_ind]}"
    )

@dp.callback_query_handler(lambda c: c.data == 'b1')
async def callback(message: Message):
    global counter
    global counter_true
    global questions_2
    global quest_ind

    counter_true = 0
    questions = []
    with open("text\qwest_2.txt", encoding="utf-8") as r:
        for i in r:
            questions_2.append(i.split('\n')[0])
    

    if (counter == 10):
        counter = 0
        quest_ind = 0

    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=question_2,
        text=f"{questions_2[quest_ind]}"
    )


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('t'))
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    global counter
    global counter_true
    global questions_1
    global quest_ind

    if (callback.data == f't{questions_1[quest_ind + 5]}'):
        counter_true += 1

    quest_ind += 7
    counter += 1

    if (quest_ind < len(questions_1)):
        await bot.send_message(
            chat_id=user_id,
            reply_markup=question_1,
            text=f"{questions_1[quest_ind]}"
        )
    else:
        if (counter_true > 1 and counter_true <= 4):
            await bot.send_message(
                chat_id=user_id,
                reply_markup=final,
                text=f"Вы набрали {counter_true} балла"
            )
        elif (counter_true == 1):
            await bot.send_message(
                chat_id=user_id,
                reply_markup=final,
                text="Вы набрали 1 балл"
            )
        elif (counter_true == 0 or counter_true > 4):
            await bot.send_message(
                chat_id=user_id,
                reply_markup=final,
                text=f"Вы набрали {counter_true} баллов"
            )

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('t'))
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    global counter
    global counter_true
    global questions_2
    global quest_ind

    if (callback.data == f't{questions_2[quest_ind + 5]}'):
        counter_true += 1

    quest_ind += 7
    counter += 1

    if (quest_ind < len(questions_2)):
        await bot.send_message(
            chat_id=user_id,
            reply_markup=question_2,
            text=f"{questions_2[quest_ind]}"
        )
    else:
        if (counter_true > 1 and counter_true <= 4):
            await bot.send_message(
                chat_id=user_id,
                reply_markup=final,
                text=f"Вы набрали {counter_true} балла"
            )
        elif (counter_true == 1):
            await bot.send_message(
                chat_id=user_id,
                reply_markup=final,
                text="Вы набрали 1 балл"
            )
        elif (counter_true == 0 or counter_true > 4):
            await bot.send_message(
                chat_id=user_id,
                reply_markup=final,
                text=f"Вы набрали {counter_true} баллов"
            )


question_1 = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text=questions_1[quest_ind + 1], callback_data=f't1'),
    InlineKeyboardButton(text=questions_1[quest_ind + 2], callback_data=f't2'),
    InlineKeyboardButton(text=questions_1[quest_ind + 3], callback_data=f't3'),
    InlineKeyboardButton(text=questions_1[quest_ind + 4], callback_data=f't4'),
    InlineKeyboardButton(text='Главное меню', callback_data='5')
)
question_2 = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text=questions_2[quest_ind + 1], callback_data=f't1'),
    InlineKeyboardButton(text=questions_2[quest_ind + 2], callback_data=f't2'),
    InlineKeyboardButton(text=questions_2[quest_ind + 3], callback_data=f't3'),
    InlineKeyboardButton(text=questions_2[quest_ind + 4], callback_data=f't4'),
    InlineKeyboardButton(text='Главное меню', callback_data='5')
)

final = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='Пройти снова', callback_data='a1'),
    InlineKeyboardButton(text='Главное меню', callback_data='5')
)

office = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='Сотрудники', callback_data='a2'),
    InlineKeyboardButton(text='Рассписание', callback_data='b2'),
    InlineKeyboardButton(text='План офиса', callback_data='c2'),
    InlineKeyboardButton(text='Техподдержка', callback_data='d2'),
    InlineKeyboardButton(text='Главное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c: c.data == 'a2')
async def callback(message: Message):
    office_text = []
    with open("text\office.txt", encoding="utf-8") as r:
        for i in r:
            office_text.append(i.split('\n')[0])
    for i in range(len(office_text)):
        if(i % 2 == 0 and not i == 0):
            await asyncio.sleep(2.5)
        await bot.send_message(
            chat_id=user_id,
            text=f"{office_text[i]}"
        )
    await bot.send_message(
            chat_id=user_id,
            reply_markup=mainWindow,
            text=f"Главное окно"
        )
    

@dp.callback_query_handler(lambda c: c.data == 'b2')
async def callback(message: Message):
    await bot.send_photo(
        chat_id=user_id,
        photo=open('images\schedule.png', 'rb')
    )
    await bot.send_message(
            chat_id=user_id,
            reply_markup=office,
            text=f"Офис и сотрудники"
        )
    
@dp.callback_query_handler(lambda c: c.data == 'c2')
async def callback(message: Message):
    await bot.send_photo(
        chat_id=user_id,
        photo=open('images\office_map.png', 'rb')
    )
    await bot.send_message(
            chat_id=user_id,
            reply_markup=office,
            text=f"Офис и сотрудники"
        )

@dp.callback_query_handler(lambda c: c.data == 'd2')
async def callback(message: Message):
    await bot.send_message(
            chat_id=user_id,
            reply_markup=tehnical_support,
            text=f"К кому вы хотите обратиться?"
        )


tehnical_support = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='Генеральный директор', callback_data='da2'), # @Kruglikeugen
    InlineKeyboardButton(text='Тим лидер', callback_data='db2'), # @V1olet_Demon
    InlineKeyboardButton(text='Старший Backend разработчик', callback_data='dc2'), # @sayaora
    InlineKeyboardButton(text='Главный бухгалтер', callback_data='dd2'), 
    InlineKeyboardButton(text='Главное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c: c.data=='da2')
async def with_hidden_link(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(f"Генеральный директор - @Kruglikeugen"),
        parse_mode=types.ParseMode.HTML,
        reply_markup = tehnical_support
    )

@dp.callback_query_handler(lambda c: c.data=='db2')
async def with_hidden_link(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(f"Тим лидер - @V1olet_Demon"),
        parse_mode=types.ParseMode.HTML,
        reply_markup = tehnical_support
    )

@dp.callback_query_handler(lambda c: c.data=='dc2')
async def with_hidden_link(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(f"Старший Backend разработчик - @sayaora"),
        parse_mode=types.ParseMode.HTML,
        reply_markup = tehnical_support
    )

@dp.callback_query_handler(lambda c: c.data=='dd2')
async def with_hidden_link(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(f"Главный бухгалтер - @IVIGllG"),
        parse_mode=types.ParseMode.HTML,
        reply_markup = tehnical_support
    )



@dp.message_handler(commands=['start'])
async def callback_start(message: Message):
    global user_id
    user_id = message.from_user.id

    await bot.send_message(
        chat_id=message.chat.id,
        reply_markup=mainWindow,
        text='Главное окно'
    )


if __name__ == '__main__':
    executor.start_polling(dp)
