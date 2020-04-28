import discord

nbMessage = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        global nbMessage
        if message.author.id == self.user.id:
            return

        nbMessage += 1
        await message.channel.send(nbMessage)

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

client = MyClient()

client.run('NTU0NzI4Mjc2OTY3NTU1MDc3.XqFVfQ.xT8jEl9Tuedw-AQJIg5Fvc01Uv0')