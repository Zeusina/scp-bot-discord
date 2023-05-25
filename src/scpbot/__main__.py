import discord
from os import getenv
import logging
from scpbot.utils import logging_conf
from discord.ext import commands
from scpbot.music import musiccontroller


logging_conf.configurate_logging()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.add_cog(musiccontroller.MusicController(bot))
    logging.info(f'We have logged in as {bot.user}')


bot.run(getenv("TOKEN"))
