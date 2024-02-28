import pyrogramx
from pyrogramx import raw
from .menu_button import MenuButton


class MenuButtonCommands(MenuButton):
    """A menu button, which opens the bot's list of commands."""

    def __init__(self):
        super().__init__("commands")

    async def write(
        self, client: "pyrogramx.Client"
    ) -> "raw.types.BotMenuButtonCommands":
        return raw.types.BotMenuButtonCommands()
