import discord
from discord.ext import commands

class Donation:
    """Donations to Silent Trainers Bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, pass_context=True)
    async def donate(self,ctx,institution):
        """Donations!"""
        if ctx.invoked_subcommand is None:
            await self.bot.say("Try another time")

    @donate.command(pass_context=True)
    async def silent_trainers(self,ctx):
        "Donate to Silent Trainers Bot"
        
        await self.bot.say("**__Donate Here__**\nhttps://paypal.me/ketchumamps\nDonate to Silent Trainers Bot Today!")
    

def setup(bot):
    bot.add_cog(Donation(bot))