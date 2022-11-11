# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
from config import token


import youtube_dl
import os
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"Получено сообщение: {message.content} {message}")
    await message.reply(f"{message.content}")

bot.run(token)