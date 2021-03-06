import discord
from discord.ext import commands
import urllib.request
import json

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    This command sends an API request to steam
    and respond with data about the specified steam account
    '''
    @commands.command(aliases = ['hourswasted', 'getdisappointed', 'steam', 'gamerflex'])
    async def steamhours(self, ctx, steamid):
        with open('json/data.json', 'r') as fp:
            self.idJson = json.load(fp)

        apikey = str(self.idJson["KEY"]["steamAPI"])

        steamAPIURL = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={apikey}&steamid={steamid}&include_played_free_games=False'
        steamAPIUsrURL = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={apikey}&steamids={steamid}'
        totalMinutes = 0

        with urllib.request.urlopen(steamAPIUsrURL) as userurl:
            response = json.loads(userurl.read().decode())
            steamUser = response['response']['players'][0]
            
        with urllib.request.urlopen(steamAPIURL) as url:
            data = json.loads(url.read().decode())
            for game in data['response']['games']:
                totalMinutes += game['playtime_forever']

        embed = discord.Embed(title = steamUser["personaname"], colour = 0x0080ff)
        embed.set_thumbnail(url = steamUser['avatarfull'])
        embed.add_field(name = 'Total hours played:', value = f' **{round(totalMinutes/60)}**', inline = True)
        embed.add_field(name = 'Games owned: ', value = f'**{data["response"]["game_count"]}**')

        await ctx.channel.send(content=None, embed = embed)

    '''
    Sends a message of the list of commands available to the users
    '''
    @commands.command(aliases = ['tolong'])
    async def help(self, ctx):
        embed = discord.Embed(title = 'Help', description = 'Help means tolong. It means you minta tolong', colour = 0x0080ff)
        embed.set_thumbnail(url = 'https://image.psikolif.com/wp-content/uploads/2018/10/Logo-Binus-University-Universitas-Bina-Nusantara-PNG.png')
        embed.add_field(name = '!ping', value = 'Returns the latency of the bot to the server', inline = False)
        embed.add_field(name = '!clear/!clr <integer>', value = 'Clears the past <integer> messages', inline = False)
        embed.add_field(name = '!announce/!broadcast <message>', value = 'Creates a server wide announcement containing <message>', inline = False)
        embed.add_field(name = '!kick <mentionuser> <reason:optional>', value = 'Kicks a mentioned user', inline = False)
        embed.add_field(name = '!ban <mentionuser> <reason:optional>', value = 'Bans a mentioned user', inline = False)
        embed.add_field(name = '!harass <mentionuser(can be multiple users)>', value = 'Makes the bot harass the mentioned user forever', inline = False)
        embed.add_field(name = '!gamerflex/!steam <steamID64>', value = 'You\'ll either be proud or disappointed', inline = False)
        embed.add_field(name = '!play <songname/link>', value = 'Plays music of your choosing. Accepts song name or any url as parameter', inline = False)
        embed.add_field(name = '!skip', value = 'skips the music that is currently playing', inline = False)
        embed.add_field(name = '!np/!current/!playing', value = 'Shows the song title that is currently playing', inline = False)
        embed.add_field(name = '!queue/!q', value = 'Lists the upcoming songs that will be played', inline = False)
        embed.add_field(name = '!save', value = 'Saves the music that the bot is currently playing', inline = False)
        embed.add_field(name = '!library', value = 'See the list of songs saved to your library', inline = False)
        embed.add_field(name = '!playfromlibrary/!pfl <index>', value = 'Plays music from <index> of your music library', inline = False)
        embed.add_field(name = '!removesong/!rm/!rs <index>', value = 'Removes song in <index> from your music library', inline = False)
        await ctx.author.send(content = None, embed = embed)


def setup(bot):
    bot.add_cog(Fun(bot))
