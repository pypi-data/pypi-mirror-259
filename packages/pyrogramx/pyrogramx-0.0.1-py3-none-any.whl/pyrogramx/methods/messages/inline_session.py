import pyrogramx
from pyrogramx import raw
from pyrogramx.errors import AuthBytesInvalid
from pyrogramx.session import Session
from pyrogramx.session.auth import Auth


async def get_session(client: "pyrogramx.Client", dc_id: int):
    if dc_id == await client.storage.dc_id():
        return client

    async with client.media_sessions_lock:
        if client.media_sessions.get(dc_id):
            return client.media_sessions[dc_id]

        session = client.media_sessions[dc_id] = Session(
            client,
            dc_id,
            await Auth(client, dc_id, await client.storage.test_mode()).create(),
            await client.storage.test_mode(),
            is_media=True,
        )

        await session.start()

        for _ in range(3):
            exported_auth = await client.invoke(
                raw.functions.auth.ExportAuthorization(dc_id=dc_id)
            )

            try:
                await session.invoke(
                    raw.functions.auth.ImportAuthorization(
                        id=exported_auth.id, bytes=exported_auth.bytes
                    )
                )
            except AuthBytesInvalid:
                continue
            else:
                break
        else:
            await session.stop()
            raise AuthBytesInvalid

        return session
