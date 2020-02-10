#!/usr/bin/env python
# encoding:utf8

"""
    DragonPy - Dragon 32 emulator in Python
    =======================================

    This file was generated by parsing "font-6847.png" from XRoar.
    The generator code war removed with:

    https://github.com/jedie/DragonPy/commit/2044cf6f44ca8b2e3dbb377a07fe8ccecf173c0d

    You can see the deleted files here:

    https://github.com/jedie/DragonPy/tree/6aee7cab8df49c638c2c49ea6fd152e5a54b792d/dragonpy/Dragon32/DragonFont

    see also:
        http://archive.worldofdragon.org/index.php?title=CharMap

    :created: 2014 by Jens Diemer - www.jensdiemer.de
    :copyleft: 2014-2015 by the DragonPy team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""


import logging
import math

from dragonpy.Dragon32.dragon_charmap import COLORS, INVERTED, NORMAL, get_hex_color


try:
    import tkinter  # python 3
except ImportError:
    import tkinter as tkinter  # Python 2


log = logging.getLogger(__name__)


BACKGROUND_CHAR = "."
FOREGROUND_CHAR = "X"
CHARS_DICT = {
    '@': (  # COMMERCIAL AT
        "........",
        "........",
        "........",
        "...XXX..",
        "..X...X.",
        "......X.",
        "...XX.X.",
        "..X.X.X.",
        "..X.X.X.",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    'A': (  # LATIN CAPITAL LETTER A
        "........",
        "........",
        "........",
        "....X...",
        "...X.X..",
        "..X...X.",
        "..X...X.",
        "..XXXXX.",
        "..X...X.",
        "..X...X.",
        "........",
        "........",
        "........",
    ),
    'B': (  # LATIN CAPITAL LETTER B
        "........",
        "........",
        "........",
        "..XXXX..",
        "...X..X.",
        "...X..X.",
        "...XXX..",
        "...X..X.",
        "...X..X.",
        "..XXXX..",
        "........",
        "........",
        "........",
    ),
    'C': (  # LATIN CAPITAL LETTER C
        "........",
        "........",
        "........",
        "...XXX..",
        "..X...X.",
        "..X.....",
        "..X.....",
        "..X.....",
        "..X...X.",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    'D': (  # LATIN CAPITAL LETTER D
        "........",
        "........",
        "........",
        "..XXXX..",
        "...X..X.",
        "...X..X.",
        "...X..X.",
        "...X..X.",
        "...X..X.",
        "..XXXX..",
        "........",
        "........",
        "........",
    ),
    'E': (  # LATIN CAPITAL LETTER E
        "........",
        "........",
        "........",
        "..XXXXX.",
        "..X.....",
        "..X.....",
        "..XXXX..",
        "..X.....",
        "..X.....",
        "..XXXXX.",
        "........",
        "........",
        "........",
    ),
    'F': (  # LATIN CAPITAL LETTER F
        "........",
        "........",
        "........",
        "..XXXXX.",
        "..X.....",
        "..X.....",
        "..XXXX..",
        "..X.....",
        "..X.....",
        "..X.....",
        "........",
        "........",
        "........",
    ),
    'G': (  # LATIN CAPITAL LETTER G
        "........",
        "........",
        "........",
        "...XXXX.",
        "..X.....",
        "..X.....",
        "..X..XX.",
        "..X...X.",
        "..X...X.",
        "...XXXX.",
        "........",
        "........",
        "........",
    ),
    'H': (  # LATIN CAPITAL LETTER H
        "........",
        "........",
        "........",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "..XXXXX.",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "........",
        "........",
        "........",
    ),
    'I': (  # LATIN CAPITAL LETTER I
        "........",
        "........",
        "........",
        "...XXX..",
        "....X...",
        "....X...",
        "....X...",
        "....X...",
        "....X...",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    'J': (  # LATIN CAPITAL LETTER J
        "........",
        "........",
        "........",
        "......X.",
        "......X.",
        "......X.",
        "......X.",
        "..X...X.",
        "..X...X.",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    'K': (  # LATIN CAPITAL LETTER K
        "........",
        "........",
        "........",
        "..X...X.",
        "..X..X..",
        "..X.X...",
        "..XX....",
        "..X.X...",
        "..X..X..",
        "..X...X.",
        "........",
        "........",
        "........",
    ),
    'L': (  # LATIN CAPITAL LETTER L
        "........",
        "........",
        "........",
        "..X.....",
        "..X.....",
        "..X.....",
        "..X.....",
        "..X.....",
        "..X.....",
        "..XXXXX.",
        "........",
        "........",
        "........",
    ),
    'M': (  # LATIN CAPITAL LETTER M
        "........",
        "........",
        "........",
        "..X...X.",
        "..XX.XX.",
        "..X.X.X.",
        "..X.X.X.",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "........",
        "........",
        "........",
    ),
    'N': (  # LATIN CAPITAL LETTER N
        "........",
        "........",
        "........",
        "..X...X.",
        "..XX..X.",
        "..X.X.X.",
        "..X..XX.",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "........",
        "........",
        "........",
    ),
    'O': (  # LATIN CAPITAL LETTER O
        "........",
        "........",
        "........",
        "..XXXXX.",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "..XXXXX.",
        "........",
        "........",
        "........",
    ),
    'P': (  # LATIN CAPITAL LETTER P
        "........",
        "........",
        "........",
        "..XXXX..",
        "..X...X.",
        "..X...X.",
        "..XXXX..",
        "..X.....",
        "..X.....",
        "..X.....",
        "........",
        "........",
        "........",
    ),
    'Q': (  # LATIN CAPITAL LETTER Q
        "........",
        "........",
        "........",
        "...XXX..",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "..X.X.X.",
        "..X..X..",
        "...XX.X.",
        "........",
        "........",
        "........",
    ),
    'R': (  # LATIN CAPITAL LETTER R
        "........",
        "........",
        "........",
        "..XXXX..",
        "..X...X.",
        "..X...X.",
        "..XXXX..",
        "..X.X...",
        "..X..X..",
        "..X...X.",
        "........",
        "........",
        "........",
    ),
    'S': (  # LATIN CAPITAL LETTER S
        "........",
        "........",
        "........",
        "...XXX..",
        "..X...X.",
        "...X....",
        "....X...",
        ".....X..",
        "..X...X.",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    'T': (  # LATIN CAPITAL LETTER T
        "........",
        "........",
        "........",
        "..XXXXX.",
        "....X...",
        "....X...",
        "....X...",
        "....X...",
        "....X...",
        "....X...",
        "........",
        "........",
        "........",
    ),
    'U': (  # LATIN CAPITAL LETTER U
        "........",
        "........",
        "........",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    'V': (  # LATIN CAPITAL LETTER V
        "........",
        "........",
        "........",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "...X.X..",
        "...X.X..",
        "....X...",
        "....X...",
        "........",
        "........",
        "........",
    ),
    'W': (  # LATIN CAPITAL LETTER W
        "........",
        "........",
        "........",
        "..X...X.",
        "..X...X.",
        "..X...X.",
        "..X.X.X.",
        "..X.X.X.",
        "..XX.XX.",
        "..X...X.",
        "........",
        "........",
        "........",
    ),
    'X': (  # LATIN CAPITAL LETTER X
        "........",
        "........",
        "........",
        "..X...X.",
        "..X...X.",
        "...X.X..",
        "....X...",
        "...X.X..",
        "..X...X.",
        "..X...X.",
        "........",
        "........",
        "........",
    ),
    'Y': (  # LATIN CAPITAL LETTER Y
        "........",
        "........",
        "........",
        "..X...X.",
        "..X...X.",
        "...X.X..",
        "....X...",
        "....X...",
        "....X...",
        "....X...",
        "........",
        "........",
        "........",
    ),
    'Z': (  # LATIN CAPITAL LETTER Z
        "........",
        "........",
        "........",
        "..XXXXX.",
        "......X.",
        ".....X..",
        "....X...",
        "...X....",
        "..X.....",
        "..XXXXX.",
        "........",
        "........",
        "........",
    ),
    '[': (  # LEFT SQUARE BRACKET
        "........",
        "........",
        "........",
        "..XXX...",
        "..X.....",
        "..X.....",
        "..X.....",
        "..X.....",
        "..X.....",
        "..XXX...",
        "........",
        "........",
        "........",
    ),
    '\\': (  # REVERSE SOLIDUS
        "........",
        "........",
        "........",
        "..X.....",
        "..X.....",
        "...X....",
        "....X...",
        ".....X..",
        "......X.",
        "......X.",
        "........",
        "........",
        "........",
    ),
    ']': (  # RIGHT SQUARE BRACKET
        "........",
        "........",
        "........",
        "....XXX.",
        "......X.",
        "......X.",
        "......X.",
        "......X.",
        "......X.",
        "....XXX.",
        "........",
        "........",
        "........",
    ),
    '\u2191': (  # UPWARDS ARROW
        "........",
        "........",
        "........",
        "....X...",
        "...XXX..",
        "..X.X.X.",
        "....X...",
        "....X...",
        "....X...",
        "....X...",
        "........",
        "........",
        "........",
    ),
    '\u2190': (  # LEFTWARDS ARROW
        "........",
        "........",
        "........",
        "........",
        "....X...",
        "...X....",
        "..XXXXX.",
        "...X....",
        "....X...",
        "........",
        "........",
        "........",
        "........",
    ),
    ' ': (  # SPACE
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
    ),
    '!': (  # EXCLAMATION MARK
        "........",
        "........",
        "........",
        "....X...",
        "....X...",
        "....X...",
        "....X...",
        "....X...",
        "........",
        "....X...",
        "........",
        "........",
        "........",
    ),
    '"': (  # QUOTATION MARK
        "........",
        "........",
        "........",
        "...X.X..",
        "...X.X..",
        "...X.X..",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
    ),
    '#': (  # NUMBER SIGN
        "........",
        "........",
        "........",
        "...X.X..",
        "...X.X..",
        "..XX.XX.",
        "........",
        "..XX.XX.",
        "...X.X..",
        "...X.X..",
        "........",
        "........",
        "........",
    ),
    '$': (  # DOLLAR SIGN
        "........",
        "........",
        "........",
        "....X...",
        "...XXXX.",
        "..X.....",
        "...XXX..",
        "......X.",
        "..XXXX..",
        "....X...",
        "........",
        "........",
        "........",
    ),
    '%': (  # PERCENT SIGN
        "........",
        "........",
        "........",
        "..XX..X.",
        "..XX..X.",
        ".....X..",
        "....X...",
        "...X....",
        "..X..XX.",
        "..X..XX.",
        "........",
        "........",
        "........",
    ),
    '&': (  # AMPERSAND
        "........",
        "........",
        "........",
        "...X....",
        "..X.X...",
        "..X.X...",
        "...X....",
        "..X.X.X.",
        "..X..X..",
        "...XX.X.",
        "........",
        "........",
        "........",
    ),
    "'": (  # APOSTROPHE
        "........",
        "........",
        "........",
        "...XX...",
        "...XX...",
        "...XX...",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
    ),
    '(': (  # LEFT PARENTHESIS
        "........",
        "........",
        "........",
        "....X...",
        "...X....",
        "..X.....",
        "..X.....",
        "..X.....",
        "...X....",
        "....X...",
        "........",
        "........",
        "........",
    ),
    ')': (  # RIGHT PARENTHESIS
        "........",
        "........",
        "........",
        "....X...",
        ".....X..",
        "......X.",
        "......X.",
        "......X.",
        ".....X..",
        "....X...",
        "........",
        "........",
        "........",
    ),
    '*': (  # ASTERISK
        "........",
        "........",
        "........",
        "........",
        "....X...",
        "...XXX..",
        "..XXXXX.",
        "...XXX..",
        "....X...",
        "........",
        "........",
        "........",
        "........",
    ),
    '+': (  # PLUS SIGN
        "........",
        "........",
        "........",
        "........",
        "....X...",
        "....X...",
        "..XXXXX.",
        "....X...",
        "....X...",
        "........",
        "........",
        "........",
        "........",
    ),
    ',': (  # COMMA
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "..XX....",
        "..XX....",
        "...X....",
        "..X.....",
        "........",
        "........",
        "........",
    ),
    '-': (  # HYPHEN-MINUS
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "..XXXXX.",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
    ),
    '.': (  # FULL STOP
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "..XX....",
        "..XX....",
        "........",
        "........",
        "........",
    ),
    '/': (  # SOLIDUS
        "........",
        "........",
        "........",
        "......X.",
        "......X.",
        ".....X..",
        "....X...",
        "...X....",
        "..X.....",
        "..X.....",
        "........",
        "........",
        "........",
    ),
    '0': (  # DIGIT ZERO
        "........",
        "........",
        "........",
        "...XX...",
        "..X..X..",
        "..X..X..",
        "..X..X..",
        "..X..X..",
        "..X..X..",
        "...XX...",
        "........",
        "........",
        "........",
    ),
    '1': (  # DIGIT ONE
        "........",
        "........",
        "........",
        "....X...",
        "...XX...",
        "....X...",
        "....X...",
        "....X...",
        "....X...",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    '2': (  # DIGIT TWO
        "........",
        "........",
        "........",
        "...XXX..",
        "..X...X.",
        "......X.",
        "...XXX..",
        "..X.....",
        "..X.....",
        "..XXXXX.",
        "........",
        "........",
        "........",
    ),
    '3': (  # DIGIT THREE
        "........",
        "........",
        "........",
        "...XXX..",
        "..X...X.",
        "......X.",
        "....XX..",
        "......X.",
        "..X...X.",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    '4': (  # DIGIT FOUR
        "........",
        "........",
        "........",
        ".....X..",
        "....XX..",
        "...X.X..",
        "..XXXXX.",
        ".....X..",
        ".....X..",
        ".....X..",
        "........",
        "........",
        "........",
    ),
    '5': (  # DIGIT FIVE
        "........",
        "........",
        "........",
        "..XXXXX.",
        "..X.....",
        "..XXXX..",
        "......X.",
        "......X.",
        "..X...X.",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    '6': (  # DIGIT SIX
        "........",
        "........",
        "........",
        "...XXX..",
        "..X.....",
        "..X.....",
        "..XXXX..",
        "..X...X.",
        "..X...X.",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    '7': (  # DIGIT SEVEN
        "........",
        "........",
        "........",
        "..XXXXX.",
        "......X.",
        ".....X..",
        "....X...",
        "...X....",
        "..X.....",
        "..X.....",
        "........",
        "........",
        "........",
    ),
    '8': (  # DIGIT EIGHT
        "........",
        "........",
        "........",
        "...XXX..",
        "..X...X.",
        "..X...X.",
        "...XXX..",
        "..X...X.",
        "..X...X.",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    '9': (  # DIGIT NINE
        "........",
        "........",
        "........",
        "...XXX..",
        "..X...X.",
        "..X...X.",
        "...XXXX.",
        "......X.",
        "......X.",
        "...XXX..",
        "........",
        "........",
        "........",
    ),
    ':': (  # COLON
        "........",
        "........",
        "........",
        "........",
        "...XX...",
        "...XX...",
        "........",
        "...XX...",
        "...XX...",
        "........",
        "........",
        "........",
        "........",
    ),
    ';': (  # SEMICOLON
        "........",
        "........",
        "........",
        "...XX...",
        "...XX...",
        "........",
        "...XX...",
        "...XX...",
        "....X...",
        "...X....",
        "........",
        "........",
        "........",
    ),
    '<': (  # LESS-THAN SIGN
        "........",
        "........",
        "........",
        ".....X..",
        "....X...",
        "...X....",
        "..X.....",
        "...X....",
        "....X...",
        ".....X..",
        "........",
        "........",
        "........",
    ),
    '=': (  # EQUALS SIGN
        "........",
        "........",
        "........",
        "........",
        "........",
        "..XXXXX.",
        "........",
        "..XXXXX.",
        "........",
        "........",
        "........",
        "........",
        "........",
    ),
    '>': (  # GREATER-THAN SIGN
        "........",
        "........",
        "........",
        "...X....",
        "....X...",
        ".....X..",
        "......X.",
        ".....X..",
        "....X...",
        "...X....",
        "........",
        "........",
        "........",
    ),
    '?': (  # QUESTION MARK
        "........",
        "........",
        "........",
        "...XX...",
        "..X..X..",
        ".....X..",
        "....X...",
        "....X...",
        "........",
        "....X...",
        "........",
        "........",
        "........",
    ),
    '\u2588': (  # FULL BLOCK
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
    ),
    '\u259b': (  # QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER LEFT
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
    ),
    '\u259c': (  # QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER RIGHT
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
    ),
    '\u2580': (  # UPPER HALF BLOCK
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
    ),
    '\u2599': (  # QUADRANT UPPER LEFT AND LOWER LEFT AND LOWER RIGHT
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
    ),
    '\u258c': (  # LEFT HALF BLOCK
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
    ),
    '\u259a': (  # QUADRANT UPPER LEFT AND LOWER RIGHT
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
    ),
    '\u2598': (  # QUADRANT UPPER LEFT
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
    ),
    '\u259f': (  # QUADRANT UPPER RIGHT AND LOWER LEFT AND LOWER RIGHT
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
    ),
    '\u259e': (  # QUADRANT UPPER RIGHT AND LOWER LEFT
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
    ),
    '\u2590': (  # RIGHT HALF BLOCK
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
    ),
    '\u259d': (  # QUADRANT UPPER RIGHT
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
    ),
    '\u2584': (  # LOWER HALF BLOCK
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
        "XXXXXXXX",
    ),
    '\u2596': (  # QUADRANT LOWER LEFT
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
    ),
    '\u2597': (  # QUADRANT LOWER RIGHT
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
        "....XXXX",
    ),
}


class TkImageFont(object):
    """
    Important is that image must be bind to a object, without:
    the garbage-collection by Python will "remove" the created images in Tkinter.Canvas!
    """

    def __init__(self, chars_dict, scale_factor):
        assert isinstance(scale_factor, int)
        assert scale_factor > 0

        self.chars_dict = chars_dict
        self.scale_factor = scale_factor

        temp = chars_dict["X"]
        self.width_real = len(temp[0])
        self.height_real = len(temp)

        self.width_scaled = self.width_real * self.scale_factor
        self.height_scaled = self.height_real * self.scale_factor

        log.critical("Every character is %ipx x %ipx (incl. scale factor: %i)",
                     self.width_scaled, self.height_scaled,
                     self.scale_factor
                     )

    def get_char(self, char, color):
        log.critical("Generate char %s %s", repr(char), color)
        try:
            char_data = self.chars_dict[char]
        except KeyError:
            log.log(99, "Error: character %s is not in CHARS_DICT !", repr(char))
#             return self._generate_char(char="?", color=color)
            return self.get_char(char="?", color=color)

        foreground, background = get_hex_color(color)
        foreground = f"#{foreground}"
        background = f"#{background}"

        img = tkinter.PhotoImage(
            width=self.width_scaled,
            height=self.height_scaled
        )

        # Fill the character pixels without padding
        for y, line in enumerate(char_data):
            for x, bit in enumerate(line):
                if bit == BACKGROUND_CHAR:
                    color = background
                else:
                    assert bit == FOREGROUND_CHAR
                    color = foreground

                img.put(color, (x, y))

        # resize the character
        if self.scale_factor > 1:
            img = img.zoom(self.scale_factor, self.scale_factor)

        return img


class TestTkImageFont(object):
    CACHE = {}

    def __init__(self, row_count, tk_font, colors):
        self.row_count = row_count
        self.tk_font = tk_font
        self.colors = colors
        self.color_index = 0
        self.current_color = self.colors[self.color_index]

        self.root = tkinter.Tk()
        self.root.title("TkImageFont Test")

        self.root.bind('<Down>', self.event_arrow_down)
        self.root.bind('<Up>', self.event_arrow_up)

        self.total_width = self.tk_font.width_scaled * self.row_count
        self.total_height = int(
            self.tk_font.height_scaled * math.ceil(
                len(self.tk_font.chars_dict) / self.row_count + 1
            )
        )

        print(f"Window/Canvas geometry: {self.total_width}px x {self.total_height}px")
        self.root.geometry(f"+{self.total_width:d}+{self.total_height:d}")

        self.canvas = tkinter.Canvas(self.root,
                                     width=self.total_width,
                                     height=self.total_height,
                                     bd=0,  # Border
                                     bg="#000000",
                                     )
        self.canvas.pack()
        self.add_chars()
        self.root.update()

    def add_chars(self):
        print("Fill with", self.current_color)
        chars_dict = self.tk_font.chars_dict
        for no, char in enumerate(sorted(chars_dict.keys())):
            y, x = divmod(no * self.tk_font.width_scaled, self.total_width)
            y *= self.tk_font.height_scaled
#             print "add %s color: %s to %i x %i" % (
#                 repr(char), self.current_color, x, y
#             )
            img = self.tk_font.get_char(char, self.current_color)
            self.CACHE[(char, self.current_color)] = img  # avoid garbage collection

            self.canvas.create_image(x, y,
                                     image=img,
                                     state="normal",
                                     anchor=tkinter.NW  # NW == NorthWest
                                     )

    def event_arrow_up(self, event):
        self.color_index += 1
        if self.color_index >= len(self.colors):
            self.color_index = 0
        self.current_color = self.colors[self.color_index]
        self.add_chars()

    def event_arrow_down(self, event):
        self.color_index -= 1
        if self.color_index < 0:
            self.color_index = len(self.colors) - 1
        self.current_color = self.colors[self.color_index]
        self.add_chars()

    def mainloop(self):
        self.root.mainloop()


def test_dict(chars_dict, width, height):
    for char, data in sorted(chars_dict.items()):
        if len(data) != height:
            print("Char %s has wrong height / row count !" % repr(char))
            print(f"Should have {height:d} rows, but has: {len(data):d} rows")
        for line in data:
            if len(line) != width:
                print("Char %s has wrong width / column count !" % repr(char))
                print(f"Should have {width:d} columns, but has: {len(line):d} columns")


if __name__ == "__main__":
    test_dict(CHARS_DICT, width=8, height=13)

#     scale_factor = 1
#     scale_factor = 2
#     scale_factor = 3
    scale_factor = 4
#     scale_factor = 8
    tk_font = TkImageFont(
        CHARS_DICT, scale_factor,
    )

    colors = (NORMAL, INVERTED) + COLORS

    t = TestTkImageFont(
        row_count=10,
        tk_font=tk_font,
        colors=colors,
    )
    t.mainloop()
    print(" --- END --- ")
