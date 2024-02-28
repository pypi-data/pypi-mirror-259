import re


_ESC = '\x1b['
_OPEN = {
    # Decoration
    'bold': '1',
    'dim': '2',
    'italic': '3',
    'under': '4',
    'blink': '5',
    'strike': '9',
    'frame': '51',
    'circle': '52',
    'overline': '53',
    # Foreground Colors
    'black': '30',
    'red': '31',
    'green': '32',
    'yellow': '33',
    'blue': '34',
    'magenta': '35',
    'cyan': '36',
    'white': '37',
    # Background Colors
    'bg_black': '40',
    'bg_red': '41',
    'bg_green': '42',
    'bg_yellow': '44',
    'bg_blue': '44',
    'bg_magenta': '45',
    'bg_cyan': '46'
}
_CLOSE = {
    # Decoration
    '/bold': '22',
    '/dim': '22',
    '/italic': '23',
    '/under': '24',
    '/blink': '25',
    '/strike': '29',
    '/frame': '54',
    '/circle': '54',
    '/overline': '55',
    # Foreground Colors
    '/black': '39',
    '/red': '39',
    '/green': '39',
    '/yellow': '39',
    '/blue': '39',
    '/magenta': '39',
    '/cyan': '39',
    '/white': '39',
    # Background Colors
    '/bg_white': '49',
    '/bg_black': '49',
    '/bg_red': '49',
    '/bg_green': '49',
    '/bg_yellow': '49',
    '/bg_blue': '49',
    '/bg_magenta': '49',
    '/bg_cyan': '49',
    # End all formatting
    '/': '0'
}
_LINK_PREFIX = '\x1b]8;;'
_LINK_SUFFIX = '\x1b\x5c'
# Matches all ansi regex tags that are supported in a string
_ANSI_REGEX = re.compile(r'\x1b\[\d+(;\d*)*m|\x1b]8;;[^\\]*\x1b\x5c')
_ANSI = {**_OPEN, **_CLOSE}


def _parse_link(match: re.Match) -> str:
    url, text = match.groups()
    return _LINK_PREFIX + url + _LINK_SUFFIX + text + _LINK_PREFIX + _LINK_SUFFIX


def _strip_link(match: re.Match) -> str:
    return match.groups()[1]


def strip_ansi(ansi_str: str) -> str:
    """For links, **the URL will be REMOVED, leaving only the text behind**"""
    return _ANSI_REGEX.sub('', ansi_str)


def parse_ansi(ansi_str: str) -> str:
    """Parses a string with ANSI codes and attempts to convert them to markdown"""
    raise NotImplementedError('Still need to implement this!')
