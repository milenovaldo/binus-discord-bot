import discord, json
from discord.ext import commands
from random import randint
from time import sleep
from datetime import datetime

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.currentDate = datetime.now().strftime('%Y-%m-%d')
        self.currentTime = datetime.now().strftime('%H:%M:%S')

    def levelUpAnnouncement(self, mention, role):
        return f'{mention} have leveled up to {role}'
    
    '''
    Notifies us when the bot is ready to function.
    '''
    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f'Logged in as {self.bot.user} \n'+
            'Logging active'
            )
        await self.bot.change_presence(status = discord.Status.online, activity = discord.Game('!help v1.2'))   

    '''
    Creates an announcement when someone joins the server, sends
    the new member the rules of the server in private message, and
    adds their ID to the json.
    '''
    @commands.Cog.listener()
    async def on_member_join(self, member):
        #Announcement
        channel = self.bot.get_channel(635840445079093250)
        await channel.send(f'Please welcome {member.mention} to the server')
        #Rules messaging
        await member.send(
            f'Welcome to Binus Discord server \n' +
            f'Please read the rules below: \n' +
            f'1. Do not be annoying \n' +
            f'2. Do not send inflammatory messages in the server or to anyone in the server \n' +
            f'Breaking these rules will result in a perma ban.'
        )
        #Registering the new user to the json
        with open('json/userxp.json') as fp:
            users = json.load(fp)
        if str(member.id) not in users["users"]:
            users["users"].update({str(member.id): 0})
            with open('json/userxp.json', 'w') as fileToDump:
                json.dump(users, fileToDump, indent = 4)
        else:
            pass

    '''
    Creates an announcement when someone gets banned from the server
    and removed them from userxp.json
    '''
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        with open('json/userxp.json') as fp:
            users = json.load(fp)
        try:
            del users["users"][str(member.id)]
            with open('json/userxp.json', 'w') as fileToDump:
                json.dump(users, fileToDump, indent = 4)
        except KeyError:
            print('Key doesn\'t exist. Add member id manually to the json.')

    '''
    Creates an announcement when someone gets unbanned in the server
    '''
    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        channel = self.bot.get_channel(635840445079093250)
        await channel.send(f'User {member.mention} has been unbanned from the server', delete_after = 10)

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
        if str(message.author) in harassUserList:
            try:
                randNum = randint(0, len(harassmentResponses) - 1)
                await message.channel.send(f'{message.author.mention} {harassmentResponses[randNum]}')
                if randNum == 6:
                    sleep(5)
                    await message.channel.send(f'{message.author.mention} Sike, b*tch')
                else:
                    pass
            except IndexError:
                print('Harassment response empty. Fill in the "harassmentreponses.txt"')
        '''
        Level up system
        adds experience points every time a user sends a message
        in the server
        '''
        try:
            with open('json/userxp.json') as fp:
                users = json.load(fp)
            users['users'][str(message.author.id)] += 1
            with open('json/userxp.json', 'w') as fileToDump:
                json.dump(users, fileToDump, indent = 4)
            authorXP = users['users'][str(message.author.id)]
            if authorXP == 10:
                role = discord.utils.get(message.guild.roles, id = 638181731794681866)
                await message.author.add_roles(role)
                await message.channel.send(self.levelUpAnnouncement(message.author.mention, role.name))
            elif authorXP == 30:
                role = discord.utils.get(message.guild.roles, id = 638181995909873694)
                await message.author.add_roles(role)
                await message.channel.send(self.levelUpAnnouncement(message.author.mention, role.name))
            elif authorXP == 90:
                role = discord.utils.get(message.guild.roles, id = 638182182136840202)
                await message.author.add_roles(role)
                await message.channel.send(self.levelUpAnnouncement(message.author.mention, role.name))
            elif authorXP == 270:
                role = discord.utils.get(message.guild.roles, id = 638182260264403024)
                await message.author.add_roles(role)
                await message.channel.send(self.levelUpAnnouncement(message.author.mention, role.name))
            elif authorXP == 810:
                role = discord.utils.get(message.guild.roles, id = 638182302408769571)
                await message.author.add_roles(role)
                await message.channel.send(self.levelUpAnnouncement(message.author.mention, role.name))
        except:
            pass

        '''
        This block of code sends a motivational message 
        to encourage you to get a girlfriend/boyfriend 
        if the bot receives a Direct Message from anyone.
        '''
        if message.channel.type == discord.ChannelType.private:
            DMresponses = [
                'Get a girlfriend bro (or boyfriend).',
                'I have a boyfriend',
                'I\'m already committed to someone. Find someone else.'
            ]
            await message.author.send(DMresponses[randint(0, len(DMresponses) - 1)])
            return
        else:
            pass

        '''
        Logs all the messages sent.
        '''
        log = f'{message.channel}: ({self.currentTime}) {message.author}: {message.content}'
        print(log)
        with open(f'logs/{self.currentDate}.txt', 'a') as fpAppend:
            fpAppend.write(f'{log}\n')


'''
Sets up the bot object as a cog
'''
def setup(bot):
    bot.add_cog(Listener(bot))
