import pyrogramx
from pyrogramx import raw
from pyrogramx import types


class GetMe:
    async def get_me(self: "pyrogramx.Client") -> "types.User":
        """Get your own user identity.

        .. include:: /_includes/usable-by/users-bots.rst

        Returns:
            :obj:`~pyrogramx.types.User`: Information about the own logged in user/bot.

        Example:
            .. code-block:: python

                me = await app.get_me()
                print(me)
        """
        r = await self.invoke(
            raw.functions.users.GetFullUser(id=raw.types.InputUserSelf())
        )

        users = {u.id: u for u in r.users}

        return types.User._parse(self, users[r.full_user.id])
