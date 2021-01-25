import logging
import sys
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import config
from sqliter import SQLiter
from sqliter import USER
from sqliter import PHONE
from sqliter import ALL
from face import Facebook

print(sys.platform)

API_TOKEN = config.TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# sql
db = SQLiter('db.db')
db_user = USER('db.db')
db_phone = PHONE('db.db')
db_all = ALL('db.db')

sg = Facebook('lastkey.txt')


@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if not db_user.subscriber_exist(message.from_user.id):
        db_user.add_subscriber(message.from_user.id, message.from_user.full_name, True)
    else:
        db_user.update_subscription(message.from_user.id, True)
    await message.answer('Ви підписалися на розсилку')

    # TODO:добавить всплывающее окно
    # bot.answer_callback_query(
    # callback_query_id=call.id, show_alert=False,
    #                         text=config.phone_number)


@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if not db_user.subscriber_exist(message.from_user.id):
        db_user.add_subscriber(message.from_user.id, message.from_user.full_name, False)
    else:
        db_user.update_subscription(message.from_user.id, False)
    await message.answer('Ви не підписані')
    # TODO:добавить всплывающее окно
    # bot.answer_callback_query(
    # callback_query_id=call.id, show_alert=False,
    #                         text=config.phone_number)


@dp.message_handler(commands=['start'], commands_prefix='!/')
async def send_welcome(message: types.Message):
    """ sti = open(config.sticker, 'rb')
     bot.send_sticker(message.chat.id, sti)"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    st = KeyboardButton('start')
    markup.add(st)
    if not db_user.subscriber_exist(message.from_user.id):
        db_user.add_subscriber(message.from_user.id, message.from_user.full_name, datetime.now(), True)
    else:
        db_user.update_subscription(message.from_user.id, True)
    # await message.answer('Ви підписалися на розсилку')
    # keyboard
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    item1 = KeyboardButton('Червоноград')
    item2 = KeyboardButton("Новояворівськ")
    markup.add(item1, item2)
    await message.answer(f'Добрий день, {message.from_user.first_name}, де Ви знаходитесь?',
                         parse_mode=types.ParseMode.MARKDOWN, reply_markup=markup)


@dp.message_handler(content_types=['text'])
async def process_photo_command(message: types.Message, request='yes'):
    if message.chat.type == 'private':
        if message.text == 'Новояворівськ':

            await bot.send_message(message.chat.id, '😊')  # TODO: сделать вслывающее окно - вы выбрали такой то город
            # photo = open(config.foto, 'rb')
            # await bot.send_photo(message.chat.id, photo, parse_mode=types.ParseMode.MARKDOWN)

        elif message.text == 'Червоноград':
            # keyboard
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            item1 = KeyboardButton("Контакти", request_contact=False)
            item2 = KeyboardButton("Більше тут")
            item3 = KeyboardButton("Акції 😊")
            item4 = KeyboardButton("База")
            item5 = KeyboardButton("Вибрати місто")
            item6 = KeyboardButton(text='Замовити дзвінок', request_contact=True)
            item7 = KeyboardButton('Замовити заміри', request_contact=False)
            # item5 = types.KeyboardButton("Залишити геолокацію", request_location=True)
            markup.add(item1, item2, item3)
            markup.add(item6, item7)
            markup.row(item5)

            if message.chat.id in config.admin_all:
                markup.row(item4)

            # TODO: возможно приветствие вывести в сплывающее окно?
            await message.answer(config.hello_text(message.from_user.first_name), parse_mode=types.ParseMode.MARKDOWN,
                                 reply_markup=markup)

        elif message.text == 'Контакти':
            photo = open(config.foto, 'rb')
            await bot.send_photo(message.chat.id, photo, parse_mode=types.ParseMode.MARKDOWN)

        elif message.text == "Акції 😊":
            markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
            item1 = InlineKeyboardButton("Двері вхідні", callback_data='action1')
            item2 = InlineKeyboardButton("Двері міжкімнатні", callback_data='action2')
            item3 = InlineKeyboardButton("Ламінат", callback_data='action3')
            item4 = InlineKeyboardButton("Жалюзі", callback_data='action4')
            markup.add(item1, item2, item3, item4)
            await bot.send_message(message.chat.id, '😊', reply_markup=markup)

        elif message.text == "Більше тут":
            #   bot.send_message(message.chat.id, 'https://www.facebook.com/watch/?v=653010194852467')
            markup = types.InlineKeyboardMarkup(row_width=1)
            item = types.InlineKeyboardButton(text="натисни мене", url=config.URL)
            markup.add(item)
            await bot.send_message(message.chat.id, '😊', reply_markup=markup)

        elif message.text == 'Вибрати місто':
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            item1 = KeyboardButton('Червоноград')
            item2 = KeyboardButton("Новояворівськ")
            markup.add(item1, item2)
            await message.answer(f'Добрий день, {message.from_user.first_name}, де Ви знаходитесь?',
                                 parse_mode=types.ParseMode.MARKDOWN, reply_markup=markup)

        elif message.text == "Замовити заміри":
            markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
            item1 = InlineKeyboardButton("Двері вхідні", callback_data='act1')
            item2 = InlineKeyboardButton("Двері міжкімнатні", callback_data='act2')
            item3 = InlineKeyboardButton("Вікна", callback_data='act3')
            item4 = InlineKeyboardButton("Жалюзі", callback_data='act4')
            markup.add(item1, item2, item3, item4)
            await bot.send_message(message.chat.id, 'Що бажаєте замовити?', reply_markup=markup)


        elif message.text == 'База':
            try:
                for admins in config.admin_all:
                    await bot.send_message(admins, db.send_recording())
            except TypeError:
                print("Пустое значение")
            print(db.send_callback_all())  # TODO remove
        else:
            await bot.send_message(message.from_user.id, 'Викорустовуйте, будь-ласка, меню')
            db.add_text(message.from_user.id, message.text)


# save phone number in db.db'sub'
@dp.message_handler(content_types=["contact"])
async def tel_number(message):
    db_phone.add_phone_number(message.contact['phone_number'], message.contact['first_name'],
                              message.contact['last_name'], message.contact['user_id'])
    db_all.merged()
    try:
        answer = "Ім'я: {} {},\nНомер телефону: {}" \
            .format(message.contact['first_name'], message.contact['last_name'], message.contact['phone_number'])

        for admins in config.admin_all:
            await bot.send_message(admins, answer)

    except TypeError:
        print("Пустое значение")
    print(db.send_callback_all())  # TODO remove

    await bot.send_message(message.chat.id, 'Очікуйте дзвінок')


@dp.callback_query_handler(lambda call: True)
async def callback_inline(call):
    try:
        if call.message:
            if call.data == 'action1':
                await bot.send_message(call.message.chat.id, 'готуємо сюрприз 😊')
                await bot.send_message(call.message.chat.id, '😊')
                # photo_vhidni = open(config.foto, 'rb')
                # bot.send_photo(call.message.chat.id, photo)
            elif call.data == 'action2':
                # bot.send_message(call.message.chat.id, 'описание акции2')
                photo_interior_doors = open(config.foto_special_offer_interior_doors, 'rb')
                await bot.send_photo(call.message.chat.id, photo_interior_doors)
            elif call.data == 'action3':
                await bot.send_message(call.message.chat.id, 'готуємо сюрприз 😊')
                await bot.send_message(call.message.chat.id, '😊')
            elif call.data == 'action4':
                # bot.send_message(call.message.chat.id, 'описание акции4')
                photo_blinds_promotion = open(config.foto_blinds_promotion, 'rb')
                await bot.send_photo(call.message.chat.id, photo_blinds_promotion)

            # ACT1-4
            if call.data == 'act1':
                db.add_callback(call.message.chat.id, call.message.chat.full_name, config.items_list[0], datetime.now())

                # message for admins
                for admins in config.admin_all:
                    await bot.send_message(admins, 'Нове замовлення!')
                for admins in config.admin_all:
                    await bot.send_message(admins, db.send_recording())
                # message for all
                await bot.send_message(call.message.chat.id, 'Очікуйте дзвінок')


            elif call.data == 'act2':
                db.add_callback(call.message.chat.id, call.message.chat.full_name, config.items_list[1],
                                datetime.now())
                for admins in config.admin_all:
                    await bot.send_message(admins, 'Нове замовлення!')

                for admins in config.admin_all:
                    await bot.send_message(admins, db.send_recording())
                await bot.send_message(call.message.chat.id, 'Очікуйте дзвінок')

            elif call.data == 'act3':
                db.add_callback(call.message.chat.id, call.message.chat.full_name, config.items_list[2], datetime.now())
                for admins in config.admin_all:
                    await bot.send_message(admins, 'Нове замовлення!')

                for admins in config.admin_all:
                    await bot.send_message(admins, db.send_recording())
                await bot.send_message(call.message.chat.id, 'Очікуйте дзвінок')


            elif call.data == 'act4':
                db.add_callback(call.message.chat.id, call.message.chat.full_name, config.items_list[3], datetime.now())
                for admins in config.admin_all:
                    await bot.send_message(admins, 'Нове замовлення!')

                for admins in config.admin_all:
                    await bot.send_message(admins, db.send_recording())

                await bot.send_message(call.message.chat.id, 'Очікуйте дзвінок')
            else:
                pass

    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    # dp.loop.create_task(scheduled(10))  # 10 секунд
    executor.start_polling(dp, skip_updates=True)
