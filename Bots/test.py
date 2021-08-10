import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('NjU1MDQ5OTA2NDY1MTQ0ODMy.XfOoAw.HUxxm6XA47AHpkGj3kr8w158kpY')