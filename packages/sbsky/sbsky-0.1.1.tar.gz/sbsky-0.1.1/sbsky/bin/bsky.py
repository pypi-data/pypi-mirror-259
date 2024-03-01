import fire
import os
from pathlib import Path
from loguru import logger
from sbsky.lib.bsky import Bsky
from sbsky.lib.text_builder import TextBuilderRenderer

login = os.environ["BSKYUSERNAME"]
password = os.environ["BSKYPASSWORD"]

logger.level("TRACE")

class BskyCLI:
    def __init__(self, session_file="~/.bsky/sessionfile.txt"):
        session_file = Path(session_file).expanduser()
        self._ensure_bsky_folder(session_file)
        self.bsky = Bsky(session_file=str(session_file))


    def _ensure_bsky_folder(self, session_file):
        bsky_folder = session_file.parent
        bsky_folder.mkdir(parents=True, exist_ok=True)

    async def parse(self, text):
        # await self.bsky.auth(login, password)
        return TextBuilderRenderer().render(text)


    async def post(self, text):
        await self.bsky.auth(login, password)
        await self.bsky.post(text)


def run():
    fire.Fire(BskyCLI)


if __name__ == "__main__":
    run()
