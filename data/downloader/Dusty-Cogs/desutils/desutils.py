import discord
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils.menu import *
from __main__ import send_cmd_help, settings
from cogs.utils import checks
from random import choice
import os
import aiohttp

# weird because 0 indexing
numbs = {
    "1⃣": 0,
    "2⃣": 1,
    "3⃣": 2,
    "4⃣": 3,
    "5⃣": 4,
    "6⃣": 5,
    "7⃣": 6,
    "8⃣": 7,
    "9⃣": 8,
    "🔟": 9
}


class Desutils:
    def __init__(self, bot):
        self.bot = bot
        self.menu = Menu(bot)

    def _perms(self, ctx, perm):
        if ctx.message.author.id == settings.owner:
            return True

        ch = ctx.message.channel
        author = ctx.message.author
        resolved = ch.permissions_for(author)
        return resolved.perm

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def botinfo(self, ctx):
        _colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        _colour = int(_colour, 16)
        _creation_date = self.bot.user.created_at.strftime("%d %b %Y %H:%M")
        _usercount = len([x.bot for x in self.bot.get_all_members()])
        _servercount = len(self.bot.servers)
        _name = "{}#{}".format(self.bot.user.name,
                               self.bot.user.discriminator)

        e = discord.Embed(description="Bot statistics", colour=_colour)
        e.set_author(name=_name, icon_url=self.bot.user.avatar_url)
        e.add_field(name="User count", value=_usercount)
        e.add_field(name="Server count", value=_servercount)
        e.set_footer(text="Bot created on {}".format(_creation_date))

        try:
            await self.bot.say(embed=e)
        except discord.Forbidden:
            await self.bot.say("I don\'t have permission to send embeds here!")

    async def _prompt(self, ctx, msg: str):
        await self.bot.say(msg)
        msg = await self.bot.wait_for_message(author=ctx.message.author,
                                              channel=ctx.message.channel)
        return msg

    @commands.command(pass_context=True, no_pm=True)
    async def utilsmenu(self, ctx):
        cmds = ["Roles", "Send cog", "List cogs", "Perms"]
        cmd = ""
        cmd_msg = "Roles\nSend cog\nList cogs\nPerms"

        cmd = await self.menu.menu(ctx, 1, cmd_msg, cmds)

        if cmd == 1 and self._perms(ctx, 'manage_roles'):
            return await ctx.invoke(self.roles)

        if cmd == 2 and self._perms(ctx, 'manage_roles'):
            return await ctx.invoke(self.sendcog)

        if cmd == 3 and self._perms(ctx, 'manage_messages'):
            return await ctx.invoke(self.listcogs)

        if cmd == 4 and self._perms(ctx, 'manage_roles'):
            return await ctx.invoke(self.perms)

        if cmd is None:
            return await self.bot.say("Menu has expired.")

    @checks.mod_or_permissions(manage_roles=True)
    @commands.command(pass_context=True, no_pm=True)
    async def roles(self, ctx):
        roles = ""
        for x in ctx.message.server.roles:
            roles += ((str(x.name).ljust(30)) + str(x.id) + "\n")
        await self.bot.say("```{0}```".format(roles))

    @checks.is_owner()
    @commands.command(pass_context=True, no_pm=True)
    async def sendcog(self, ctx, cog=""):
        fp = ""
        if cog == "":
            fp = await self._prompt(ctx, "What cog do you want to send?")
            fp = "cogs/{0}.py".format(fp.content)
        else:
            fp = "cogs/{0}.py".format(cog)
        if os.path.exists(fp):
            await self.bot.send_file(ctx.message.channel, fp)
        else:
            await self.bot.say("Cog not found!")

    @checks.mod_or_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def pin(self, ctx, text: str, user: discord.User = None):
        """Pin a recent message, useful on mobile.

        Usage:
            pin word
            pin "More than one word"
            pin "More than one word but said by" @someone """
        channel = ctx.message.channel
        if not text:
            return await send_cmd_help(ctx)
        else:
            if user and text:
                async for x in self.bot.logs_from(channel):
                    if x.content.startswith(text) and x.author.id == user.id:
                        return await self.bot.pin_message(x)
            elif text:
                async for x in self.bot.logs_from(channel):
                    if x.content.startswith(text):
                        return await self.bot.pin_message(x)
            else:
                await self.bot.say("AAAAAAAAAAAAAAAA SOMETHING WENT WRONG THAT SHOULDN'T HAVE!!!!!!!")

    @checks.mod_or_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def unpin(self, ctx, text: str, user: discord.User = None):
        """Unpin a message pinned in the current channel.

        Usage is the same as the pin command"""

        channel = ctx.message.channel
        if not text:
            return await send_cmd_help(ctx)
        for x in (await self.bot.pins_from(channel)):
            if text and user:
                if x.content.startswith(text) and x.author == user:
                    return await self.bot.unpin_message(x)
            elif text and x.content.startswith(text):
                return await self.bot.unpin_message(x)

    async def prefixes(self, message):
        if message.content == "prefixes":
            server = message.server
            prefix_list = [x for x in self.bot.settings.prefixes]
            serverprefix_list = [x for x in self.bot.settings.get_server_prefixes(server)]
            msg = "```Global prefixes: {0}\n".format(', '.join(prefix_list))
            msg += "Server prefixes: {0}```".format(', '.join(serverprefix_list))
            await self.bot.send_message(message.channel, msg)

    @checks.is_owner()
    @commands.command(pass_context=True, no_pm=True)
    async def listcogs(self, ctx):
        """Shows the status of cogs.

        + means the cog is loaded
        - means the cog is unloaded
        ? means the cog couldn't be found(it was probably removed manually)"""

        all_cogs = dataIO.load_json("data/red/cogs.json")
        loaded, unloaded, other = ("",) * 3
        cogs = self.bot.cogs['Owner']._list_cogs()

        for x in all_cogs:
            if all_cogs.get(x):
                if x in cogs:
                    loaded += "+\t{0}\n".format(x.split('.')[1])
                else:
                    other += "?\t{0}\n".format(x.split('.')[1])
            elif x in cogs:
                unloaded += "-\t{0}\n".format(x.split('.')[1])
        msg = "```diff\n{0}{1}{2}```".format(loaded, unloaded, other)
        await self.bot.say(msg)

    @checks.is_owner()
    @commands.command(pass_context=True, no_pm=True)
    async def perms(self, ctx):
        user = await self._prompt(ctx, "What user?")
        try:
            if user.mentions is not None:
                user = user.mentions[0]
        except:
            try:
                user = discord.utils.get(ctx.message.server.members, name=str(user.content))
            except:
                return await self.bot.say("User not found!")
        perms = iter(ctx.message.channel.permissions_for(user))
        perms_we_have = "```diff\n"
        perms_we_dont = ""
        for x in perms:
            if "True" in str(x):
                perms_we_have += "+\t{0}\n".format(str(x).split('\'')[1])
            else:
                perms_we_dont += ("-\t{0}\n".format(str(x).split('\'')[1]))
        await self.bot.say("{0}{1}```".format(perms_we_have, perms_we_dont))


def setup(bot):
    n = Desutils(bot)
    bot.add_listener(n.prefixes, 'on_message')
    bot.add_cog(n)
