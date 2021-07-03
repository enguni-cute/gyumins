import discord
from discord.utils import get
import os
from bs4 import BeautifulSoup
import urllib
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("준비완료")
    game = discord.Game("경민이랑")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("ㅎㅇ"):
        await message.channel.send("하이")
    if message.content.startswith("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ"):
        await message.channel.send("뭘 빠개 패고싶게")
    if message.content.startswith("야"):
        await message.channel.send("ㅇ")
    if message.content.startswith("씨발"):
        await message.channel.send("욕하지마 라고 재형이가 시켰어")
    if message.content.startswith("엥구니"):
        await message.channel.send("엥그이")
    if message.content.startswith("ㅇㅋ"):
        await message.channel.send("㉧")
    if message.content.startswith("ㅗ"):
        await message.channel.send("개 빡세.......Ah..")
    if message.content.startswith("규민아"):
        await message.channel.send("왱 ㅎㅎ")
    if message.content.startswith("김규민"):
        await message.channel.send("뭐 씨발 개 븅신년아 라고 재형이가 하래...")
    if message.content.startswith("용재야"):
        await message.channel.send("왜 불러~~")
    if message.content.startswith("ㅅㄱ"):
        await message.channel.send("수고")
    if message.content.startswith("어쩌라고"):
        await message.channel.send("띠껍네")
    if message.content.startswith("병신"):
        await message.channel.send("욕을하네..")
    if message.content.startswith("븅신"):
        await message.channel.send("왜 그러고 사니,,")
    if message.content.startswith("좆"):
        await message.channel.send("응 니 2.6cm")
    if message.content.startswith("노"):
        await message.channel.send("망난")
    if message.content.startswith("씹년아"):
        await message.channel.send("뭐 병Sin아")
    if message.content.startswith("엥기"):
        await message.channel.send("엥구이!!!!!!!!!!!!!!!!!!")
    if message.content.startswith("ㄴㅁ"):
        await message.channel.send("응 녬")
    if message.content.startswith("잘생겼다"):
        await message.channel.send("ㅋ")
    if message.content.startswith("ㅇ"):
        await message.channel.send("㉪㉪")
    if message.content.startswith("시발"):
        await message.channel.send("욕하네 ")
    if message.content.startswith("?"):
        await message.channel.send("뭐 찌질한 새끼야")
 
if ctx.author.voice and ctx.author.voice.channel:
channel = ctx.author.voice.channel
await channel.connect()

@app.command(name="참가", pass_context=True)
async def _join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("아무도 없잖아 Tq련아")
await app.voice_clients[0].disconnect()
        
@app.command(name="연결끊기")
async def _leave(ctx):
    await app.voice_clients[0].disconnect()
    
access_token = os.environ['BOT_TOKEN']
client.run(access_token)
