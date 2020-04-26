#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random
from vn_lang import VN_LOWERCASE
from unidecode import unidecode
import math

SAMPLING_MAP = {
    u"q": [u"1", u"2", u"w", u"a", u"s"],
    u"w": [u"2", u"3", u"q", u"e", u"a", u"s", u"d"],
    u"e": [u"3", u"4", u"w", u"r", u"s", u"d", u"f", u"é", u"ê", u"è"],
    u"r": [u"4", u"5", u"e", u"t", u"d", u"f", u"g"],
    u"t": [u"5", u"6", u"r", u"y", u"f", u"g", u"h"],
    u"y": [u"6", u"7", u"t", u"u", u"g", u"h", u"j", u"ỵ"],
    u"u": [u"7", u"8", u"y", u"i", u"h", u"j", u"k", u"ụ"],
    u"i": [u"8", u"9", u"u", u"o", u"ị", u"j", u"k", u"l"],
    u"o": [u"9", u"0", u"i", u"p", u"k", u"l", u";", u"ô"],
    u"p": [u"0", u"-", u"[", u"o", u"l", u";", u"'", "b"],
    u"a": [u"q", u"w", u"z", u"x", u"s", u"â", u"á"],
    u"s": [u"q", u"w", u"e", u"a", u"s", u"d", u"z", u"x", u"c"],
    u"d": [u"w", u"e", u"r", u"s", u"f", u"x", u"c", u"v", u"đ"],
    u"f": [u"e", u"r", u"t", u"d", u"g", u"c", u"v", u"b"],
    u"g": [u"r", u"t", u"y", u"f", u"h", u"v", u"b", u"n"],
    u"h": [u"t", u"y", u"u", u"g", u"j", u"b", u"n", u"m"],
    u"j": [u"y", u"u", u"i", u"h", u"k", u"n", u"m", u","],
    u"k": [u"c", u"u", u"i", u"o", u"j", u"l", u"m", u",", u"."],
    u"l": [u"i", u"o", u"p", u"k", u";", u",", u".", u"/"],
    u"đ": [u"w", u"e", u"r", u"s", u"f", u"x", u"c", u"v", u"d", u"dd"],
    u"z": [u"a", u"s", u"x"],
    u"x": [u"z", u"a", u"s", u"d", u"c"],
    u"c": [u"k", u"x", u"s", u"d", u"f", u"v"],
    u"v": [u"c", u"b", u"d", u"f", u"g"],
    u"b": [u"v", u"f", u"g", u"h", u"n", u"p"],
    u"n": [u"b", u"m", u"g", u"h", u"j"],
    u"m": [u"n", u"j", u",", u"k"],
    u"â": [u"a", u"aa"],
    u"ấ": [u"a", u"á", u"aa", u"aas", u"â"],
    u"ầ": [u"a", u"à", u"aa", u"aaf", u"â"],
    u"ậ": [u"a", u"ạ", u"aa", u"aaj", u"â"],
    u"ẩ": [u"a", u"ả", u"aa", u"aar", u"â"],
    u"ă": [u"a", u"aw"],
    u"ắ": [u"a", u"á", u"aw", u"aws", u"ă"],
    u"ằ": [u"a", u"à", u"aw", u"awf", u"ă"],
    u"ặ": [u"a", u"ạ", u"aw", u"awj", u"ă"],
    u"ẳ": [u"a", u"ả", u"aw", u"awr", u"ă"],
    u"á": [u"as", u"a"],
    u"à": [u"af", u"a"],
    u"ạ": [u"aj", u"a"],
    u"ả": [u"ar", u"a"],
    u"ê": [u"e", u"ee"],
    u"ế": [u"e", u"ee", u"ees"],
    u"ề": [u"e", u"ee", u"eef"],
    u"ệ": [u"e", u"ee", u"eej"],
    u"ể": [u"e", u"ee", u"eer"],
    u"é": [u"e", u"es"],
    u"è": [u"e", u"ef"],
    u"ẹ": [u"e", u"ej"],
    u"ẻ": [u"e", u"er"],
    u"ư": [u"u", u"uw", u"]"],
    u"ứ": [u"u", u"uw", u"uws", u"]s"],
    u"ừ": [u"u", u"uw", u"uwf", u"]f"],
    u"ự": [u"u", u"uw", u"uwj", u"]j"],
    u"ử": [u"u", u"uw", u"uwr", u"]r"],
    u"ú": [u"u", u"us"],
    u"ù": [u"u", u"uf"],
    u"ụ": [u"u", u"uj"],
    u"ủ": [u"u", u"ur"],
    u"ý": [u"y", u"ys", u"í", u"is"],
    u"ỳ": [u"y", u"yf", u"ì", u"if"],
    u"ỵ": [u"y", u"yj", u"ị", u"ij"],
    u"ỷ": [u"y", u"yr", u"ỉ", u"ir"],
    u"í": [u"y", u"ys", u"ý", u"is"],
    u"ì": [u"y", u"yf", u"ỳ", u"if"],
    u"ị": [u"y", u"yj", u"ỵ", u"ij"],
    u"ỉ": [u"y", u"yr", u"ỷ", u"ir"],
    u"ô": [u"o", u"oo"],
    u"ố": [u"o", u"oo", u"oos", u"ô"],
    u"ồ": [u"o", u"oo", u"oof", u"ô"],
    u"ộ": [u"o", u"oo", u"ooj", u"ô"],
    u"ổ": [u"o", u"oo", u"oor", u"ô"],
    u"ơ": [u"o", u"ow", u"["],
    u"ớ": [u"o", u"ows", u"[s", u"ơ"],
    u"ò": [u"o", u"owf", u"[f", u"ơ"],
    u"ợ": [u"o", u"owj", u"[j", u"ơ"],
    u"ở": [u"o", u"owr", u"[r", u"ơ"],
    u"ó": [u"os", u"o"],
    u"ò": [u"of", u"o"],
    u"ọ": [u"oj", u"o"],
    u"ỏ": [u"or", u"o"],
}

VN_TELEX = {
    u"ấ": [(u"aa", u"s"), (u"â", u"s")],
    u"ầ": [(u"aa", u"f"), (u"â", u"f")],
    u"ậ": [(u"aa", u"j"), (u"â", u"j")],
    u"ẩ": [(u"aa", u"r"), (u"â", u"r")],
    u"ắ": [(u"aw", u"s"), (u"ă", u"s")],
    u"ằ": [(u"aw", u"f"), (u"ă", u"f")],
    u"ặ": [(u"aw", u"j"), (u"ă", u"j")],
    u"ẳ": [(u"aw", u"r"), (u"ă", u"r")],
    u"á": [(u"a", u"s")],
    u"à": [(u"a", u"f")],
    u"ạ": [(u"a", u"j")],
    u"ả": [(u"a", u"r")],
    u"ế": [(u"ee", u"s"), (u"ê", u"s")],
    u"ề": [(u"ee", u"f"), (u"ê", u"f")],
    u"ệ": [(u"ee", u"j"), (u"ê", u"j")],
    u"ể": [(u"ee", u"r"), (u"ê", u"r")],
    u"é": [(u"e", u"s")],
    u"è": [(u"e", u"f")],
    u"ẹ": [(u"e", u"j")],
    u"ẻ": [(u"e", u"r")],
    u"ứ": [(u"ư", u"s"), (u"uw", u"s")],
    u"ừ": [(u"ư", u"f"), (u"uw", u"f")],
    u"ự": [(u"ư", u"j"), (u"uw", u"j")],
    u"ử": [(u"ư", u"r"), (u"uw", u"r")],
    u"ú": [(u"u", u"s")],
    u"ù": [(u"u", u"f")],
    u"ụ": [(u"u", u"j")],
    u"ủ": [(u"u", u"r")],
    u"í": [(u"i", u"s")],
    u"ì": [(u"i", u"f")],
    u"ị": [(u"i", u"j")],
    u"ỉ": [(u"i", u"r")],
    u"ý": [(u"y", u"s")],
    u"ỳ": [(u"y", u"f")],
    u"ỵ": [(u"y", u"j")],
    u"ỷ": [(u"y", u"r")],
    u"ố": [(u"ô", u"s"), (u"oo", u"s")],
    u"ồ": [(u"ô", u"f"), (u"oo", u"f")],
    u"ộ": [(u"ô", u"j"), (u"oo", u"j")],
    u"ổ": [(u"ô", u"r"), (u"oo", u"r")],
    u"ớ": [(u"ơ", u"s"), (u"ow", u"s")],
    u"ờ": [(u"ơ", u"f"), (u"ow", u"f")],
    u"ợ": [(u"ơ", u"j"), (u"ow", u"j")],
    u"ở": [(u"ơ", u"r"), (u"ow", u"r")],
    u"ó": [(u"o", u"s")],
    u"ò": [(u"o", u"f")],
    u"ọ": [(u"o", u"j")],
    u"ỏ": [(u"o", u"r")],
    u"đ": [(u"d", u"d")],
}

ACTIONS = [
    "INSERT", "REMOVE", "NORMAL_REPLACE", "TELEX_REPLACE", "DO_NOTHING", "UNACCENT"
]

# Add space character
CHARS = VN_LOWERCASE + u" "


def generate_misspell_sample(query, n=25, max_edit_distance=4):
    tokens = query.split()
    if len(tokens) == 1:
        n = 15
    elif len(tokens) == 2:
        n = 25
    elif len(tokens) == 3:
        n = 35
    else:
        n = 45
    clenq = len(query)
    vv = clenq / 4
    if vv == 0:
        vv = 1
    max_edit_distance = int(min(vv, max_edit_distance))

    results = set()

    for _ in range(n):
        actions = [random.choice(ACTIONS) for i in range(max_edit_distance)]
        qx = query

        for a in actions:
            clen = len(qx)
            pos = random.randint(0, clen - 1)

            if a == "DO_NOTHING":
                continue

            if a == "INSERT":
                rc = random.sample(CHARS, 1)[0]
                qx = qx[:pos + 1] + rc + qx[pos + 1:]
            elif a == "REMOVE":
                qx = qx[:pos] + qx[pos + 1:]
            elif a == "NORMAL_REPLACE":
                c = qx[pos]
                if c not in SAMPLING_MAP:
                    qx = qx[:pos] + random.choice(CHARS) + qx[pos + 1:]
                else:
                    qx = qx[:pos] + \
                        random.choice(SAMPLING_MAP[c]) + qx[pos + 1:]
            elif a == "TELEX_REPLACE":
                c = qx[pos]
                if c not in VN_TELEX:
                    if c not in SAMPLING_MAP:
                        qx = qx[:pos] + random.choice(CHARS) + qx[pos + 1:]
                    else:
                        qx = qx[:pos] + \
                            random.choice(SAMPLING_MAP[c]) + qx[pos + 1:]
                else:
                    if pos < len(qx) - 1:
                        nc = qx[pos + 1]
                        telex_c = random.choice(VN_TELEX[c])
                        if nc != u" ":
                            qx = qx[:pos] + telex_c[0] + \
                                nc + telex_c[1] + qx[pos + 2:]
                        else:
                            qx = qx[:pos] + telex_c[0] + \
                                telex_c[1] + qx[pos + 1:]
            elif a == "UNACCENT":
                tokens = qx.split()
                tc = random.randint(0, len(tokens) - 1)
                tokens[tc] = unidecode(tokens[tc])
                qx = u" ".join(tokens)

        qx = u" ".join(qx.split())
        if qx != query:
            results.add(qx)

    return results


if __name__ == "__main__":
    for r in generate_misspell_sample(u"quần áo"):
        print(r)
