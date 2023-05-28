import discord
import yt_dlp
from discord.ext import commands
import logging


class MusicController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_song = None


