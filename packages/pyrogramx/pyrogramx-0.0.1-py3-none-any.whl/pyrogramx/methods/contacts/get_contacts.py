import logging
from typing import List

import pyrogramx
from pyrogramx import raw
from pyrogramx import types

log = logging.getLogger(__name__)


class GetContacts:
    async def get_contacts(self: "pyrogramx.Client") -> List["types.User"]:
        """Get contacts from your Telegram address book.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~pyrogramx.types.User`: On success, a list of users is returned.

        Example:
            .. code-block:: python

                contacts = await app.get_contacts()
                print(contacts)
        """
        contacts = await self.invoke(raw.functions.contacts.GetContacts(hash=0))
        return types.List(types.User._parse(self, user) for user in contacts.users)
