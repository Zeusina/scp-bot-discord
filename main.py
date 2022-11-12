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

# adding listeners to bot
bot.add_listener(bot_events.on_ready)

# adding commands to bot
bot.add_command(bot_commands.join)
bot.add_command(bot_commands.leave)
bot.add_command(bot_commands.play)
bot.add_command(bot_commands.pause)
bot.add_command(bot_commands.resume)
bot.add_command(bot_commands.stop)


# running bot
bot.run(token)