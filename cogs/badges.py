import discord
from discord.ext import commands


class Gyms:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(invoke_without_command=True, pass_context=True, no_pm=True)
    async def badge(self, ctx, badge_name: str, user: discord.Member=None):
        """Gives a role to a user. 
        
        If <user> is not specified, it gives the role to whoever invoked the command."""
        author = ctx.message.author
        server = author.server
        if user is None:
            user = author
        role = discord.utils.get(server.roles, name=badge_name)
        if role is not None:
            if role not in user.roles and (author.top_role > role or author == server.owner):
                try:
                    await self.bot.add_roles(user, role)
                    await self.bot.say(" " + ctx.message.author.mention + "The {} Badge has been given to {}.".format(role.name, user.mention))
                except discord.errors.Forbidden:
                    await self.bot.say("I do not have permission to add the {} Badge.".format(role.name))
            elif author.top_role <= role and author != server.owner:
                await self.bot.say("You do not have permission to give the {} Badge.".format(role.name))
            else:
                await self.bot.say(" " + ctx.message.author.mention + "{} already has the {} Badge.".format(user.display_name, role.name))
        else:
            await self.bot.say("The `{}` role does not exist. Remember role names are case-sensitive.\n".format(role_name) +
                               "If the role name is more than one word surround it with `\'` or `\"`.")
    @commands.command()
    async def vermilion(self, gym):
        """The Vermilion Gym and its details"""
		
        # Command function
        await self.bot.say("**__Gym__**: Vermilion Gym\n**__Gym Leader__**: <@410795571771605004>\n**__Badge__**: <:thunderbadge:436621413324029952>")

    @commands.command()
    async def viridian(self, gym):
        """The Viridian Gym and its details"""
		
        # Command function
        await self.bot.say("**__Gym__**: Viridian Gym\n**__Gym Leader__**: <@335289862674579461>\n**__Badge__**: <:earthbadge:436357400950341633>")

    @commands.command()
    async def saffron(self, gym):
        """The Saffron Gym and its details"""
		
        # Command function
        await self.bot.say("**__Gym__**: Saffron Gym\n**__Gym Leader__**: <@336707358505959432>\n**__Badge__**: <:marshbadge:436359110989053962>")

    @commands.command()
    async def fuchsia(self, gym):
        """The Fuchsia Gym and its details"""
		
        # Command function
        await self.bot.say("**__Gym__**: Fuchsia Gym\n**__Gym Leader__**: <@387129129004302336>\n**__Badge__**: <:soulbadge:436620195205873664>")

    @commands.command()
    async def celadon(self, gym):
        """The Celadon Gym and its details"""
		
        # Command function
        await self.bot.say("**__Gym__**: Celedon Gym\n**__Gym Leader__**: <@360828289561919500>\n**__Badge__**: <:rainbowbadge:436356068881203212>")

    @commands.command()
    async def cerulean(self, gym):
        """The Cerulean Gym and its details"""
		
        # Command function
        await self.bot.say("**__Gym__**: Cerulean Gym\n**__Gym Leader__**: <@265565197496745984>\n**__Badge__**: <:cascadebadge:436619728388096001>")

    @commands.command()
    async def pewter(self, gym):
        """The Pewter Gym and its details"""
		
        # Command function
        await self.bot.say("**__Gym__**: Pewter Gym\n**__Gym Leader__**: <@256621201592418305>\n**__Badge__**: <:boulderbadge:436618870531424257>")

    @commands.command()
    async def badges(self):
        """Shows the badges"""

        # Command function
        await self.bot.say("`Kanto Region`\n\nBoulder Badge: <:boulderbadge:436618870531424257>\nCascade Badge: <:cascadebadge:436619728388096001>\nThunder Badge: <:thunderbadge:436621413324029952>\nRainbow Badge: <:rainbowbadge:436356068881203212>\nSoul Badge: <:soulbadge:436620195205873664>\nMarsh Badge: <:marshbadge:436359110989053962>\nVolcano Badge: <:volcanobadge:436351091337330698>\nEarth Badge: <:earthbadge:436357400950341633>\n \n`Johto Region`\n\n**COMING SOON**")
    
    @commands.command(pass_context=True)
    async def gym(self,ctx, rules):
        """Rules of battles here"""

        # Command function
        await self.bot.say(" " + ctx.message.author.mention + "\n**__HOW TO GET A GYM BADGE__**\n-Battle the gym leader of the badge you want!\n-There will be 3 battles to decide the winner.\n-You can use the gym type weakness only once and if you do you must win all three battles.\n-No legendary can be used.\n-please be patience as Gym leaders are not on 24-7\n-Cooldown time of 12 hours to rechallenge a gym leader\n-No repeating a Pokemon  (you can use 3 different Pidgeys e.g.)\n\n**__HOW TO BECOME A GYM LEADER__**\n-Must have all gym badges\n-Can only challenge for a Gym leader positions during Gym Challenge week.\n-Best out of 3\n-Must use Gym type in battle.\n-No legendary(edited)\n\n**__ELITE 4 AND POKEMON CHAMPION__**\n-must have all the Gym Badges to challenge the elite 4\n-If you chose to challenge the elite 4 you must give up your Gym Leader position.\n-must beat all elite 4 to be able to challenge the Pokemon champion.\n-If you beat any one of the elite 4 you can stop there and take there spot in the elite 4 but if at any point you lose you must start over.\n-You can only challenge the elite 4 and the Pokemon champion during Champion week.\n-Best out of 3 for each duel.\n-In all elite 4 and Pokemon champion duels Legendary Pokemon are allowed and you may use any Pokemon type.\n\n**__GYM CHALLENGE WEEK__**\nMore info soon...\n\n**__CHAMPION WEEK__**\nMore info soon...")

    @commands.command(pass_context=True)
    async def commands(self,ctx):
        """Shows the badges"""

        # Command function
        await self.bot.say(" " + ctx.message.author.mention + "\n**$mystic** | Join mystic with this command\n**$valor** | Join valor with this command\n**$instinct** | Join instinct with this command\n**$team** | Join the team\n**$<gym_name>** <type in gym>\n**$badges** | Shows all badges of Pokemon\n**$elite4** | Self explanitory\n**$pokeleague** | Another common sense thing\n**$tournaments** | COMING SOON\n**$pokehelp** | Use this for your everyday commands\n**$helpme** | Get help")


def setup(bot):
    bot.add_cog(Gyms(bot))
