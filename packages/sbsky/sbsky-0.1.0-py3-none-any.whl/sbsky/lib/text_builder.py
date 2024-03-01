from typing import Any, Dict, cast
from atproto import IdResolver
from atproto_identity.handle.resolver import HandleResolver
from mistune.core import BlockState
from mistune.renderers.markdown import MarkdownRenderer
from atproto_client.utils import TextBuilder
import mistune
from .mistune_plugins import hashtags, mentions

class BlueSkyRenderer(MarkdownRenderer):
    def __init__(self):
        super().__init__()
        self.text_builder = TextBuilder()
        self.resolver = IdResolver()
        self.include = True # Using a temporary lock, should be improved

    def link(self, token: Dict[str, Any], state: BlockState) -> str:
        label = cast(str, token.get("label"))
        self.include = False
        text = self.render_children(token, state)
        self.include = True
        out = '[' + text + ']'
        if label:
            return out + '[' + label + ']'

        attrs = token['attrs']
        url = attrs['url']
        title = attrs.get('title')
        if text == url and not title:
            return '<' + text + '>'
        elif 'mailto:' + text == url and not title:
            return '<' + text + '>'

        out += '('
        if '(' in url or ')' in url:
            out += '<' + url + '>'
        else:
            out += url
        if title:
            out += ' "' + title + '"'
        self.text_builder.link(url=url, text=text)
        return out + ')'

    def text(self, token: Dict[str, Any], state: BlockState) -> str:
        if self.include:
            self.text_builder.text(cast(str, token["raw"]))
        return cast(str, token["raw"])

    def mention(self, token: Dict[str, Any], state: BlockState) -> str:
        name = token['raw']
        did = self.resolver.handle.resolve(f"@{name}")
        # I can't resolve something like washingtonpost.com and bsky.app
        self.text_builder.mention(name, did if did else "")
        return f"@{name}"

    def hashtag(self, token: Dict[str, Any], state: BlockState) -> str:
        tag = token['raw']
        self.text_builder.tag(tag, tag)
        return f'#{tag}'


class TextBuilderRenderer():
    def __init__(self):
        super().__init__()
        self.parser = mistune.Markdown(renderer=BlueSkyRenderer(), inline=mistune.InlineParser(hard_wrap=False), plugins=[mentions, hashtags])

    def parse(self, text: str) -> TextBuilder:
        self.parser.parse(text)
        return self.parser.renderer.text_builder # type: ignore

    def render(self, text: str):
        return self.parser.parse(text)
