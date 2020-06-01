import discord
import openpyxl
import datetime

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("기다리고 있는중")
    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):

    if message.author.bot:
        return None

    if message.content.startswith("{싹수야 도움말"):
        await message.channel.send("무슨 도움말을 할까요?")
        await message.channel.send("https://cdn.discordapp.com/attachments/714377816421957663/716943029298266123/21cf9b2c60bdb65b.png")

    if message.content.startswith("{싹수야?"):
        await message.channel.send("네?")
        await message.channel.send("https://cdn.discordapp.com/attachments/716541654848503890/716935341822443520/6ed0b344b1b53351.png")

    if message.content.startswith("{싹수야 아잉아잉"):
        await message.channel.send("그거 저두 할수 있어요!")
        await message.channel.send("https://cdn.discordapp.com/attachments/716541654848503890/716936060004859965/8eeefe382170c0d0.png")

    if message.content.startswith("{싹수야 빙글뱅글"):
        await message.channel.send("으어어 새상이 돈드아@@@")
        await message.channel.send("https://cdn.discordapp.com/attachments/716541654848503890/716938451832012840/d78d73a147eec6cd.png")

    if message.content.startswith("{싹수야 싸가지 없네"):
        await message.channel.send("저 아직 싹이 없어요!")
        await message.channel.send("https://cdn.discordapp.com/attachments/716541654848503890/716938679439982632/6f23d3b66b38d556.png")

    if message.content.startswith("{싹수야 철좀 들어"):
        await message.channel.send("저 철 들어 올립니다!")
        await message.channel.send("https://cdn.discordapp.com/attachments/716541654848503890/716938958734622760/8816e73502778769.png")

    if message.content.startswith("{싹수야 안녕"):
        await message.channel.send("안녕하세요!")
        await message.channel.send("https://cdn.discordapp.com/attachments/716541654848503890/716939473212145684/7c3066eb17612b3d.png")

    if message.content.startswith("{싹수야 칼"):
        await message.channel.send("난 칼을 들고있다. 무섭지?")
        await message.channel.send("https://cdn.discordapp.com/attachments/716541654848503890/716939637666349096/67bd543e530e4074.png")

    if message.content.startswith("{싹수야 함수"):
        await message.channel.send("우웨 너한테 함수 냄새나 ;;")
        await message.channel.send("https://cdn.discordapp.com/attachments/716541654848503890/716957373629202432/0d0cf5c9aeb72e5a.png")

    if message.content.startswith("{싹수야 ㅋㅋㅋ"):
        await message.channel.send("하하하!")
        await message.channel.send("https://cdn.discordapp.com/attachments/716541654848503890/716959751128481862/4a4edfeda586e5d8.png")

    if message.content.startswith("{싹수야 코스프레 함수"):
        await message.channel.send("나는 함수다!")
        await message.channel.send("https://cdn.discordapp.com/attachments/716541654848503890/716960211382042625/87ae8bf9a5d6e494.png")

    if message.content.startswith("{싹수야 프로필"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="사용자 이름", value=message.author.name, inline=True)
        embed.add_field(name="서버 사용자 이름", value=message.author.display_name, inline=True)
        embed.add_field(name="가입 날짜", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="사용자 ID", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith(""):
        file = openpyxl.load_workbook("호감도.xlsx")
        sheet = file.active
        exp = [50, 150, 400, 800, 1300, 2000, 2800, 3700, 4800, 6000, 7300, 9200, 11500, 13000]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 5
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value - 1]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    await message.channel.send("싹수와의 호감도가 올랐습니다.\n현재 호감도 : " + str(sheet["C" + str(i)].value) + "\n경험치 : " + str(sheet["B" + str(i)].value))
                file.save("호감도.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                file.save("호감도.xlsx")
                break

            i += 1

client.run("NzE2OTA4MjYzMTEwNzM3OTQw.XtSnEA.d2cgMl0u6FlqZZM7xptH1w-_PAQ")