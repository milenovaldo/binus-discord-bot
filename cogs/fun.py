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
        with open('txt/steamapi.txt', 'r') as fp:
            apikey = fp.readline()

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

        embed = discord.Embed(title = 'Gamer Flex')
        embed.set_thumbnail(url = steamUser['avatarfull'])
        embed.add_field(name = steamUser["personaname"], value = f'Total hours played: **{round(totalMinutes/60)}**')
        await ctx.channel.send(content=None, embed = embed)


def setup(bot):
    bot.add_cog(Fun(bot))
