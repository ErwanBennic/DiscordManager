import discord

client = discord.Client()
message_counter = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!help'):
        await message.channel.send('Liste des commandes disponibles : !hello')


@client.event
async def on_message(message):
    global message_counter
    message_counter += 1
    await message.channel.send('Nombre de messages envoyés : '+ str(message_counter))

client.run('NTU0NzI4Mjc2OTY3NTU1MDc3.XqFVfQ.xT8jEl9Tuedw-AQJIg5Fvc01Uv0')