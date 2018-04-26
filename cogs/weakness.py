import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


class Pokemon:
    """Weaknesses & More"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, pass_context=True)
    async def gen_1(self,ctx,pokemon):
        
        if ctx.invoked_subcommand is None:
            await self.bot.say("""**__Error__**: You have either selected to incorrect Pokemon name or you used a capital letter. Please Try Again""")

    @gen_1.command(pass_context=True)
    async def bulbasaur(self,ctx):
        
        author = "Bulbasaur"
        description = ("#001")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0x0FF00, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/434542722121203712/437347577415860224/bulbasaur.gif")
        embed.title = "Pokedex Entry"
        embed.set_author(name="Bulbasaur", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Types", value="<:grasstype:437249725796712468> <:poisontype:437249726790893578>")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.add_field(name="HP", value="45")
        embed.add_field(name="Attack", value="49")
        embed.add_field(name="Defense", value="49")
        embed.add_field(name="Sp. Attack", value="65")
        embed.add_field(name="Sp. Defense", value="65")
        embed.add_field(name="Speed", value="45")
        embed.add_field(name="Evolutions", value="#002 Ivysaur | #003 Venusaur")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def ivysaur(self):
        
        author = "Ivysaur"
        description = ("#002")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0x0FF00, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338042911528583170/437357991814234122/ivysaur.gif")
        embed.title = "Pokedex Entry"
        embed.set_author(name="Ivysaur", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Types", value="<:grasstype:437249725796712468> <:poisontype:437249726790893578>")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.add_field(name="HP", value="60")
        embed.add_field(name="Attack", value="62")
        embed.add_field(name="Defense", value="63")
        embed.add_field(name="Sp. Attack", value="80")
        embed.add_field(name="Sp. Defense", value="80")
        embed.add_field(name="Speed", value="60")
        embed.add_field(name="Evolutions", value="#001 Bulbasaur | #003 Venusaur")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def venusaur(self):
        
        author = "Venusaur"
        description = ("#003")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0x0FF00, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338042911528583170/437358055743815680/venusaur.gif")
        embed.title = "Pokedex Entry"
        embed.set_author(name="Venusaur", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Types", value="<:grasstype:437249725796712468> <:poisontype:437249726790893578>")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.add_field(name="HP", value="80")
        embed.add_field(name="Attack", value="82")
        embed.add_field(name="Defense", value="83")
        embed.add_field(name="Sp. Attack", value="100")
        embed.add_field(name="Sp. Defense", value="100")
        embed.add_field(name="Speed", value="80")
        embed.add_field(name="Evolutions", value="#001 Bulbasaur | #002 Ivysaur")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		
    
    @gen_1.command()
    async def charmander(self):
        
        author = "Charmander"
        description = ("#004")
        field_name = "Weakness"
        field_contents = "<:watertype:437249726476189698> <:ground:437249726400823316> <:rocktype:437249726698618880>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338042911528583170/437358967853678592/charmander.gif")
        embed.title = "Pokedex Entry"
        embed.add_field(name="Types", value="<:firetype:437249724538683393>")
        embed.set_author(name="Charmander", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:watertype:437249726476189698> <:ground:437249726400823316> <:rocktype:437249726698618880>")  # Can add multiple fields.
        embed.add_field(name="HP", value="39")
        embed.add_field(name="Attack", value="52")
        embed.add_field(name="Defense", value="43")
        embed.add_field(name="Sp. Attack", value="60")
        embed.add_field(name="Sp. Defense", value="50")
        embed.add_field(name="Speed", value="65")
        embed.add_field(name="Evolutions", value="#005 Charmeleon | #006 Charizard")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def charmeleon(self):
        
        author = "Charmeleon"
        description = ("#005")
        field_name = "Weakness"
        field_contents = "<:watertype:437249726476189698> <:ground:437249726400823316> <:rocktype:437249726698618880>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338042911528583170/437359639315742740/charmeleon.gif")
        embed.title = "Pokedex Entry"
        embed.add_field(name="Types", value="<:firetype:437249724538683393>")
        embed.set_author(name="Charmeleon", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:watertype:437249726476189698> <:ground:437249726400823316> <:rocktype:437249726698618880>")  # Can add multiple fields.
        embed.add_field(name="HP", value="58")
        embed.add_field(name="Attack", value="64")
        embed.add_field(name="Defense", value="58")
        embed.add_field(name="Sp. Attack", value="80")
        embed.add_field(name="Sp. Defense", value="65")
        embed.add_field(name="Speed", value="80")
        embed.add_field(name="Evolutions", value="#004 Charmander | #006 Charizard")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def charizard(self):
        
        author = "Charizard"
        description = ("#006")
        field_name = "Weakness"
        field_contents = "<:watertype:437249726476189698> <:rocktype:437249726698618880> <:electrictype:437249725264166912>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437364888562696203/charizard.gif")
        embed.title = "Pokedex Entry"
        embed.add_field(name="Types", value="<:firetype:437249724538683393> <:flyingtype:437249725658431490>")
        embed.set_author(name="Charizard", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:watertype:437249726476189698> <:rocktype:437249726698618880> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.add_field(name="HP", value="78")
        embed.add_field(name="Attack", value="84")
        embed.add_field(name="Defense", value="78")
        embed.add_field(name="Sp. Attack", value="109")
        embed.add_field(name="Sp. Defense", value="85")
        embed.add_field(name="Speed", value="100")
        embed.add_field(name="Evolutions", value="#004 Charmander | #005 Charmeleon")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)


    @gen_1.command()
    async def squirtle(self):
        
        author = "Squirtle"
        description = ("#007")
        field_name = "Weakness"
        field_contents = "<:grasstype:437249725796712468> <:electrictype:437249725264166912>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0x000FF, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437369728688848896/squirtle.png")
        embed.title = "Pokedex Entry"
        embed.add_field(name="Types", value="<:watertype:437249726476189698>")
        embed.set_author(name="Squirtle", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:grasstype:437249725796712468> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.add_field(name="HP", value="44")
        embed.add_field(name="Attack", value="48")
        embed.add_field(name="Defense", value="65")
        embed.add_field(name="Sp. Attack", value="50")
        embed.add_field(name="Sp. Defense", value="64")
        embed.add_field(name="Speed", value="43")
        embed.add_field(name="Evolutions", value="#008 Wartortle | #009 Blastoise")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def wartortle(self):
        
        author = "Wartortle"
        description = ("#008")
        field_name = "Weakness"
        field_contents = "<:grasstype:437249725796712468> <:electrictype:437249725264166912>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0x000FF, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437367249427365889/wartortle.gif")
        embed.title = "Pokedex Entry"
        embed.add_field(name="Types", value="<:watertype:437249726476189698>")
        embed.set_author(name="Wartortle", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:grasstype:437249725796712468> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.add_field(name="HP", value="59")
        embed.add_field(name="Attack", value="63")
        embed.add_field(name="Defense", value="80")
        embed.add_field(name="Sp. Attack", value="65")
        embed.add_field(name="Sp. Defense", value="80")
        embed.add_field(name="Speed", value="58")
        embed.add_field(name="Evolutions", value="#007 Squirtle | #009 Blastoise")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def blastoise(self):
        
        author = "Blastoise"
        description = ("#009")
        field_name = "Weakness"
        field_contents = "<:grasstype:437249725796712468> <:electrictype:437249725264166912>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0x000FF, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437371179683020811/blastoise.gif")
        embed.title = "Pokedex Entry"
        embed.add_field(name="Types", value="<:watertype:437249726476189698>")
        embed.set_author(name="Blastoise", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:grasstype:437249725796712468> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.add_field(name="HP", value="79")
        embed.add_field(name="Attack", value="83")
        embed.add_field(name="Defense", value="100")
        embed.add_field(name="Sp. Attack", value="85")
        embed.add_field(name="Sp. Defense", value="105")
        embed.add_field(name="Speed", value="78")
        embed.add_field(name="Evolutions", value="#007 Squirtle | #008 Wartortle")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		
def setup(bot):
    bot.add_cog(Pokemon(bot))

