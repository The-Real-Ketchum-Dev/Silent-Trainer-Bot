import sys
from discord.ext import commands
import discord
import cogs.load_json

class Pokedex():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def pokedex(self,ctx, *, pkmn_name : str):
        """Get the stats of a Pokemon!"""
        pkmn_name = pkmn_name.lower()

        try:
            data = cogs.load_json.get_poke_info()
            data_bool = True
        except:
            data_bool = False

        if pkmn_name[0:4] == "tapu":
            poke_ico_name_set = True
            if pkmn_name[5:] == "koko":
                poke_ico_name = "tapu_koko"
                pkmn_name = "tapukoko"
            elif pkmn_name[5:] == "bulu":
                poke_ico_name = "tapu_bulu"
                pkmn_name = "tapubulu"
            elif pkmn_name[5:] == "fini":
                poke_ico_name = "tapu_fini"
                pkmn_name = "tapufini"
            elif pkmn_name[5:] == "lele":
                poke_ico_name = "tapu_lele"
                pkmn_name = "tapulele"
        else:
            poke_ico_name_set = False

        if pkmn_name[0:4] == "type":
            poke_ico_name_set = True
            poke_ico_name = "type_null"
            pkmn_name = "typenull"
            
        pkmn_name_capt = pkmn_name.title()
        try:
            subdata = data[pkmn_name]
        except:
            await self.bot.say("The pokemon you searched for doesn't exist or you may have wrongly spelt the name.")
            return 0

        type_one = subdata['types'][0]
        type_one = type_one.title()

        ability_prim = subdata['abilities']['primary']
        ability_prim = ability_prim.title()

        try:
            ability_hidden = subdata['abilities']['hidden']
            ability_hidden = ability_hidden.title()
            ability_final = "Hidden : " + ability_hidden + "\n" + "Primary : " + ability_prim
        except:
            ability_hidden = "No Hidden Ability"
            ability_final = "Hidden : " + ability_hidden + "\n" + "Primary : " + ability_prim
            
        try:
            type_two = subdata['types'][1]
            type_two = type_two.title()
            type_final = type_one + ', ' + type_two

        except:
            type_final = type_one
            pass
        if not poke_ico_name_set:
            poke_ico_name = pkmn_name.lower()
            poke_ico_name = poke_ico_name.replace(" ", "_")
        poke_ico_url = "http://smogon.com/dex/media/sprites/xy/" + poke_ico_name + ".gif"
        send_data = discord.Embed(title=pkmn_name_capt, description='***Information***', colour=0x4499E7)
        send_data.set_image(url=poke_ico_url)
        send_data.set_author(name='Pokedex', icon_url=poke_ico_url)
        send_data.add_field(name="Attack", value=subdata['stats']['atk'], inline=True)
        send_data.add_field(name="Special Attack", value=subdata['stats']['spa'], inline=True)
        send_data.add_field(name="Defense", value=subdata['stats']['def'], inline=True)
        send_data.add_field(name="Special Defense", value=subdata['stats']['spd'], inline=True)
        send_data.add_field(name="HP", value=subdata['stats']['hp'], inline=True)
        send_data.add_field(name="Speed", value=subdata['stats']['spe'], inline=True)
        send_data.add_field(name="Types", value=type_final, inline=True)
        send_data.add_field(name="Abilities", value=ability_final, inline=True)
        send_data.add_field(name="Base Experience", value=subdata['base_exp'], inline=True)
        send_data.add_field(name="Base Friendship", value=subdata['base_friendship'], inline=True)
        await self.bot.say(embed=send_data)
        
def setup(bot):
    bot.add_cog(Pokedex(bot))