import logging

import discord
from discord.ext import commands
import yt_dlp


class Music(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="play", aliases=["p", "pl"], help="Воспроизведение музыки из ссылки")
    async def play(self, ctx, url):
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
            logging.info("Playing: " + info.get("title"))

    @commands.command(name="leave", aliases=["l", "le"], help="Команда боту выйти из голосового канала")
    async def leave(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
            await ctx.voice_client.disconnect()

    @commands.command(name="join", aliases=["j", "jo"], help="Подключение бота к голосовому каналу")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Вы не в голосовом канале")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command(name="pause", aliases=["pa"], help="Приостановка воспроизведения")
    async def pause(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
            if ctx.voice_client.is_playing():
                ctx.voice_client.pause()
            else:
                await ctx.send("Ничего не играет")

    @commands.command(name="resume", aliases=["r", "re"], help="Продолжение воспроизведения")
    async def resume(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
            if ctx.voice_client.is_paused():
                ctx.voice_client.resume()
            else:
                await ctx.send("Ничего не играет")

    @commands.command(name="stop", aliases=["s", "st"], help="Остановка воспризведения")
    async def stop(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
            ctx.voice_client.stop()
            await ctx.send("Остановлено")
