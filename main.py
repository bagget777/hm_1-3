import random
from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token)
dp = Dispatcher(bot)

numbers = [1, 2, 3, 4, 5]

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("нажми на /help")

@dp.message_handler(commands='help')
async def start(message:types.Message):
    await message.answer("""нажмите на
/test""")

@dp.message_handler(commands='test')
async def testing(message: types.Message):
    secret_number = random.choice(numbers)
    await message.answer(f"Я выбрал случайное число из пяти вариантов. Попробуйте угадать: {numbers}")

    @dp.message_handler()
    async def guess_number(message: types.Message):
        try:
            guess = int(message.text)
            if guess == secret_number:
                await message.answer("Правильно! Вы угадали число.")
            else:
                await message.answer("Неправильно. Попробуйте еще раз.")
        except ValueError:
            await message.answer("Пожалуйста, введите число.")

executor.start_polling(dp)
