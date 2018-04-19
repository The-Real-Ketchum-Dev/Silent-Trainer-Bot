import discord
from discord.ext import commands


class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def volcano(self, mention):
        """<mention> the user who won\n<badge> the badge that has been won"""

        # Command function
        await self.bot.say("Great Battle Trainers!! This Trainer has won the Volcano Badge! <@&434302715691270144>")

    @commands.command()
    async def thunder(self, mention):
        """<mention> the user who won\n<badge> the badge that has been won"""

        # Command function
        await self.bot.say("Great Battle Trainers!! This Trainer has won the Thunder Badge! <@&434302715691270144>")

    @commands.command()
    async def earth(self, mention):
        """<mention> the user who won\n<badge> the badge that has been won"""

        # Command function
        await self.bot.say("Great Battle Trainers!! This Trainer has won the Earth Badge! <@&434302715691270144>")

    @commands.command()
    async def marsh(self, mention):
        """<mention> the user who won\n<badge> the badge that has been won"""

        # Command function
        await self.bot.say("Great Battle Trainers!! This Trainer has won the Marsh Badge! <@&434302715691270144>")

    @commands.command()
    async def soul(self, mention):
        """<mention> the user who won\n<badge> the badge that has been won"""

        # Command function
        await self.bot.say("Great Battle Trainers!! This Trainer has won the Soul Badge! <@&434302715691270144>")

    @commands.command()
    async def rainbow(self, mention):
        """<mention> the user who won\n<badge> the badge that has been won"""

        # Command function
        await self.bot.say("Great Battle Trainers!! This Trainer has won the Rainbow Badge! <@&434302715691270144>")

    @commands.command()
    async def cascade(self, mention):
        """<mention> the user who won\n<badge> the badge that has been won"""

        # Command function
        await self.bot.say("Great Battle Trainers!! This Trainer has won the Cascade Badge! <@&434302715691270144>")

    @commands.command()
    async def boulder(self, mention):
        """<mention> the user who won\n<badge> the badge that has been won"""

        # Command function
        await self.bot.say("Great Battle Trainers!! This Trainer has won the Boulder Badge! <@&434302715691270144>")

    @commands.command()
    async def badges(self):
        """Shows the badges"""

        # Command function
        await self.bot.say("```Boulder = Pewter Gym\nCascade = Cerulean Gym\nThunder = Vermilion Gym\nRainbow = Celadon Gym\nSoul = Fuchsia Gym\nMarsh = Saffron Gym\nVolcano = Cinnabar Gym\nEarth = Viridian Gym```")

    @commands.command()
    async def gymleaders(self):
        """Shows the badges"""

        # Command function
        await self.bot.say("**__Pewter Gym__** = *NONE*\n**__Cerulean Gym__** = <@265565197496745984>\n**__Vermilion Gym__** = <@410795571771605004>\n**__Celadon Gym__** = <@360828289561919500>\n**__Fuchsia Gym__** = <@387129129004302336>\n**__Saffron Gym__** = <@336707358505959432>\n**__Cinnabar Gym__** = <@236856961478557696>\n**__Viridian Gym__** = <@335289862674579461>")

    @commands.command()
    async def commands(self):
        """Shows the badges"""

        # Command function
        await self.bot.say("**$mystic** | Join mystic with this command\n**$valor** | Join valor with this command\n**$instinct** | Join instinct with this command\n**$team** | Join the team\n**$<badge> <mention>** | Gym Leaders ONLY\n**$elite4** | Self explanitory\n**$pokeleague** | Another common sense thing\n**$tournaments** | COMING SOON\n**$pokehelp** | Use this for your everyday commands\n**$helpme** | Get help")


def setup(bot):
    bot.add_cog(Mycog(bot))
