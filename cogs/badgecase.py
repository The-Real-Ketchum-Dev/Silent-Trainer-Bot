import os
import discord
import cogs.load_json
from .utils.dataIO import dataIO
from discord.ext import commands



class Pokemon:
    """Badge Cases"""

    def __init__(self, bot):
        self.bot = bot
        self.file_path = "data/badges/badges.json"
        self.json_data = dataIO.load_json(self.file_path)

    def savefile(self):
        dataIO.save_json("data/badges/badges.json", self.badges)

    @commands.command(invoke_without_command=True, pass_context=True)
    async def case(self,ctx,name: str):
        
        try:
            data = cogs.load_json.get_badge_info()
            data_bool = True
        except:
            data_bool = False
			
        if ctx.invoked_subcommand is None:
            await self.bot.say(" " + ctx.message.author.mention + "Your Badge Case is not ready yet")

    @commands.group(invoke_without_command=True, pass_context=True)
    async def badgecase(self,ctx,badge_name: str):
        
        try:
            data = cogs.load_json.get_badge_info()
            data_bool = True
        except:
            data_bool = False

        if ctx.invoked_subcommand is None:
            await self.bot.say("""Check if your spelling was correct""")

    @badgecase.command(pass_context=True)
    async def marsh(self,ctx):

        await self.bot.say(" " + ctx.message.author.mention + " We have successfully inserted the Marsh Badge into your Badge Case")


    @badgecase.command(pass_context=True)
    async def volcano(self,ctx):

        await self.bot.say(" " + ctx.message.author.mention + " We have successfully inserted the Volcano Badge into your Badge Case")


def check_folders(): # This is how you make your folder that will hold your data for your cog
    if not os.path.exists("data/badges"): # Checks if it exists first, if it does, then nothing executes
        print("Creating data/badges folder...")  # You can put what you want here. Prints in console for the owner
        os.makedirs("data/badges") # This makes the directory


def check_files(): # This is how you check if your file exists and let's you create it
    
    f = "data/badges/badges.json" # f is the path to the file
    if not dataIO.is_valid_json(f): # Checks if file in the specified path exists
        print("Creating default badges.json...") # Prints in console to let the user know we are making this file
        dataIO.save_json(f, system) # If you didn't use a default structure you could type: dataIO.save_json(f, {})


def setup(bot):
    check_folders() # runs the folder check on setup that way it exists before running the cog
    check_files() # runs the check files function to make sure the files you have exists
    n = Pokemon(bot)
    bot.add_cog(n)