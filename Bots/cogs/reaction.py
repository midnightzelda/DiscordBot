import discord
import random
from discord.ext import commands


class Reaction(commands.Cog):


    def __init__(self, client):
        self.client = client

    @commands.command()
    async def jiggy(self, ctx):
        await ctx.send(f'Hand it over!')


def setup(client):
    client.add_cog(Reaction(client))