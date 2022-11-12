# -*- coding: utf-8 -*-
from config import token
import asyncio
from bot_handlers.bot_init import bot
from bot_handlers import music, bot_events
import discord
from discord.ext import commands


import youtube_dl
import os


async def main():
    async with bot:
        await bot.add_cog(music.Music(bot))
        await bot.start(token)

asyncio.run(main())