import discord
import yt_dlp
from discord.ext import commands
import logging


class MusicController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_song = None

    @commands.command()
    async def play(self, ctx, url):
        """Воспроизведение музыки из ссылки"""
        if ctx.author.voice is None:
            await ctx.send("Вы не в голосовом канале")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio', 'title': True}
        vc = ctx.voice_client
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info.get("url")
            source = await discord.FFmpegOpusAudio.from_probe(url2, method='fallback', **FFMPEG_OPTIONS)
            vc.play(source)
            logging.info("Playing" + info.get("name"))

    @commands.command()
    async def leave(self, ctx):
        """Отключение бота от голосового канала"""
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
            await ctx.voice_client.disconnect()
