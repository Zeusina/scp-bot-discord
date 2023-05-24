# -*- coding: utf-8 -*-
from config import token
import asyncio
from bot_handlers.bot_init import bot
from bot_handlers import music, bot_events
import logging


async def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    async with bot:
        await bot.add_cog(music.Music(bot))
        await bot.start(token)
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Bot stopped by user")