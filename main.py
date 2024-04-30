# Libraries
import os
import discord
import datetime
import time
import asyncio
import random
import typing

from discord.ext import commands
from discord import ui
from discord import app_commands

from keep_alive import keep_alive
keep_alive()

# Setup
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = "/",
            intents = discord.Intents.all(),
            case_insensitive = True,
            help_command = None
        )
        self.start_time = time.time()

    async def setup_hook(self) -> None:
        await self.tree.sync()

    async def on_ready(self):
        print(f"Synced slash commands for {self.user} with prefix /")
        print(f"Invite Link: https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=412317240384&scope=bot")

        await bot.change_presence(
            activity = discord.Activity(
                name = game_name,
                type = discord.ActivityType.playing
            ),
            status = discord.Status.online
        )

    async def on_error(self, error) -> None:
        print(error)

    def uptime(self):
        current_time = time.time()
        difference = int(round(current_time - self.start_time))
        uptime = datetime.timedelta(seconds = difference)
        return uptime

# Variables
bot = Bot() # Set up the bot
TOKEN = os.getenv('TOKEN') # Bot Token

# Credit
color = 0x6daa41
game_name = "High Realms"
game_url = "https://www.roblox.com/groups/33438142"
game_icon = "https://media.discordapp.net/attachments/1180618436972396545/1230828028024717312/HighRealms_Isles_Icon-1_500x500.png?ex=6634bced&is=662247ed&hm=4fad82fdb54e00c6abefaa243f1f931d61cd0db89d318d48a4d4b4d0195c536d&=&format=webp&quality=lossless"

# Types
CategoryType = {
    "Building Blocks": "Building Blocks", # CategoryType["Building Blocks"]
    "Colored Blocks": "Colored Blocks", # CategoryType["Colored Blocks"]
    "Natural Blocks": "Natural Blocks", # CategoryType["Natural Blocks"]
    "Functional Blocks": "Functional Blocks", # CategoryType["Functional Blocks"]
    "Bluestone Blocks": "Bluestone Blocks" # CategoryType["Bluestone Blocks"]
}

ToolType = {
    "Axe": "<:Tool_Axe_1:1234343714852438047><:Tool_Axe_2:1234343717049991198><:Tool_Axe_3:1234343712482660463>", # ToolType["Axe"]
    "Pickaxe": "<:Tool_Pickaxe_1:1234343929458069625><:Tool_Pickaxe_2:1234343931353763903><:Tool_Pickaxe_3:1234343934688235652><:Tool_Pickaxe_4:1234343927411245117>", # ToolType["Pickaxe"]
    "Shovel": "<:Tool_Shovel1:1234344053018202142><:Tool_Shovel2:1234344055207493684><:Tool_Shovel_3:1234344047234121768><:Tool_Shovel4:1234344050501353522>" # ToolType["Shovel"]
}

# Lists & Dictionaries
block_list = typing.Literal[
    "Bluestone Block",
    "Cobalt Block",
    "Cobblestone",
    "Diamond Block",
    "Dirt",
    "Gold Ore",
    "Grass Block",
    "Iron Ore",
    "Mangrove Log",
    "Mangrove Planks",
    "Mangrove Slab",
    "Mangrove Stairs",
    "Oak Leaves",
    "Oak Log",
    "Oak Planks",
    "Oak Slab",
    "Oak Stairs",
    "Ruby Block",
    "Sapphire Ore",
    "Stone Brick Slab",
    "Stone Brick Stairs",
    "Stone Brick Wall",
    "Stone Bricks"
]

block_dict = {
    "Bluestone Block": {
        "description": "",
        "category": CategoryType["Bluestone Blocks"],
        "tool": ToolType["Pickaxe"]
    },

    "Cobalt Block": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Pickaxe"]
    },

    "Cobblestone": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Pickaxe"]
    },

    "Diamond Block": {
        "description": "A **Diamond Block** is a rare mineral block created by using nine diamonds that can be found in **the Mines**.",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Pickaxe"]
    },

    "Dirt": {
        "description": "",
        "category": CategoryType["Natural Blocks"],
        "tool": ToolType["Shovel"]
    },

    "Gold Ore": {
        "description": "",
        "category": CategoryType["Natural Blocks"],
        "tool": ToolType["Pickaxe"]
    },

    "Grass Block": {
        "description": "",
        "category": CategoryType["Natural Blocks"],
        "tool": ToolType["Shovel"]
    },

    "Iron Ore": {
        "description": "",
        "category": CategoryType["Natural Blocks"],
        "tool": ToolType["Pickaxe"]
    },

    "Mangrove Log": {
        "description": "",
        "category": CategoryType["Natural Blocks"],
        "tool": ToolType["Axe"]
    },

    "Mangrove Planks": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Axe"]
    },

    "Mangrove Slab": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Axe"]
    },

    "Mangrove Stairs": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Axe"]
    },

    "Oak Leaves": {
        "description": "",
        "category": CategoryType["Natural Blocks"],
        "tool": ToolType["Axe"]
    },

    "Oak Log": {
        "description": "",
        "category": CategoryType["Natural Blocks"],
        "tool": ToolType["Axe"]
    },

    "Oak Planks": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Axe"]
    },

    "Oak Slab": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Axe"]
    },

    "Oak Stairs": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Axe"]
    },

    "Ruby Block": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Pickaxe"]
    },

    "Sapphire Ore": {
        "description": "",
        "category": CategoryType["Natural Blocks"],
        "tool": ToolType["Pickaxe"]
    },

    "Stone Bricks": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Pickaxe"]
    },

    "Stone Brick Slab": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Pickaxe"]
    },

    "Stone Brick Stairs": {
        "description": "",
        "category": CategoryType["Building Blocks"],
        "tool": ToolType["Pickaxe"]
    }
}

category_select = [discord.SelectOption(label = category) for category in CategoryType]

changelog_list = []

# Classes
class ZoomView(ui.View):
    def __init__(self, interaction:discord.Interaction, timeout:float):
        super().__init__(timeout = timeout)
        self.interaction = interaction

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True
        await self.interaction.edit_original_response(
            view = self
        )

class ZoomButton(ui.Button):
    def __init__(self, interaction:discord.Interaction, embed:discord.Embed):
        super().__init__(
            emoji = "🔍",
            style = discord.ButtonStyle.gray
        )
        self.interaction = interaction
        self.embed = embed
        self.description = embed.fields[0]
        self.category = embed.fields[1]
        self.tool = embed.fields[2]

    @ui.button(
        emoji = "🔍",
        style = discord.ButtonStyle.gray
    )
    async def callback(self, interaction:discord.Interaction):
        embed = self.embed

        if self.interaction.user == interaction.user:
            if self.style == discord.ButtonStyle.gray:
                self.style = discord.ButtonStyle.green

                embed.clear_fields()
                embed.set_image(
                    url = embed.thumbnail.url
                )
                embed.set_thumbnail(
                    url = None
                )

                await interaction.response.edit_message(
                    embed = embed,
                    view = self.view
                )
            else:
                self.style = discord.ButtonStyle.gray

                embed.add_field(
                    name = self.description.name,
                    value = self.description.value,
                    inline = self.description.inline
                )
                embed.add_field(
                    name = self.category.name,
                    value = self.category.value,
                    inline = self.category.inline
                )
                embed.add_field(
                    name = self.tool.name,
                    value = self.tool.value,
                    inline = self.tool.inline
                )
                embed.set_thumbnail(
                    url = embed.image.url
                )
                embed.set_image(
                    url = None
                )

                await interaction.response.edit_message(
                    embed = embed,
                    view = self.view
                )


# Command: /ping
@bot.tree.command(
    name = "ping",
    description = "Returns the bot's ping and uptime."
)
@app_commands.allowed_installs(
    guilds = True,
    users = True
)
@app_commands.allowed_contexts(
    guilds = True,
    dms = True,
    private_channels = True
)
async def ping(interaction:discord.Interaction):
    latency = round(bot.latency * 1000)
    uptime = bot.uptime()

    embed = discord.Embed(
        description = f"```ansi\n[2;32mping[0m\n{latency}ms\n\n[2;32muptime[0m\n{uptime}\n```",
        color = 0x2b2d31
    )
    embed.set_author(
        name = game_name,
        url = game_url,
        icon_url = game_icon
    )

    await interaction.response.send_message(
        embed = embed,
        ephemeral = True
    )

# Command: /block <name>
@bot.tree.command(
    name = "block",
    description = "Get more information on the specified block from High Realms."
)
@app_commands.allowed_installs(
    guilds = True,
    users = True
)
@app_commands.allowed_contexts(
    guilds = True,
    dms = True,
    private_channels = True
)
@app_commands.rename(
    block = 'name'
)
@app_commands.describe(
    block = "The name of the block you'd like to know more about."
)
@app_commands.checks.cooldown(
    rate = 1,
    per = 10,
    key = lambda i: (i.guild_id, i.user.id)
)
async def block(interaction:discord.Interaction, block:block_list):
    id = block.replace(' ', '_')
    channel = bot.get_channel(1231482799987625986)
    file = discord.File(
        fp = f'Renders/HighRealms Block {id} 1000x1000.png'
    )
    message = await channel.send(
        file = file
    )

    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

    embed = discord.Embed(
        title = block,
        color = 0x2b2d31
    )
    embed.add_field(
        name = "Description",
        value = block_dict.get(block)['description'] or description,
        inline = False
    )
    embed.add_field(
        name = "Category",
        value = f"```{block_dict.get(block)['category']}```",
        inline = False
    )
    embed.add_field(
        name = "Tool",
        value = block_dict.get(block)['tool'],
        inline = False
    )

    embed.set_author(
        name = game_name,
        url = game_url,
        icon_url = game_icon
    )
    embed.set_thumbnail(
        url = message.attachments[0].url
    )

    view = ZoomView(interaction, 120)
    button = ZoomButton(interaction, embed)
    view.add_item(button)

    await interaction.response.send_message(
        embed = embed,
        view = view
    )

# Command: /changelog [date]
@bot.tree.command(
    name = "changelog",
    description = "Shows you the latest changelog of High Realms. A date can be specified to check a specific update."
)
@app_commands.allowed_installs(
    guilds = True,
    users = True
)
@app_commands.allowed_contexts(
    guilds = True,
    dms = True,
    private_channels = True
)
@app_commands.describe(
    update = "There are no updates yet."
)
async def changelog(interaction:discord.Interaction, update:str = None):
    if update is not None:
        # Needs to be worked on when the game starts getting updates
        embed = discord.Embed(
            title = update,
            color = 0x2b2d31
        )
        embed.set_author(
            name = game_name,
            url = game_url,
            icon_url = game_icon
        )
    else:
        embed = discord.Embed(
            description = f"No changelogs added yet.",
            color = 0x2b2d31
        )
        embed.set_author(
            name = game_name,
            url = game_url,
            icon_url = game_icon
        )

    await interaction.response.send_message(
        embed = embed
    )

@changelog.autocomplete(
    name = 'update'
)
async def autocomplete_callback(interaction:discord.Interaction, current:str):
    list = []
    for update in changelog_list:
        list.append(app_commands.Choice(
            name = update,
            value = update
        ))
    return list

# Error: /ping
@ping.error
async def on_test_error(interaction:discord.Interaction, error:str):
    if isinstance(error, app_commands.AppCommandError):
        print(error)

# Error: /block <name>
@block.error
async def on_test_error(interaction:discord.Interaction, error:str):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(
            content = error,
            ephemeral = True
        )
    else:
        print(error)

# Error: /changelog [date]
@changelog.error
async def on_test_error(interaction:discord.Interaction, error:str):
    if isinstance(error, app_commands.AppCommandError):
        print(error)

# Run
bot.run(TOKEN)
