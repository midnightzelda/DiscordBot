import discord
import random
from discord.ext import commands


class Chat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def fortune(self, ctx, *, question):
        """Ask Kazooie a question about the future.
                Parameters
                ------------
                channel: discord.VoiceChannel [Optional]
                    The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
                    will be made.
                This command also handles moving the bot to different channels.
                """
        responses = ['Yes',
                     'Most likely',
                     'Probably',
                     'Maybe',
                     'What do you think',
                     'Unlikely',
                     'When hell freezes over',
                     'No']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(aliases=['game'])
    async def nextgame(self, ctx):
        """gives a random selection from popular multiplayer games.
                Parameters
                ------------
                channel: discord.VoiceChannel [Optional]
                    The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
                    will be made.
                This command also handles moving the bot to different channels.
                """
        url = ['Resources/gpic/ark.jpg',
               'Resources/gpic/jackbox.jpg',
               'Resources/gpic/minecraft.png',
               'Resources/gpic/riskofrain.jpg',
               'Resources/gpic/smashbros.jpg',
               'Resources/gpic/seaofthieves.jpg',
               'Resources/gpic/portalknight.jpg',
               'Resources/gpic/raft.jpg',
               'Resources/gpic/scrapmech.jpg',
               'Resources/gpic/ageofempire.png',
               'Resources/gpic/civ.jpg',
               'Resources/gpic/warzone.jpg',
               'Resources/gpic/log.jpg',
               'Resources/gpic/ff.jpg',
               'Resources/gpic/terraria.jpg',
               'Resources/gpic/divinity.jpg',
               'Resources/gpic/chickenhorse.jpg',
               'Resources/gpic/mariokart.jpg',
               'Resources/gpic/fortnite.jpg',
               'Resources/gpic/brawlhalla.jpg',
               'Resources/gpic/gta.png',
               'Resources/gpic/halo.jpg']
        await ctx.send(f'What about this game?',file=discord.File(f'{random.choice(url)}'))


    @commands.command(aliases=['poke'])
    async def pokemon(self, ctx):
        """non functional pokecord replacement.
                Parameters
                ------------
                channel: discord.VoiceChannel [Optional]
                    The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
                    will be made.
                This command also handles moving the bot to different channels.
                """
        url = ['Resources/poke/pikachu.png',
               'Resources/poke/bulbasaur.png',
               'Resources/poke/charmander.png',
               'Resources/poke/squirtle.png',
               'Resources/poke/squirtleglasses.jpg']
        await ctx.send(file=discord.File(f'{random.choice(url)}'))

    @commands.command(aliases=['hus'])
    async def husband(self, ctx):
        """find your future husband.
                Parameters
                ------------
                channel: discord.VoiceChannel [Optional]
                    The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
                    will be made.
                This command also handles moving the bot to different channels.
                """

        await ctx.send(f'Here is your future husband', file=discord.File('Resources/male/' + f'{random.randint(1, 30)}' + '.jpg'))

    @commands.command(aliases=['wif'])
    async def wife(self, ctx):
        """find your future wife.
                Parameters
                ------------
                channel: discord.VoiceChannel [Optional]
                    The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
                    will be made.
                This command also handles moving the bot to different channels.
                """

        await ctx.send(f'Here is your future wife', file=discord.File('Resources/female/' + f'{random.randint(1, 30)}' + '.jpg'))

    @commands.command(aliases=['pussy'])
    async def cat(self, ctx):
        """find your future cat.
                Parameters
                ------------
                channel: discord.VoiceChannel [Optional]
                    The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
                    will be made.
                This command also handles moving the bot to different channels.
                """

        await ctx.send(f'Here is your future cat', file=discord.File('Resources/cat/' + f'{random.randint(1, 15)}' + '.jpg'))

    @commands.command(aliases=['pupper'])
    async def dog(self, ctx):
        """find your future dog.
                Parameters
                ------------
                channel: discord.VoiceChannel [Optional]
                    The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
                    will be made.
                This command also handles moving the bot to different channels.
                """

        await ctx.send(f'Here is your future dog', file=discord.File('Resources/dog/' + f'{random.randint(1, 15)}' + '.jpg'))

    @commands.command(aliases=['spo'])
    async def spouse(self, ctx):
        """non functional pokecord replacement.
                Parameters
                ------------
                channel: discord.VoiceChannel [Optional]
                    The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
                    will be made.
                This command also handles moving the bot to different channels.
                """
        responses = ['female',
                     'male']

        await ctx.send(f'Here is your future spouse', file=discord.File('Resources/' + f'{random.choice(responses)}' + '/' + f'{random.randint(1, 30)}' + '.jpg'))

    @commands.command()
    async def joke(self, ctx):
        """Be told an inside/regular joke.
                Parameters
                ------------
                channel: discord.VoiceChannel [Optional]
                    The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
                    will be made.
                This command also handles moving the bot to different channels.
                """
        responses = ['Horse went up in flames',
                     'Kitty Kitty Bang Bang',
                     'Squirtle',
                     'A mix between a Bulldog and a Shitzu. Is called a Bullshit']
        await ctx.send(f'{random.choice(responses)}')

    @commands.command(aliases=['drink'])
    async def mostlikely(self, ctx):
        """!drink, Prompts for most likely drinking game.
                Parameters
                ------------
                channel: discord.VoiceChannel [Optional]
                    The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
                    will be made.
                This command also handles moving the bot to different channels.
                """
        responses = ['have an affair',
                     'get married',
                     'get knocked up',
                     'throw trash out the window',
                     'kill someone',
                     'give money to the homeless',
                     'get married to a sex doll',
                     'burst into a song',
                     'crash a car',
                     'commit a train robbery',
                     'break up a marriage',
                     'play video games all day',
                     'sleep all day',
                     'die of stage fright',
                     'become famous',
                     'pay for a hooker',
                     'kidnap a child',
                     'get white girl wasted',
                     'become someone we used to know',
                     'get an std',
                     'become a vigilante',
                     'get bylaw called on them',
                     'get a parking ticket',
                     'fall down the stairs and die',
                     'live in another country',
                     'sleep with someone twice your age',
                     'join a cult',
                     'create a cult',
                     'be on the news',
                     'be a redneck',
                     'vote for trump',
                     'become a saint',
                     'survive a zombie attack',
                     'be the first voted off the island',
                     'have a deep dark secret',
                     'kill for money',
                     'Have their spouse disappear',
                     'own a tiger',
                     'turn someone gay with meth',
                     'be a undercover spy',
                     'form a rebellion',
                     'hack into the mainframe',
                     'be kicked out of the looney bin',
                     'get a sex concussion',
                     'trip over their own feet',
                     'call bylaw on their neighbour',
                     'steal bread for a starving family',
                     'commit tax fraud',
                     'become prime minister',
                     'sell their spouse on ebay',
                     'be the first to be bitten by a zombie',
                     'get down with the sickness',
                     'have baby fever',
                     'sell their kidney for the next iphone',
                     'become homeless',
                     'choke on a dick',
                     'ruin a party',
                     'become the grinch',
                     'give a $5 gift card as a birthday present',
                     'laugh to death',
                     'work for cupcakes',
                     'work as a hooker',
                     'spill juice on the carpet',
                     'lose a limb',
                     'become rich',
                     'die young',
                     'live forever',
                     'live at the gym',
                     'sell their soul to save a life',
                     'give a fake phone number',
                     'be alone forever',
                     'be into BDSM',
                     'become an alcoholic',
                     'cause a pandemic',
                     'make the bed',
                     'become a hoarder',
                     'have a terabyte worth of porn',
                     'get beaten up by a child',
                     'steal candy from a baby',
                     'forget thier child somewhere',
                     'dress to impress',
                     'give up on their dreams',
                     'own 10 cats',
                     'own 10 dogs',
                     'pay $100 for a pen',
                     'be caught outside',
                     'nail a guitar solo',
                     'go to jail',
                     'rage quit',
                     'flip the table',
                     'smoke weed',
                     'get their tongue stuck to a pole',
                     'sniff their own fart',
                     'fart in an elevator',
                     'grow a tube baby',
                     'become a monica',
                     'become a ross',
                     'become a joey',
                     'become a chandler',
                     'become a phoebe',
                     'gamble their house away',
                     'sell garbage for millions',
                     'pose for a nude photo',
                     'live with their parents forever',
                     'cure cancer',
                     'live in the jungle',
                     'win big brother',
                     'be a person everyone hates on reality tv',
                     'write a popular book',
                     'write a popular song',
                     'become bald',
                     'get randomly selected by airport security',
                     'join a pyramid scheme',
                     'gossip',
                     'urinate in public',
                     'join a gang',
                     'own a sword',
                     'free a whale from an aquarium',
                     'go on a road trip',
                     'kill their spouse with a frozen turkey then feed it to the cops',
                     'send a nude'
                     'get a surprise dick pic',
                     'smuggle drugs in their butt',
                     'become power hungry',
                     'become a comedian',
                     'create a popular game',
                     'bring someone back from the dead',
                     'sing a song confidently with the wrong lyrics',
                     'tip over a cow',
                     'live on a boat',
                     'find a monster under their bed',
                     'be friends with the monster under their bed',
                     'pay at dinner',
                     'lose their keys',
                     'screw up there, their and they\'re',
                     'make a robot',
                     'order groceries online',
                     'make a lit mix-tape',
                     'pick their nose',
                     'live their best life',
                     'be a hufflepuff',
                     'be a ravenclaw',
                     'be a slitherine',
                     'be a gryfindour',
                     'get accepted at hogwarts'
                     'teach sex-ed',
                     'be the first to resort to cannibalism',
                     'go a day without eating',
                     'get fired from their job',
                     'sass a mugger',
                     'live of the grid',
                     'go weeks without a shower',
                     'be a disney princess',
                     'own a shark',
                     'bang ms.frizzle in the magic school bus',
                     'have sex at church',
                     'fall in loved with themselves',
                     'have sex on the first date',
                     'own 100,000 books',
                     'watch tv all day',
                     'donate to a charity',
                     'suggest a drinking game out of the blue',
                     'butcher a language',
                     'buy a fancy car',
                     'catch feelings',
                     'wave back and find out they were waving at someone else',
                     'be a bad bitch',
                     'experiment with the same gender',
                     'be mistaken for the wrong gender',
                     'sound like marge simpson',
                     'give a 2 hour long lecture',
                     'travel to space',
                     'pee themselves',
                     'grind at the club',
                     'run a red light',
                     'get pulled over for speeding',
                     'own a poster saying live, laugh, love']
        await ctx.send(f'who is most likely to ' + f'{random.choice(responses)}')


def setup(client):
    client.add_cog(Chat(client))
