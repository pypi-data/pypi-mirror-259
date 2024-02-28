from typing import Callable

import pyrogramx


class OnRawUpdate:
    def on_raw_update(self=None, group: int = 0) -> Callable:
        """Decorator for handling raw updates.

        This does the same thing as :meth:`~pyrogramx.Client.add_handler` using the
        :obj:`~pyrogramx.handlers.RawUpdateHandler`.

        Parameters:
            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogramx.Client):
                self.add_handler(pyrogramx.handlers.RawUpdateHandler(func), group)
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((pyrogramx.handlers.RawUpdateHandler(func), group))

            return func

        return decorator
