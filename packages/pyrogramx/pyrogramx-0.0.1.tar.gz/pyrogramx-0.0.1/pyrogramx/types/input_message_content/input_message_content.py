import pyrogramx

from ..object import Object

"""- :obj:`~pyrogramx.types.InputLocationMessageContent`
    - :obj:`~pyrogramx.types.InputVenueMessageContent`
    - :obj:`~pyrogramx.types.InputContactMessageContent`"""


class InputMessageContent(Object):
    """Content of a message to be sent as a result of an inline query.

    Pyrogram currently supports the following types:

    - :obj:`~pyrogramx.types.InputTextMessageContent`
    """

    def __init__(self):
        super().__init__()

    async def write(self, client: "pyrogramx.Client", reply_markup):
        raise NotImplementedError
