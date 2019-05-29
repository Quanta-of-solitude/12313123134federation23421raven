import discord
from discord.ext import commands

class Trader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["help"])
    async def about(self,ctx):
        '''help menu'''
        about = """**__Federation__**\nThe server bot! Looking after the server activities and AE specific commands!"""
        #helpm = "```\n1. +svrtime: To get the AE servertime.\n2. +gif [query]: Search gif.\n\nMore coming Later!\n\nPlus, Logging #gold-raven-sets 24/7 👍 and Stalking the member activities :3```"
        helpm = "For AQ3D Related stuff:\n`char`, `aqs`, `aq3ditem`\n\nFor AQW Related stuff:\n`aqwchar`, `aqwitem(bugged)`\n\nThere are serveral hidden commands :smile:\nLogging server 24/7!"

        em = discord.Embed(color = 0xffd500)
        em.set_thumbnail(url = self.bot.user.avatar_url)
        em.set_author(name = "About Federation:", icon_url = "https://image.ibb.co/bZ6yHx/profile.png")
        em.add_field(name = "Info:", value = about, inline = False)
        em.add_field(name = "Help:", value = helpm,inline = False)
        em.set_footer(text = "|Federation|",icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = em)




def setup(bot):
    bot.add_cog(Trader(bot))
