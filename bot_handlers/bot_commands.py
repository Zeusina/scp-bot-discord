import discord
from discord.ext import commands
import youtube_dl


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


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


@bot.command()
async def play(ctx, url):
    """Воспроизведение музыки"""
    if ctx.voice_client is None:
        await ctx.send("Бот не в голосовом канале")
        return
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': "bestaudio"}
    vc = ctx.voice_client
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, method='fallback', **FFMPEG_OPTIONS)
        vc.play(source)
        print("Playing")

@bot.command()
async def pause(ctx):
    """Пауза"""
    if ctx.voice_client is None:
        await ctx.send("Бот не в голосовом канале")
        return
    if ctx.voice_client.is_playing():
        ctx.voice_client.pause()
    else:
        await ctx.send("Бот не воспроизводит музыку")

@bot.command()
async def resume(ctx):
    """Продолжить"""
    if ctx.voice_client is None:
        await ctx.send("Бот не в голосовом канале")
        return
    if ctx.voice_client.is_paused():
        ctx.voice_client.resume()
    else:
        await ctx.send("Бот не на паузе")

@bot.command()
async def stop(ctx):
    """Остановить"""
    if ctx.voice_client is None:
        await ctx.send("Бот не в голосовом канале")
        return
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
    else:
        await ctx.send("Бот не воспроизводит музыку")



