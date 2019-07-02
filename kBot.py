'''
 #      mmmmm           m
 #   m  #    #  mmm   mm#mm
 # m"   #mmmm" #" "#    #
 #"#    #    # #   #    #
 #  "m  #mmmm" "#m#"    "mm

 '''
import discord

token = 'NTkyNDg4NTkxMjgwNTcwMzgw.XRrjsA.415_bjWcX2omOx-DnJkptUKU9KI'
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves:
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        elif message.content == 'Hver er bestur?':
            await message.channel.send('''```
 _   _             _
| | | |_   _  __ _(_)
| |_| | | | |/ _` | |
|  _  | |_| | (_| | |
|_| |_|\__,_|\__, |_|
             |___/
            ```''')

client = MyClient()
client.run(token)

#Documentation of API is here: https://discordpy.readthedocs.io/en/latest/  