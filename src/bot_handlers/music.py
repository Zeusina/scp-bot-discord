from discord.ext import commands
import youtube_dl
import discord


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """Подключение бота к голосовому каналу"""
        if ctx.author.voice is None:
            await ctx.send("Вы не в голосовом канале")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def leave(self, ctx):
        """Отключение бота от голосового канала"""
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
            await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        """Проигрывание аудио"""
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
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

    @commands.command()
    async def pause(self, ctx):
        """Приостанавка воспроизведения"""
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
            if ctx.voice_client.is_playing():
                ctx.voice_client.pause()
            else:
                await ctx.send("Ничего не играет")

    @commands.command()
    async def resume(self, ctx):
        """Продолжение воспроизведения"""
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
            if ctx.voice_client.is_paused():
                ctx.voice_client.resume()
            else:
                await ctx.send("Ничего не играет")

    @commands.command()
    async def stop(self, ctx):
        """Остановка воспризведения"""
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
            ctx.voice_client.stop()
            await ctx.send("Остановлено")

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Изменение громкости"""
        if ctx.voice_client is None:
            await ctx.send("Бот не в голосовом канале")
        else:
            ctx.voice_client.source.volume = int(volume) / 100
            await ctx.send(f"Громкость установлена на {volume}%")