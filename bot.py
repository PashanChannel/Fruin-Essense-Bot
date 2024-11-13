from telebot.async_telebot import AsyncTeleBot, types
from config import bot_token, bot_version
from languages.uk import messages as uk
import asyncio

# Ініціалізація бота
bot = AsyncTeleBot(bot_token, parse_mode='HTML', disable_web_page_preview=True, colorful_logs=True)

@bot.message_handler(commands=['start'])
async def message_start(message):
    if message.chat.type == 'private':
        markup = types.InlineKeyboardMarkup(row_width=1)
        tg_channel = types.InlineKeyboardButton('Fruin Studios', url='https://t.me/fruin_studios')
        tg_nestor_churin = types.InlineKeyboardButton('Nestor Churin', url='https://t.me/nestor_churin')
        markup.add(tg_channel, tg_nestor_churin)
        start_message = uk["start"].format(bot_version)
        await bot.send_message(message.chat.id, f'{start_message}', reply_markup=markup)
    else:
        break_message = uk["start"]
        await bot.reply_to(message, break_message)

@bot.message_handler(commands=['help'])
async def message_help(message):
    if message.chat.type == 'private':
        help_message = uk["help"]
        await bot.send_message(message.chat.id, f'{help_message}')
    else: return

# Запуск бота з polling
async def run_bot():
    print(f"Bot version {bot_version} is starting...")
    await bot.polling(skip_pending=True)

# Запускаємо polling у головній функції
if __name__ == "__main__":
    asyncio.run(run_bot())
