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

@bot.command()
async def join(ctx):
    """Подключение бота к голосовому каналу"""
    if ctx.author.voice is None:
        await ctx.send("Вы не в голосовом канале!")
        return
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    """Отключение бота от голосового канала"""
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("Бот не в голосовом канале")


bot.run(token)