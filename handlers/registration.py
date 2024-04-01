from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from DB import bot_DB
import const
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    married = State()
    gender = State()
    favorite_color = State()
    nationality = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Send me ur Nickname, please!'
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Could u tell me about urself ?'
    )
    await RegistrationStates.next()


async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='How old r u ?\n'
             'Use only numeric answer\n'
             'Example: 27, 17, 18, 25, 57\n\n'
             'if u dont wanna reveal ur age, please send me - '
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    if message.text == "-":
        pass
    else:
        try:
            int(message.text)
        except ValueError:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="I told u send me ONLY numeric text\n\n"
                     "Registration FAILED ❌\n"
                     "Restart Process, please!"
            )
            await state.finish()
            return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="R u married ? (Yes/No)\n"
             "if u dont wanna reveal ur status, please send me - "
    )
    await RegistrationStates.next()


async def load_married(message: types.Message,
                       state: FSMContext):
    async with state.proxy() as data:
        data['married'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Share with me ur gender?\n'
             'if u dont wanna reveal ur gender, please send me - '
    )
    await RegistrationStates.next()


async def load_gender(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur favorite color, please!'
    )
    await RegistrationStates.next()


async def load_color(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['favorite_color'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur nationality, please!'
    )
    await RegistrationStates.next()


async def load_nationality(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['nationality'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur photo, please!'
    )
    await RegistrationStates.next()


async def load_photo(message: types.Message,
                     state: FSMContext):
    db = bot_DB.Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )
    print(message.photo)
    async with state.proxy() as data:
        db.insert_profile(
            tg_id=message.from_user.id,
            nickname=data['nickname'],
            bio=data['bio'],
            age=data['age'],
            married=data['married'],
            gender=data['gender'],
            favorite_color=data['favorite_color'],
            nationality=['nationality'],
            photo=path.name
        )

        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    bio=data['bio'],
                    age=data['age'],
                    married=data['married'],
                    gender=data['gender'],
                    favorite_color=data['favorite_color'],
                    nationality=['nationality']
                )
            )
    await bot.send_message(
        chat_id=message.from_user.id,
        text='U have successfully Registered 🎉🍾\n'
             'Congrats Comrade!!!'
    )
    await state.finish()


def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_married,
        state=RegistrationStates.married,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_color,
        state=RegistrationStates.favorite_color,
        content_types=['text']
    )
    dp.register_message_handler(
        load_nationality,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
