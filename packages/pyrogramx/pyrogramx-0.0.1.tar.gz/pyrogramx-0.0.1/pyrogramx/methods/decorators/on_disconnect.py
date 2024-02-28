from typing import Callable

import pyrogramx


class OnDisconnect:
    def on_disconnect(self=None) -> Callable:
        """Decorator for handling disconnections.

        This does the same thing as :meth:`~pyrogramx.Client.add_handler` using the
        :obj:`~pyrogramx.handlers.DisconnectHandler`.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogramx.Client):
                self.add_handler(pyrogramx.handlers.DisconnectHandler(func))
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((pyrogramx.handlers.DisconnectHandler(func), 0))

            return func

        return decorator
