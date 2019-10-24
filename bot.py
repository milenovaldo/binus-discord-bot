import discord
from discord.ext import commands
from random import randint
from time import sleep

class BinusBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.noPerm = 'You do not have permission to run this command'
    
    '''
    Notifies us when the bot is ready to function.
    '''
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user}')  
        await self.bot.change_presence(status = discord.Status.online, activity = discord.Game('Ready to accept commands'))   

    '''
    Creates an announcement when someone joins the server and sends
    the new member the rules of the server.
    '''
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(635840445079093250)
        await channel.send(f'Please welcome {member.mention} to the server', delete_after = 10)
        await member.send(
            f'Welcome to Binus Discord server \n' +
            f'Please read the rules below: \n' +
            f'1. Do not be annoying \n' +
            f'2. Do not send inflammatory messages in the server or to anyone in the server \n' +
            f'Breaking these rules will result in a perma ban.'
        )

    '''
    Creates an announcement when someone gets banned from the server
    '''
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        channel = self.bot.get_channel(635840445079093250)
        await channel.send(f'User {member} has been banned from the server', delete_after = 10)

    '''
    Creates an announcement when someone gets unbanned in the server
    '''
    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        channel = self.bot.get_channel(635840445079093250)
        await channel.send(f'User {member} has been unbanned from the server', delete_after = 10)

    @commands.Cog.listener()
    async def on_message(self, message):
        '''
        Bad words filtering
        Checks if every word contained in the message is in the list of 
        dirty words.
        If yes, then the bot delete the last message the sends a reminder
        as a response.
        '''

        if message.author.id == 635833390238793729:
            return

        mentionUser = message.author.mention
        responseList = [
            f'{mentionUser} Please keep it clean bro',
            f'{mentionUser} Did your mom not raise you properly bro?',
            f'{mentionUser} I\'m calling the police on you bro'
        ]
        
        with open('txt/dirtywords.txt', 'r') as fp:                 
            dirtywords = fp.read().splitlines()
        for word in message.content.split():
            if word.lower() in dirtywords:
                await message.delete()
                await message.channel.send(responseList[randint(0, len(responseList)-1)], delete_after = 10)
        '''
        Checks if user who wrote a message is in the "people to harass"
        list. If yes, the bot will respond with a harassment message
        '''
        with open('txt/peopletoharass.txt', 'r') as fp:
            harassUserList = fp.read().splitlines()
        with open('txt/harassmentreponses.txt', 'r') as fp:
            harassmentResponses = fp.read().splitlines()
        print(message.author)
        print(harassUserList)
        if str(message.author) in harassUserList:
            try:
                randNum = randint(0, len(harassmentResponses) - 1)
                await message.channel.send(f'{message.author.mention} {harassmentResponses[randNum]}')
                if randNum == 6:
                    sleep(5)
                    await message.channel.send(f'{message.author.mention} Sike, bitch')
                else:
                    pass
            except IndexError:
                print('Harassment response empty. Fill in the "harassmentreponses.txt"')

    '''
    Command to ask the latency of the bot in milliseconds
    '''
    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send(f'{round(self.bot.latency * 1000)} ms', delete_after = 10)

    '''
    This command clears the past few messages
    '''
    @commands.command(aliases = ['clear', 'clr'])
    async def clearMessages(self, ctx, numberOfMessages: int = 10):
        if ctx.author.id == 204172911962095616:
            await ctx.channel.purge(limit = numberOfMessages)
        else:
            await ctx.channel.send(self.noPerm)
    '''
    This command lets the whitelisted user to create a custom announcement 
    in the server.
    '''
    @commands.command(aliases = ['broadcast'])
    async def announce(self, ctx, *, message):
        sendChannel = self.bot.get_channel(635840445079093250)                                  #Specifies which channel to send the response to
        if ctx.author.id == 204172911962095616 and ctx.channel.id == 636045039386230784:        #Checks to see if the command is written by a whitelisted user and in the right channel
            await sendChannel.send(f'@everyone {message}')
        else:
            await ctx.channel.send(self.noPerm)
    
    '''
    This command kicks the user that is mentioned
    '''
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        if ctx.author.id == 204172911962095616: 
            await member.kick(reason = reason)
            await ctx.channel.send(f'User {member.mention} has been kicked due to: {reason}')
        else:
            await ctx.channel.send(self.noPerm)

    '''
    This command bans the user that is mentioned
    '''
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        if ctx.author.id == 204172911962095616: 
            await member.ban(reason = reason)
            await ctx.channel.send(f'User {member.mention} has been banned due to: {reason}')
        else:
            await ctx.channel.send(self.noPerm)


    '''
    This command is used to inflict psychological damage
    by harassing mentioned users everytime they send a message
    forever. This command is irreversible.
    '''
    @commands.command()
    async def harass(self, ctx):
        if ctx.author.id == 204172911962095616:
            toBeAdded = ctx.message.mentions                #List of users mentioned in the message
            with open('txt/peopletoharass.txt', 'a') as fp:
                for user in toBeAdded:
                    fp.write(f'{user}\n')      
        else:
            ctx.channel.send(self.noPerm)

'''
Sets up the bot object as a cog
'''
def setup(bot):
    bot.add_cog(BinusBot(bot))
