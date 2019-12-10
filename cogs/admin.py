import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('txt/whitelist.txt', 'r') as fp:
            self.whitelist = fp.read().splitlines()
        

    def noPerm(self):
        return 'You do not have permission to run this command'

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
        if str(ctx.author.id) in self.whitelist:
            await ctx.channel.purge(limit = (numberOfMessages + 1))
        else:
            await ctx.channel.send(self.noPerm())
    '''
    This command lets the whitelisted user to create a custom announcement 
    in the server.
    '''
    @commands.command(aliases = ['broadcast'])
    async def announce(self, ctx, *, message):
        sendChannel = self.bot.get_channel(635840445079093250)                                  #Specifies which channel to send the response to

        if str(ctx.author.id) in self.whitelist and ctx.channel.id == 636045039386230784:        #Checks to see if the command is written by a whitelisted user and in the right channel
            await sendChannel.send(f'@everyone {message}')
        else:
            await ctx.channel.send(self.noPerm())
    
    '''
    This command kicks the user that is mentioned
    '''
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        sendChannel = self.bot.get_channel(635840445079093250)

        if str(ctx.author.id) in self.whitelist: 
            await member.kick(reason = reason)
            await sendChannel.send(f'User {member.mention} has been kicked due to: {reason}', delete_after = 10)
        else:
            await ctx.channel.send(self.noPerm())

    '''
    This command bans the user that is mentioned
    '''
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        sendChannel = self.bot.get_channel(635840445079093250)

        if str(ctx.author.id) in self.whitelist: 
            await member.ban(reason = reason)
            await sendChannel.send(f'User {member.mention} has been banned due to: {reason}', delete_after = 10)
        else:
            await ctx.channel.send(self.noPerm())
    
    '''
    This command is used to inflict psychological damage
    by harassing mentioned users everytime they send a message
    forever. This command is irreversible.
    '''
    @commands.command()
    async def harass(self, ctx):
        if str(ctx.author.id) in self.whitelist:
            toBeAdded = ctx.message.mentions                #List of users mentioned in the message

            with open('txt/peopletoharass.txt', 'a') as fp:
                for user in toBeAdded:
                    fp.write(f'{user}\n')
        else:
            ctx.channel.send(self.noPerm())

    @commands.command(name = 'addadmin', aliases = ['whitelist'])
    async def addAdmin(self, ctx, member: discord.Member):
        print(str(ctx.author.id) in self.whitelist)

        if str(ctx.author.id) in self.whitelist:

            self.whitelist.append(member.id)
            with open('txt/whitelist.txt', 'w') as fp:
                for user in self.whitelist:
                    fp.write(f'{user}\n')

            await ctx.channel.send(f'{member.mention}has been added to the whitelist', delete_after = 10)
        else:
            await ctx.channel.send(self.noPerm())

    @commands.command(name = 'removeadmin', aliases = ['unwhitelist'])
    async def removeAdmin(self, ctx, member: discord.Member):
        if str(ctx.author.id) in self.whitelist:

            self.whitelist.remove(str(member.id))
            
            with open ('txt/whitelist.txt' , 'w') as fp:
                for user in self.whitelist:
                    fp.write(f'{user}\n')

            await ctx.channel.send(f'{member.mention} have been removed from the whitelist', delete_after = 10)

        else:
            await ctx.channel.send(self.noPerm())


'''
Sets up the bot object as a cog
'''
def setup(bot):
    bot.add_cog(Admin(bot))