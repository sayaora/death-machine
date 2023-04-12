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


mainWindow = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="Обучиться обязаностям", callback_data='2'),
    InlineKeyboardButton(text="Информация об агенстве", callback_data='3'),
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
    await bot.send_photo(
        chat_id = message.from_user.id,
        photo = open("images\\learn_page.png", 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=studing,
        text='Обучиться обязаностям'
    )

@dp.callback_query_handler(lambda c: c.data == '3')  # информация
async def callback(message: Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=open(f'images\\info\\main_info.png', 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=information,
        text='Информация об агенстве'
    )

@dp.callback_query_handler(lambda c: c.data == '4')  # офис
async def callback(message: types.Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=open(f'images\\office.png', 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=office,
        text='Офис и сотрудники'
    )

# @dp.callback_query_handler(lambda c: c.data == '4')  # вывод картинки
# async def callback(message: types.Message):
#     await bot.send_photo(
#         chat_id=message.from_user.id,
#         reply_markup=mainWindow,
#         photo=open('kartinka.png', 'rb')
#     )


escape = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Главное меню', callback_data='5')
)


@dp.callback_query_handler(lambda c: c.data == '5') # главное меню
async def callback(message: Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=open('images\\agency_main.png', 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=mainWindow,
        text='Главное меню'
    )


studing = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Тест на знание сотрудников', callback_data='a1'),
    InlineKeyboardButton(text='Тест на знание агенства', callback_data='b1'),
    InlineKeyboardButton(text='Доп образование', callback_data='c1'),
    InlineKeyboardButton(text='Глaвное меню', callback_data='5')
)

counter = 0
counter_true = 0

global questions
questions = []

quest_ind = 0


# async def increase_q(pre_counter):
#     global quest_ind
#     if(pre_counter == 4):
#         quest_ind -= 3
#         quest_ind += 7
#         return quest_ind - 7 + 4
#     else:
#         quest_ind += 1
#         return quest_ind


# print(questions)


@dp.callback_query_handler(lambda c: c.data == 'a1')
async def callback(message: Message):
    global counter
    global counter_true
    global questions
    global quest_ind

    counter = 0
    quest_ind = 0
    counter_true = 0
    questions = []
    with open("text\qwest_1.txt", encoding="utf-8") as r:
        for i in r:
            questions.append(i.split('\n')[0])
        r.close()

    await bot.send_photo(
                chat_id=message.from_user.id,
                photo=open(f'images\\test_1\\t1_{counter}.png', 'rb')
            )
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup = InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(text=f"{questions[quest_ind + 1]}", callback_data=f't1'),
            InlineKeyboardButton(text=f"{questions[quest_ind + 2]}", callback_data=f't2'),
            InlineKeyboardButton(text=f"{questions[quest_ind + 3]}", callback_data=f't3'),
            InlineKeyboardButton(text=f"{questions[quest_ind + 4]}", callback_data=f't4'),
            InlineKeyboardButton(text='Вернуться назад', callback_data='2')
        ),
        text=f"{questions[quest_ind]}"
    )

@dp.callback_query_handler(lambda c: c.data == 'b1')
async def callback(message: Message):
    global counter
    global counter_true
    global questions
    global quest_ind

    counter = 0
    quest_ind = 0
    counter_true = 0
    questions = []
    with open("text\qwest_2.txt", encoding="utf-8") as r:
        for i in r:
            questions.append(i.split('\n')[0])
        r.close()
    

    await bot.send_photo(
                chat_id=message.from_user.id,
                photo=open(f'images\\test_2\\t2_{counter}.png', 'rb')
            )
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup = InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(text=questions[quest_ind + 1], callback_data=f't1'),
            InlineKeyboardButton(text=questions[quest_ind + 2], callback_data=f't2'),
            InlineKeyboardButton(text=questions[quest_ind + 3], callback_data=f't3'),
            InlineKeyboardButton(text=questions[quest_ind + 4], callback_data=f't4'),
            InlineKeyboardButton(text='Вернуться назад', callback_data='2')
        ),
        text=f"{questions[quest_ind]}"
    )
    


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('t'))
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    global counter
    global counter_true
    global questions
    global quest_ind

    if (callback.data == f't{questions[quest_ind + 5]}'):
        counter_true += 1

    quest_ind += 7
    counter += 1

    if (quest_ind < len(questions)):
        await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=open(f'images\\test_1\\t1_{counter}.png', 'rb')
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            reply_markup = InlineKeyboardMarkup(row_width=1).add(
                InlineKeyboardButton(text=f"{questions[quest_ind + 1]}", callback_data=f't1'),
                InlineKeyboardButton(text=f"{questions[quest_ind + 2]}", callback_data=f't2'),
                InlineKeyboardButton(text=f"{questions[quest_ind + 3]}", callback_data=f't3'),
                InlineKeyboardButton(text=f"{questions[quest_ind + 4]}", callback_data=f't4'),
                InlineKeyboardButton(text='Вернуться назад', callback_data='2')
            ),
            text=f"{questions[quest_ind]}"
        )
    else:
        if(counter_true < 7):
            await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=open(f'images\\defeat.png', 'rb')
            )
        elif(counter_true >= 7 and counter_true <= 9):
            await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=open(f'images\\normal_bal.png', 'rb')
            )
        elif(counter_true == 10):
            await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=open(f'images\\win.png', 'rb')
            )
        
        if (counter_true > 1 and counter_true <= 4):
            await bot.send_message(
                chat_id=callback.from_user.id,
                reply_markup=final,
                text=f"Вы набрали {counter_true} балла"
            )
        elif (counter_true == 1):
            await bot.send_message(
                chat_id=callback.from_user.id,
                reply_markup=final,
                text="Вы набрали 1 балл"
            )
        elif (counter_true == 0 or counter_true > 4):
            await bot.send_message(
                chat_id=callback.from_user.id,
                reply_markup=final,
                text=f"Вы набрали {counter_true} баллов"
            )
    

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('t'))
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    global counter
    global counter_true
    global questions
    global quest_ind

    if (callback.data == f't{questions[quest_ind + 5]}'):
        counter_true += 1

    quest_ind += 7
    counter += 1

    if (quest_ind < len(questions)):
        await bot.send_photo(
                chat_id=callback.from_user.id,
                photo=open(f'images\\test_2\\t2_{counter}.png', 'rb')
            )
        await bot.send_message(
            chat_id=callback.from_user.id,
            reply_markup = InlineKeyboardMarkup(row_width=1).add(
                InlineKeyboardButton(text=questions[quest_ind + 1], callback_data=f't1'),
                InlineKeyboardButton(text=questions[quest_ind + 2], callback_data=f't2'),
                InlineKeyboardButton(text=questions[quest_ind + 3], callback_data=f't3'),
                InlineKeyboardButton(text=questions[quest_ind + 4], callback_data=f't4'),
                InlineKeyboardButton(text='Вернуться назад', callback_data='2')
            ),
            text=f"{questions[quest_ind]}"
        )
    else:
        if(counter_true < 7):
            await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=open(f'images\\defeat.png', 'rb')
            )
        elif(counter_true >= 7 and counter_true <= 9):
            await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=open(f'images\\normal_bal.png', 'rb')
            )
        elif(counter_true == 10):
            await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=open(f'images\\win.png', 'rb')
            )

        if (counter_true > 1 and counter_true <= 4):
            await bot.send_message(
                chat_id=callback.from_user.id,
                reply_markup=final,
                text=f"Вы набрали {counter_true} балла"
            )
        elif (counter_true == 1):
            await bot.send_message(
                chat_id=callback.from_user.id,
                reply_markup=final,
                text="Вы набрали 1 балл"
            )
        elif (counter_true == 0 or counter_true > 4):
            await bot.send_message(
                chat_id=callback.from_user.id,
                reply_markup=final,
                text=f"Вы набрали {counter_true} баллов"
            )

# question_1 = InlineKeyboardMarkup(row_width=1).add(
#         InlineKeyboardButton(text=f"{questions_1[quest_ind + 1]}", callback_data=f't1'),
#         InlineKeyboardButton(text=f"{questions_1[quest_ind + 2]}", callback_data=f't2'),
#         InlineKeyboardButton(text=f"{questions_1[quest_ind + 3]}", callback_data=f't3'),
#         InlineKeyboardButton(text=f"{questions_1[quest_ind + 4]}", callback_data=f't4'),
#         InlineKeyboardButton(text='Главное меню', callback_data='5')
#     )

# question_2 = InlineKeyboardMarkup(row_width=1).add(
#     InlineKeyboardButton(text=questions_2[quest_ind + 1], callback_data=f't1'),
#     InlineKeyboardButton(text=questions_2[quest_ind + 2], callback_data=f't2'),
#     InlineKeyboardButton(text=questions_2[quest_ind + 3], callback_data=f't3'),
#     InlineKeyboardButton(text=questions_2[quest_ind + 4], callback_data=f't4'),
#     InlineKeyboardButton(text='Главное меню', callback_data='5')
# )

final = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Пройти снова', callback_data='a1'),
    InlineKeyboardButton(text='Главное меню', callback_data='5')
)


@dp.callback_query_handler(lambda c: c.data=='c1')
async def with_hidden_link(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(f"{fmt.hide_link('https://stepik.org/catalog?utm_campaign=catalog_2022_04_08&utm_medium=stepik_courses&utm_source=stepik_landing_welcome_new')}"
        f"Предлагаем пройти курсы повышения квалификации на платформе Stepik"),
        parse_mode=types.ParseMode.HTML,
        reply_markup = studing
    )

# конец обучиться обязоностям


information = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Основная информация',callback_data='a2'),
    InlineKeyboardButton('Чем занимаемся',callback_data='b2'),
    InlineKeyboardButton('Продуктовая линейка',callback_data='c2'),
    InlineKeyboardButton('Главное меню',callback_data='5')
)

@dp.callback_query_handler(lambda c: c.data=='a2') # Основная информация
async def callback(message:Message):
    text_inormation = ""
    with open("text\\information.txt", encoding="utf-8") as r:
        for i in r:
            text_inormation += i

    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=open(f'images\\info\\agency_history.png', 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"{text_inormation}\n",
        reply_markup = information,
    )
    
    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     reply_markup = information,
    #     text='Информация об агенстве'
    # )

@dp.callback_query_handler(lambda c:c.data=='b2') # Чем занимаемся
async def callback(message:Message):
    text_inormation = ""
    with open("text\\affair.txt", encoding="utf-8") as r:
        for i in r:
            text_inormation += i
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=open(f'images\\info\\core_buisness.png', 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=information,
        text=f'{text_inormation}'
    )
    
@dp.callback_query_handler(lambda c: c.data == 'c2')  # Продуктовая линейка
async def callback(message: Message):
    text_inormation = ""
    with open("text\\product_line.txt", encoding="utf-8") as r:
        for i in r:
            text_inormation += i
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=open(f'images\\info\\product_line.png', 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=productnext,
        text=f'что то о рекламе'
    )
productnext=InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('создание сайтов',callback_data='ca2'),
    InlineKeyboardButton('вернутся в основную вкладку',callback_data='cd2')
)
productnext2=InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Поддержка сайтов',callback_data='cb2'),
    InlineKeyboardButton('вернутся в основую вкладку',callback_data='cd2')
)
finishview=InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('вернутся в основную вкладку',callback_data='cd2'),
    InlineKeyboardButton('в главное меню',callback_data='5'),
)

@dp.callback_query_handler(lambda c: c.data=='ca2')
async def callback(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=productnext2,
        text='что то там  о создании сайтов'
    )

@dp.callback_query_handler(lambda c: c.data=='cb2')
async def callback(message:Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=finishview,
        text='что то там  о поддержке сайтов'
    )

# конец информация об агенстве

office = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Сотрудники', callback_data='a3'),
    InlineKeyboardButton(text='Рассписание', callback_data='b3'),
    InlineKeyboardButton(text='План офиса', callback_data='c3'),
    InlineKeyboardButton(text='Техподдержка', callback_data='d3'),
    InlineKeyboardButton(text='Главное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c: c.data == 'a3')
async def callback(message: Message):
    office_text = []
    with open("text\office.txt", encoding="utf-8") as r:
        for i in r:
            office_text.append(i.split('\n')[0])
    for i in range(len(office_text)):
        if(i % 2 == 0 and not i == 0):
            await asyncio.sleep(3)

        if(i != 0 and i % 2 == 0):
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=open(f'images\office\office_{i//2}.png', 'rb')
            )
        elif(i == 0 and i % 2 == 0):
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=open(f'images\office\office_{0}.png', 'rb')
            )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"{office_text[i]}"
        )
    await bot.send_message(
            chat_id=message.from_user.id,
            reply_markup=office,
            text=f"Офис и сотрудники"
        )
    

@dp.callback_query_handler(lambda c: c.data == 'b3')
async def callback(message: Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=open('images\schedule.png', 'rb')
    )
    await bot.send_message(
            chat_id=message.from_user.id,
            reply_markup=office,
            text=f"Офис и сотрудники"
        )
    
@dp.callback_query_handler(lambda c: c.data == 'c3')
async def callback(message: Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=open('images\office\office_map.png', 'rb')
    )
    await bot.send_message(
            chat_id=message.from_user.id,
            reply_markup=office,
            text=f"Офис и сотрудники"
        )

@dp.callback_query_handler(lambda c: c.data == 'd3')
async def callback(message: Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=open('images\\support.png', 'rb')
    )
    await bot.send_message(
            chat_id=message.from_user.id,
            reply_markup=tehnical_support,
            text=f"К кому вы хотите обратиться?"
        )


tehnical_support = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Генеральный директор', callback_data='da3'), # @Kruglikeugen
    InlineKeyboardButton(text='Тим лидер', callback_data='db3'), # @V1olet_Demon
    InlineKeyboardButton(text='Старший Backend разработчик', callback_data='dc3'), # @sayaora
    InlineKeyboardButton(text='Главный бухгалтер', callback_data='dd3'), 
    InlineKeyboardButton(text='Главное меню', callback_data='5')
)

@dp.callback_query_handler(lambda c: c.data=='da3')
async def with_hidden_link(message:Message):
    await bot.send_photo(
        chat_id = message.from_user.id,
        photo = open("images\\tehnical_support\\kruglikeugen.png" , 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(f"Генеральный директор - @Kruglikeugen"),
        parse_mode=types.ParseMode.HTML,
        reply_markup = tehnical_support
    )

@dp.callback_query_handler(lambda c: c.data=='db3')
async def with_hidden_link(message:Message):
    await bot.send_photo(
        chat_id = message.from_user.id,
        photo = open("images\\tehnical_support\\V1olet_Demon.png" , 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(f"Тим лидер - @V1olet_Demon"),
        parse_mode=types.ParseMode.HTML,
        reply_markup = tehnical_support
    )

@dp.callback_query_handler(lambda c: c.data=='dc3')
async def with_hidden_link(message:Message):
    await bot.send_photo(
        chat_id = message.from_user.id,
        photo = open("images\\tehnical_support\\sayaora.png" , 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(f"Старший Backend разработчик - @sayaora"),
        parse_mode=types.ParseMode.HTML,
        reply_markup = tehnical_support
    )

@dp.callback_query_handler(lambda c: c.data=='dd3')
async def with_hidden_link(message:Message):
    await bot.send_photo(
        chat_id = message.from_user.id,
        photo = open("images\\tehnical_support\\IVIGllG.png" , 'rb')
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(f"Главный бухгалтер - @IVIGllG"),
        parse_mode=types.ParseMode.HTML,
        reply_markup = tehnical_support
    )



@dp.message_handler(commands=['start'])
async def callback_start(message: Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=open('images\\agency_main.png', 'rb')
    )
    await bot.send_message(
        chat_id=message.chat.id,
        reply_markup=mainWindow,
        text='Главное окно'
    )


if __name__ == '__main__':
    executor.start_polling(dp)
