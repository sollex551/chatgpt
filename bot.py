import openai
from aiogram import Dispatcher, executor, Bot
from aiogram.types import Message

openai.api_key = 'Your-openai-TOKEN'

TOKEN = 'YOUR_TELEGRAM_BOT'

bot = Bot(TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def check_subscription(message: Message):
    full_name = message.from_user.full_name

    await bot.send_message(message.from_user.id,
                           f'Здравствуйте {full_name}\nВас приветствует  Чат гпт-бот. Подпишись на @AllApkaa ')


@dp.message_handler(commands=['help'])
async def command_start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f'Обратитесь в тех поддержку для помощи  (@CHAT_GPTADMIN)')


@dp.message_handler(content_types=['text'])
async def handle_message(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'пожалуйста подпишись на мой канал @AllApkaa')

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    await message.answer(
        f'*Ответ на вопрос*    : `{response.choices[0].text}` \n\n* Мой исходный код в телеграм канале @AllApkaa*\n\n'
        f'*Ваш вопрос:* \n\n `{message.text} ` ', parse_mode='MARKDOWN')


executor.start_polling(dp)
