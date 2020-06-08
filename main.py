import discord
import time

nbMessage = 0
start_time = time.time()
text_file = open("swearWords.txt", "r")
words = text_file.read().split()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        global nbMessage
        if message.author.id == self.user.id:
            return

        nbMessage += 1
        elapsed_time = time.time() - start_time

        print("Le bot est en ligne depuis %.0f" % elapsed_time + " secondes.")

        if nbMessage > 5 and elapsed_time < 5:
            await message.channel.send('Attention {0.author.mention}'.format(message) + ', tu es en train de spammer. Nombre de messages envoyés : ' + str(nbMessage))

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        if message.content.startswith('!uptime'):
            await message.channel.send('Le bot est en ligne depuis : ' + str(int(elapsed_time)) + ' secondes.')

        if message.content.startswith('!disconnect'):
            await message.channel.send('Le bot va s\'éteindre, veuillez patienter...')
            await client.close()

        if message.content.startswith('!help'):
            embed = discord.Embed(title="Liste des Commandes", color=0xffd500)
            imageURL = "https://cdn.discordapp.com/app-icons/554728276967555077/d2311bf0edfdd74c720abf4af04aac3a.png?size=256%22"
            embed.set_image(url=imageURL)
            embed.add_field(name="Hello World", value="!hello", inline=False)
            embed.add_field(name="Donne l'uptime du bot", value="!uptime", inline=False)
            embed.add_field(name="Déconnecte le bot", value="!disconnect", inline=False)
            embed.add_field(name="Ajoute un rôle à un utilisateur", value="!addrole {personne} {rôle}", inline=False)
            embed.set_footer(text="Requested by " + message.author.name, icon_url=message.author.avatar_url)

            await message.channel.send(embed=embed)

        for word in words:
            if word == message.content.lower():
                await message.delete()
                await message.channel.send(':warning: Attention {0.author.mention}, '.format(message) + ' votre message a été **supprimé** : merci d\'utiliser **un langage correct !**')

        # Faire une commande pour set le temps de timeout du spam

client = MyClient()
client.run('NTU0NzI4Mjc2OTY3NTU1MDc3.XqgORQ.4T8JXoVYzL4dMeuUH0FDajdNgPA')