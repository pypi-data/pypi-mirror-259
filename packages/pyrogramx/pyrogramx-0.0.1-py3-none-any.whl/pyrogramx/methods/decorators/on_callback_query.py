from typing import Callable

import pyrogramx
from pyrogramx.filters import Filter


class OnCallbackQuery:
    def on_callback_query(self=None, filters=None, group: int = 0) -> Callable:
        """Decorator for handling callback queries.

        This does the same thing as :meth:`~pyrogramx.Client.add_handler` using the
        :obj:`~pyrogramx.handlers.CallbackQueryHandler`.

        Parameters:
            filters (:obj:`~pyrogramx.filters`, *optional*):
                Pass one or more filters to allow only a subset of callback queries to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogramx.Client):
                self.add_handler(
                    pyrogramx.handlers.CallbackQueryHandler(func, filters), group
                )
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrogramx.handlers.CallbackQueryHandler(func, self),
                        group if filters is None else filters,
                    )
                )

            return func

        return decorator
