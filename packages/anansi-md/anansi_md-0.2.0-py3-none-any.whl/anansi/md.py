import re

from anansi.ansi import _ANSI, _ESC, _OPEN, _parse_link, _strip_link


_TAG_REGEX = re.compile(fr'(\[(?:/?\s*(?:(?:{"|".join(_OPEN.keys())})\s*)*)+])')
_LINK_REGEX = re.compile(r'\[link=(?P<url>[^]]*)](?P<txt>.*)\[/link]')


def _parse_tags(cmd: re.Match) -> str:
    cmd = cmd.groups()[0]
    contents = cmd.strip('[').strip(']')
    tags = contents.split(' ')
    for i, tag in enumerate(tags):
        code = _ANSI.get(tag)
        if not code:
            continue
        tags[i] = code
    return f'{_ESC}{";".join(tags)}m'


def parse_md(md_str: str) -> str:
    tags_parsed = _TAG_REGEX.sub(_parse_tags, md_str)
    return _LINK_REGEX.sub(_parse_link, tags_parsed)


def strip_md(line: str) -> str:
    tagged = _TAG_REGEX.sub('', line)
    return _LINK_REGEX.sub(_strip_link, tagged)
