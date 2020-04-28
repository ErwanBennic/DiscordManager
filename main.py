import discord
import time

nbMessage = 0
start_time = time.time()
words=["list", "of", "words"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        global nbMessage
        if message.author.id == self.user.id:
            return

        nbMessage += 1
        elapsed_time = time.time() - start_time

        print(elapsed_time)

        if nbMessage > 5 and elapsed_time < 5:
            await message.channel.send('Attention {0.author.mention}'.format(message) + ', vous êtes en train de spammer. Nombre de messages envoyés : ' + str(nbMessage))

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        if message.content.startswith('!uptime'):
            await message.channel.send('Le bot est en ligne depuis :' + str(elapsed_time) + ' secondes.')

        if message.content.startswith('!disconnect'):
            await client.close()

    async def on_message(self, message):
        if any(word in message.content.lower() for word in words):
            await message.delete()
            await message.channel.send(':warning: Attention {0.author.mention}, '.format(message) + ' votre message a été **supprimé** : merci d\'utiliser **un langage correct !**')

client = MyClient()
client.run('NTU0NzI4Mjc2OTY3NTU1MDc3.XqgFYw.O-67bvPEsHsgV0eO3ZIquD-r6_c')