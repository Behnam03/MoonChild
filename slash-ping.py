import discord

from discord.ext import commands
from discord import Interaction
from discord import app_commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # slash command
    @app_commands.command(name="ping", description="mige Salam")
    async def pingS(self, ctx: Interaction):
     await ctx.response.send_message("Hi, Mooni!") #use ephemral=True to make it that just the person who is using can only see it.


async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add.cog(Ping(bot))
    else:
        await bot.add_cog(
            Ping(bot),
            guild=discord.Object(id=bot.config["test-server-id"])
        )