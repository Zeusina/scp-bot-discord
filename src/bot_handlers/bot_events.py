from bot_handlers.bot_init import bot


@bot.event
async def on_ready():
    print('Бот запущен')
