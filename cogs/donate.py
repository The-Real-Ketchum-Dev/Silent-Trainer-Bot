import discord
from discord.ext import commands

class Donation:
    """Gives the link to KetchumMaps donation page."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=False)
    async def donate(self):
        """Gives the link to KetchumMaps donation page."""
        await self.bot.say("**__PayPal__**\nhttp://www.paypal.me/ketchumamps\nDonate to help us continue our vission")

def setup(bot):
    bot.add_cog(Donation(bot))