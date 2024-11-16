import discord, json

from discord.ext import commands


class advertise(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(advertise(bot))
