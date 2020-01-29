import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='', type=1))


@client.event
async def on_message(message):
    if message.content.startswith("hi"):
        await client.send_message(message.channel, "HI")
        
    if message.content.startswith("test"):
        await client.send_message(message.channel, "Works!")

    if message.content.startswith("/dm"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        print("send dm!")
        await author.send(msg)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
