import discord
from discord.ext import commands


class Party(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def joinm(member):
        print(f'{member} has joined the party!')

    @commands.command()
    async def removem(member):
        print(f'{member} has left! Good riddance.')


def setup(client):
    client.add_cog(Party(client))