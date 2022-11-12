import discord
from discord.ext import commands


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
