import discord
from discord.ext import commands

class Donation:
    """Gives the link to KetchumMaps donation page."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=False)
    async def elite4(self):
        """Gives the link to KetchumMaps donation page."""
        await self.bot.say("```COMING SOON```")
    
    @commands.command()
    async def pokeleague(self):
        """Shows the badges"""

        # Command function
        await self.bot.say("```COMING SOON```")

    @commands.command()
    async def tournaments(self):
        """Shows the badges"""

        # Command function
        await self.bot.say("```COMING SOON```")

    @commands.command()
    async def helpme(self):
        """Shows the badges"""

        # Command function
        await self.bot.say("Before asking for help please refer to <#434304246276685825> or <#433740903027572736>\nIf you did not find your answer there then proceed to ask your question. **Do not DM any Mods at any time unless approved before hand**.")


def setup(bot):
    bot.add_cog(Donation(bot))