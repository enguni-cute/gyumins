import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("준비완료")
    game = discord.Game("Assetto Corsa")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("ㅎㅇ"):
        await message.channel.send("하이")
    if message.content.startswith("ㅋㅋ"):
        await message.channel.send("너무 띠껍네..")
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
    if message.content.startswith("노무현"):
        await message.channel.send("이기야!!!!!!!!!")
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
    if message.content.startswith("ㅋ"):
        await message.channel.send("개띠껍네 ㅄ년")
    if message.content.startswith("?"):
        await message.channel.send("뭐 찌질한 새끼야")
    if message.content.startswith("!p"):
        await message.channel.send(":thumbsup:Joined `음성 채널` and bound to #채팅방")
        await message.channel.send("👍")






access_token = os.environ['BOT_TOKEN']
client.run(access_token)
