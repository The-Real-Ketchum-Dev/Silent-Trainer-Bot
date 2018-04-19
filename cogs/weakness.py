import discord
from discord.ext import commands


class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weaknesschart(self):
        """<mention> the user who won\n<badge> the badge that has been won"""

        # Command function
        await self.bot.say("https://cdn.discordapp.com/attachments/350451958227795979/436286384274407438/vnstODV.jpg")

    
def setup(bot):
    bot.add_cog(Mycog(bot))
