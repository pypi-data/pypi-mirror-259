from loguru import logger
from atproto import (
    AsyncClient,
    models,
)
from typing import (
    Dict,
    Any,
    List,
)

import os

from sbsky.lib.text_builder import TextBuilderRenderer


class Bsky:
    # I don't feel like there is a rate limit on the operations yet
    def __init__(
        self,
        session_file: str = "sessionfile.txt",
    ):
        self.client = AsyncClient()
        self.session_file = session_file

    async def auth(
        self,
        login: str,
        password: str,
    ):
        logger.info(f"Loading Session File from: {self.session_file}")
        if os.path.exists(self.session_file):
            # Load session string from file
            if not await self._import_session_string():
                await self._get_new_token(login, password)
        else:
            # Authenticate and save session string to file
            await self._get_new_token(login, password)

    async def _import_session_string(self) -> bool:
        if os.path.exists(self.session_file):
            # Load session string from file
            with open(self.session_file, "r") as f:
                session_string = f.read().strip()
                await self.client._import_session_string(session_string)
                try:
                    await self.client._refresh_and_set_session()
                    await self.client.login(session_string=session_string)
                    logger.info("Session loaded from file.")
                    return True
                except Exception as e:
                    logger.warning(f"caught BadRequestError {e} Returning False")
                    return False
        return False

    async def _get_new_token(self, login: str, password: str):
        self.client = AsyncClient()
        await self.client.login(login=login, password=password)
        session_string = self.client.export_session_string()
        with open(self.session_file, "w") as f:
            f.write(session_string)
            logger.info("New session authenticated and saved.")

    async def parse(self, text):
        return TextBuilderRenderer().parse(text)

    async def post(self, text):
        res = await self.client.post(TextBuilderRenderer().parse(text))
        logger.info(f"Posted Text: Returned {res}")
