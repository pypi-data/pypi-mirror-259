from uuid import uuid4

import pyrogramx
from pyrogramx import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~pyrogramx.types.InlineQueryResultCachedAudio`
    - :obj:`~pyrogramx.types.InlineQueryResultCachedDocument`
    - :obj:`~pyrogramx.types.InlineQueryResultCachedAnimation`
    - :obj:`~pyrogramx.types.InlineQueryResultCachedPhoto`
    - :obj:`~pyrogramx.types.InlineQueryResultCachedSticker`
    - :obj:`~pyrogramx.types.InlineQueryResultCachedVideo`
    - :obj:`~pyrogramx.types.InlineQueryResultCachedVoice`
    - :obj:`~pyrogramx.types.InlineQueryResultArticle`
    - :obj:`~pyrogramx.types.InlineQueryResultAudio`
    - :obj:`~pyrogramx.types.InlineQueryResultContact`
    - :obj:`~pyrogramx.types.InlineQueryResultDocument`
    - :obj:`~pyrogramx.types.InlineQueryResultAnimation`
    - :obj:`~pyrogramx.types.InlineQueryResultLocation`
    - :obj:`~pyrogramx.types.InlineQueryResultPhoto`
    - :obj:`~pyrogramx.types.InlineQueryResultVenue`
    - :obj:`~pyrogramx.types.InlineQueryResultVideo`
    - :obj:`~pyrogramx.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup",
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "pyrogramx.Client"):
        pass
