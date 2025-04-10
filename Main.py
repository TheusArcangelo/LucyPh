import discord
from discord import app_commands

class lucyph(discord.Client):

    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="!",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"The {self.user} was successfully connected")

bot = lucyph()

@bot.tree.command(name="hello", description="first command")
async def hello(interaction:discord.Interaction):
    await interaction.response.send_message(f"Hi {interaction.user.mention}!")


bot.tree.command(name="soma", description="Uma soma que o bot ira resolver")
async def sooma(interaction:discord.Interaction,numero1:int,numero2:int):
    numero_somado = numero1 + numero2
    await interaction.response.send_message(f"O numero somado é {numero_somado}.)

bot.run(You Token)
