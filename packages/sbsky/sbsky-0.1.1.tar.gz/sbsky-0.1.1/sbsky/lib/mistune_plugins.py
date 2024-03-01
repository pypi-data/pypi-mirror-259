__all__ = ['mentions', 'hashtags']

from typing import Match
from mistune.markdown import Markdown

MENTION_PATTERN = r'@([\w+.]+)'
HASHTAG_PATTERN = r'#(\w+)'

def parse_mention(inline: "InlineParser", m: Match[str], state: "InlineState") -> int: # type: ignore
    name = m.group(0).strip("@")
    state.append_token({"type": "mention", "raw": name})
    return m.end()

def render_mention(renderer: "BaseRenderer", name: str) -> str: # type: ignore
    # Adjust the rendering as needed
    return f'<a href="/user/{name}" class="mention">@{name}</a>'

def mentions(md: "Markdown") -> None:
    md.inline.register('mention', MENTION_PATTERN, parse_mention, before='text')

def parse_hashtag(inline: "InlineParser", m: Match[str], state: "InlineState") -> int: # type: ignore
    tag = m.group(0).strip("#")
    state.append_token({"type": "hashtag", "raw": tag})
    return m.end()

def render_hashtag(renderer: "BaseRenderer", tag: str) -> str:
    # Adjust the rendering as needed
    return f'<a href="/tag/{tag}" class="hashtag">#{tag}</a>'

def hashtags(md: "Markdown") -> None:
    md.inline.register('hashtag', HASHTAG_PATTERN, parse_hashtag, before='text') # type: ignore
