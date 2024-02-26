import discord
import random
import time
from discord.ext import commands

# --MISC--


class MISC(commands.Cog):

    def __init__(self, client):
        self.client = client

    # ping command. *rounded numbers*
    @commands.command(aliases=['ping', 'lag'])
    async def latency(self, ctx):
        await ctx.send(f'Bot latency =  {round(self.client.latency * 1000)}ms\n{self.client.latency}')

    # descision command. says yes or no
    @commands.command(aliases=['decision'])
    async def decide(self, ctx, *, question):
        decision_responses = ['Yes', 'No', 'Perhaps']
        await ctx.send(f'Question: {question}\nFrom: {ctx.author.mention}\nAnswer: {random.choice(decision_responses)}')

    # say command. Repeats what you say and deletes the original command.
    @commands.command(aliases=['repeat'])
    async def say(self, ctx, *, question):
        await ctx.message.delete()
        await ctx.send(f'{question}')

    # coinflip command. does heads or tails randomly.
    @commands.command(aliases=['heads', 'tails', 'coin'])
    async def coinflip(self, ctx):
        coin_responses = ['heads', 'tails']
        await ctx.send(f'{random.choice(coin_responses)}')

    # rickroll command
    @commands.command(aliases=['apply_admin', 'role_admin', 'assign_admin', 'administrator', 'giveadmin'])
    async def give_me_admin(self, ctx):
        rickrolls = [
            'https://media.giphy.com/media/lgcUUCXgC8mEo/giphy.gif',
            'https://gfycat.com/sanedisgustingatlanticridleyturtle'
        ]
        await ctx.send(f'{ctx.author.mention}, you are such a fool. :stuck_out_tongue_winking_eye:\n {random.choice(rickrolls)}')

    # 8 Ball command
    @commands.command(aliases=['8_ball', '8ball'])
    async def eightball(self, ctx, *, question):
        eightball_responses = [
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes, definitely.',
            'You may rely on it.',
            'Yesn\'t',
            'Idk man you tell me.',
            'lmao don\'t keep your hopes up'
        ]
        await ctx.send(f'Question: {question}\nFrom: {ctx.author.mention}\nAnswer: {random.choice(eightball_responses)}')

    # ily command
    @commands.command()
    async def ily(self, ctx):
        ily_responses = [
            'I love you too. ||no homo||',
            'I love you too. ||full homo||',
            'bitch stfu',
            'bitch, 𝔁𝓾𝓮:cold_face:𝓱𝓾𝓪:woman_fairy:𝓹𝓲𝓪𝓸:heart_eyes_cat:𝓹𝓲𝓪𝓸:moyai:𝓫𝓮𝓲:japanese_goblin:𝓯𝓮𝓷𝓰:star_struck:𝔁𝓲𝓪𝓸:smirk_cat:𝔁𝓲𝓪𝓸:footprints:',
            ':heart_eyes: Yeah? ||Well I don\'t :sparkles: :fairy:||'
        ]
        await ctx.send(random.choice(ily_responses))

    # checks if its tinah
    def is_it_tinah(ctx):
        return ctx.author.id == 498654378840817675

    # Tinah's command
    @commands.command(aliases=['whos', 'who\'s', 'who'])
    @commands.check(is_it_tinah)
    async def daddy(self, ctx):
        await ctx.send('<@498654378840817675>')

    # Replay Iyaz Command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def replay(self, ctx):
        replay_lyrics = [
            'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'Remember the first time we met', 'You was at the mall with your friends', 'I was scared to approach ya', 'But then you came closer', 'Hopin\' you would give me a chance', 'Who would have ever knew', 'That we would ever be more than friends', 'We\'re real worldwide', 'breakin all the rules', 'She like a song played again and again', 'That girl', 'like somethin off a poster', 'That girl', 'is a dime they say', 'That girl', 'is a gun to my holster', 'She\'s runnin through my mind all day', 'ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'See you been all around the globe', 'Not once did you leave my mind', 'We talk on the phone', 'from night til the morn', 'Girl you really change my life', 'Doin things I never do', 'I\'m in the kitchen cookin things she likes', 'We\'re real worldwide', 'breakin all the rules', 'Someday I wanna make you my wife', 'That girl', 'like somethin off a poster', 'That girl', 'is a dime they say', 'That girl', 'is the gun to my holster', 'She\'s runnin through my mind all day', 'ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'I can be your melody, A girl that could write you a symphony', 'The one that could fill your fantasies', 'So come baby girl let\'s sing with me', 'Ay', 'I can be your melody', 'A girl that could write you a symphony', 'The one that could fill your fantasies', 'So come baby girl let\'s sing with me', 'Ay', 'na na na na na na na', 'Na na na na na na', 'Shawty got me singin', 'Na na na na na na na', 'Na na na na na na na', 'Now she got me singin', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay', 'Shawty\'s like a melody in my head', 'That I can\'t keep out', 'Got me singin\' like', 'Na na na na everyday', 'It\'s like my ipod stuck on replay', 'replay-ay-ay-ay'
        ]
        for l in replay_lyrics:
            await ctx.send(l)
            time.sleep(1.5)

    # triangle test
    @commands.command(aliases=['trig', 'tri', 'triangle'])
    async def triangulate(self, ctx, *, question):
        max_str_len = 8
        if len(question) <= max_str_len:
            i = 0
            for x in question:
                await ctx.send(question[0:i+1])
                time.sleep(0.5)
                i += 1
                if i == len(question):
                    for x in question:
                        i -= 1
                        if i == 0:
                            break
                        await ctx.send(question[0:i])
                        time.sleep(1)
        else:
            await ctx.send(f'That message is too long. I will only accept messages that are {max_str_len} characters in length.')

# Cog Setup


def setup(client):
    client.add_cog(MISC(client))
