import json
import discord
from pathlib import Path
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self, config):
        super().__init__(
            command_prefix="-",
            help_command=None,
            intents=discord.Intents.all(),
            application_id=config["application-id"]
        )

        self.config = config

    async def setup_hook(self):
        for file in Path("cogs").glob("*.py"):
            cog_name = file.name.split(".")[0]
            await self.load_extension(f"cogs.{cog_name}")
            print("Loaded extension:", file.name)

            if self.config["test-server-id"] == "":
                await self.tree.sync()
            else:
                await self.tree.sync(guild=discord.Object(id=self.config["test-server-id"]))

    async def on_ready(self):
        print("Bot is ready")
        await self.change_presence(activity=discord.Activity(name="MoonChild"))

if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    bot = Bot(config)
    bot.run(config["token"])
