import pyrogramx
from pyrogramx import raw
from .bot_command_scope import BotCommandScope


class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """Represents the scope of bot commands, covering all group and supergroup chat administrators."""

    def __init__(self):
        super().__init__("all_chat_administrators")

    async def write(self, client: "pyrogramx.Client") -> "raw.base.BotCommandScope":
        return raw.types.BotCommandScopeChatAdmins()
