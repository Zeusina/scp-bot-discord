# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
from config import token
from bot_handlers import bot_commands, bot_events


import youtube_dl
import os


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

bot.add_listener(bot_events.on_ready)
bot.add_command(bot_commands.join)
bot.add_command(bot_commands.leave)
bot.add_command(bot_commands.play)

bot.run(token)