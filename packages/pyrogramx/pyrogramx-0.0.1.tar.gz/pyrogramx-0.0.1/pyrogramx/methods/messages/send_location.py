from datetime import datetime
from typing import Union

import pyrogramx
from pyrogramx import raw, utils
from pyrogramx import types


class SendLocation:
    async def send_location(
        self: "pyrogramx.Client",
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        schedule_date: datetime = None,
        protect_content: bool = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply",
        ] = None,
    ) -> "types.Message":
        """Send points on the map.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            latitude (``float``):
                Latitude of the location.

            longitude (``float``):
                Longitude of the location.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            reply_markup (:obj:`~pyrogramx.types.InlineKeyboardMarkup` | :obj:`~pyrogramx.types.ReplyKeyboardMarkup` | :obj:`~pyrogramx.types.ReplyKeyboardRemove` | :obj:`~pyrogramx.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            :obj:`~pyrogramx.types.Message`: On success, the sent location message is returned.

        Example:
            .. code-block:: python

                app.send_location("me", latitude, longitude)
        """
        r = await self.invoke(
            raw.functions.messages.SendMedia(
                peer=await self.resolve_peer(chat_id),
                media=raw.types.InputMediaGeoPoint(
                    geo_point=raw.types.InputGeoPoint(lat=latitude, long=longitude)
                ),
                message="",
                silent=disable_notification or None,
                reply_to_msg_id=reply_to_message_id,
                random_id=self.rnd_id(),
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                noforwards=protect_content,
                reply_markup=await reply_markup.write(self) if reply_markup else None,
            )
        )

        for i in r.updates:
            if isinstance(
                i,
                (
                    raw.types.UpdateNewMessage,
                    raw.types.UpdateNewChannelMessage,
                    raw.types.UpdateNewScheduledMessage,
                ),
            ):
                return await types.Message._parse(
                    self,
                    i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats},
                    is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage),
                )
