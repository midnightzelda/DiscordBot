import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix='!')

players = {}


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Banjo Kazooie'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('NjU1MDQ5OTA2NDY1MTQ0ODMy.XfOoAw.HUxxm6XA47AHpkGj3kr8w158kpY')