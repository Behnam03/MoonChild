import discord
from discord.ext import commands

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="clickme", style=discord.ButtonStyle.blurple)
    async def my_butten(self, interaction: discord.interactions, button: discord.ui.Button):
        await interaction.response.send_message("you clicked me!", ephemeral=True)


class Clickme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def click(self, ctx):
        await ctx.send("Message with a button", view=Buttons())


async def setup(bot):
    await bot.add_cog(Clickme(bot))