import discord
import json
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('json/data.json', 'r') as fp:
            self.idJson = json.load(fp)
        self.whitelist = list(map(int, self.idJson["ID"]["whitelistedUsers"]))
        self.generalChannelID = int(self.idJson["ID"]["generalChannel"])
        self.general = self.bot.get_channel(self.generalChannelID) 
        
    def noPerm(self):
        return 'You do not have permission to run this command'

    def jsonDump(self):
        with open('json/data.json', 'w') as fileToDump:
            json.dump(self.idJson, fileToDump, indent = 4)


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
        if ctx.author.id in self.whitelist:
            await ctx.channel.purge(limit = (numberOfMessages + 1))
        else:
            await ctx.channel.send(self.noPerm())
    '''
    This command lets the whitelisted user to create a custom announcement 
    in the server.
    '''
    @commands.command(aliases = ['broadcast'])
    async def announce(self, ctx, *, message):                                
        if ctx.author.id in self.whitelist:        
            await self.general.send(f'@everyone {message}')
        else:
            await ctx.channel.send(self.noPerm())
    
    '''
    This command kicks the user that is mentioned
    '''
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        if ctx.author.id in self.whitelist: 
            await member.kick(reason = reason)
            await self.general.send(f'User {member.mention} has been kicked due to: {reason}', delete_after = 10)
        else:
            await ctx.channel.send(self.noPerm())

    '''
    This command bans the user that is mentioned
    '''
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        if ctx.author.id in self.whitelist: 
            await member.ban(reason = reason)
            await self.general.send(f'User {member.mention} has been banned due to: {reason}', delete_after = 10)
        else:
            await ctx.channel.send(self.noPerm())
    
    '''
    This command is used to inflict psychological damage
    by harassing mentioned users everytime they send a message
    forever. This command is irreversible.
    '''
    @commands.command()
    async def harass(self, ctx):
        if ctx.author.id in self.whitelist:
            toBeAdded = ctx.message.mentions                #List of users mentioned in the message

            with open('txt/peopletoharass.txt', 'a') as fp:
                for user in toBeAdded:
                    fp.write(f'{user}\n')
        else:
            await ctx.channel.send(self.noPerm())


    '''
    Adds a mentioned user to the whitelist
    whitelisted user have access to the moderation commands, etc
    '''
    @commands.command(name = 'addadmin', aliases = ['whitelist'])
    async def addAdmin(self, ctx, member: discord.Member):
        if ctx.author.id in self.whitelist:
            self.idJson["ID"]["whitelistedUsers"].append(member.id)

            self.jsonDump()

            await ctx.channel.send(f'{member.mention}has been added to the whitelist', delete_after = 10)
        else:
            await ctx.channel.send(self.noPerm())

    '''
    Removes a mentioned user from the bot's whitelist
    '''
    @commands.command(name = 'removeadmin', aliases = ['unwhitelist', 'rmadmin'])
    async def removeAdmin(self, ctx, member: discord.Member):
        if ctx.author.id in self.whitelist:
            self.idJson["ID"]["whitelistedUsers"].remove(member.id)

            self.jsonDump()

            await ctx.channel.send(f'{member.mention} have been removed from the whitelist', delete_after = 10)

        else:
            await ctx.channel.send(self.noPerm())

    '''
    If the 'general' channel name was renamed, this command
    reassigns a channel this command is ran in as the new 'general'
    '''
    @commands.command(name = 'setgeneral')
    async def setGeneral(self, ctx):
        if ctx.author.id in self.whitelist:
            self.idJson["ID"]["generalChannel"] = ctx.message.channel.id

            self.jsonDump()

            await ctx.channel.send(f'This text channel has been set as the \'general\' channel.', delete_after = 10)
            
        else:
            await ctx.channel.send(self.noPerm())

    '''
    Set a music voice channel
    '''
    @commands.command(name = 'setmusic', aliases = ['musicchannel', 'setmusicchannel'])
    async def setMusic(self, ctx):
        if ctx.author.id in self.whitelist:
            try:
                self.idJson["ID"]["musicChannel"] = ctx.author.voice.channel.id

                self.jsonDump()
            except AttributeError:
                await ctx.channel.send(f'Please be in a voice channel to set the music voice channel', delete_after = 10)
        else:
            await ctx.channel.send(self.noPerm())
            

'''
Sets up the bot object as a cog
'''
def setup(bot):
    bot.add_cog(Admin(bot))