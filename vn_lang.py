#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import codecs
from unidecode import unidecode
from itertools import product


SUBSTITUTIONS = {
    u'a': u'áảàãạâấẩẫầậăắẳẵằặ',
    u'á': u'aảàãạâấẩẫầậăắẳẵằặ',
    u'ả': u'aáàãạâấẩẫầậăắẳẵằặ',
    u'à': u'aáảãạâấẩẫầậăắẳẵằặ',
    u'ã': u'aáảàạâấẩẫầậăắẳẵằặ',
    u'ạ': u'aáảàãâấẩẫầậăắẳẵằặ',
    u'â': u'aáảàãạấẩẫầậăắẳẵằặ',
    u'ấ': u'aáảàãạâẩẫầậăắẳẵằặ',
    u'ẩ': u'aáảàãạâấẫầậăắẳẵằặ',
    u'ẫ': u'aáảàãạâấẩầậăắẳẵằặ',
    u'ầ': u'aáảàãạâấẩẫậăắẳẵằặ',
    u'ậ': u'aáảàãạâấẩẫầăắẳẵằặ',
    u'ă': u'aáảàãạâấẩẫầậắẳẵằặ',
    u'ắ': u'aáảàãạâấẩẫầậăẳẵằặ',
    u'ẳ': u'aáảàãạâấẩẫầậăắẵằặ',
    u'ẵ': u'aáảàãạâấẩẫầậăắẳằặ',
    u'ằ': u'aáảàãạâấẩẫầậăắẳẵặ',
    u'ặ': u'aáảàãạâấẩẫầậăắẳẵằ',
    u'd': u'đ',
    u'đ': u'd',
    u'e': u'ẹẻèéẽêệểềếễ',
    u'ẹ': u'eẻèéẽêệểềếễ',
    u'ẻ': u'eẹèéẽêệểềếễ',
    u'è': u'eẹẻéẽêệểềếễ',
    u'é': u'eẹẻèẽêệểềếễ',
    u'ẽ': u'eẹẻèéêệểềếễ',
    u'ê': u'eẹẻèéẽệểềếễ',
    u'ệ': u'eẹẻèéẽêểềếễ',
    u'ể': u'eẹẻèéẽêệềếễ',
    u'ề': u'eẹẻèéẽêệểếễ',
    u'ế': u'eẹẻèéẽêệểềễ',
    u'ễ': u'eẹẻèéẽêệểềế',
    u'i': u'ịỉìíĩ',
    u'ị': u'iỉìíĩ',
    u'ỉ': u'iịìíĩ',
    u'ì': u'iịỉíĩ',
    u'í': u'iịỉìĩ',
    u'ĩ': u'iịỉìí',
    u'o': u'ọỏòóõơợởờớỡôổốồỗộ',
    u'ọ': u'oỏòóõơợởờớỡôổốồỗộ',
    u'ỏ': u'oọòóõơợởờớỡôổốồỗộ',
    u'ò': u'oọỏóõơợởờớỡôổốồỗộ',
    u'ó': u'oọỏòõơợởờớỡôổốồỗộ',
    u'õ': u'oọỏòóơợởờớỡôổốồỗộ',
    u'ơ': u'oọỏòóõợởờớỡôổốồỗộ',
    u'ợ': u'oọỏòóõơợờớỡôổốồỗộ',
    u'ở': u'oọỏòóõơợờớỡôổốồỗộ',
    u'ờ': u'oọỏòóõơợởớỡôổốồỗộ',
    u'ớ': u'oọỏòóõơợởờỡôổốồỗộ',
    u'ỡ': u'oọỏòóõơợởờớôổốồỗộ',
    u'ô': u'oọỏòóõơợởờớỡổốồỗộ',
    u'ổ': u'oọỏòóõơợởờớỡôốồỗộ',
    u'ố': u'oọỏòóõơợởờớỡôổồỗộ',
    u'ồ': u'oọỏòóõơợởờớỡôổốỗộ',
    u'ỗ': u'oọỏòóõơợởờớỡôổốồộ',
    u'ộ': u'oọỏòóõơợởờớỡôổốồỗ',
    u'u': u'ụủùúũưựửừứữ',
    u'ụ': u'uủùúũưựửừứữ',
    u'ủ': u'uụùúũưựửừứữ',
    u'ù': u'uụủúũưựửừứữ',
    u'ú': u'uụủùũưựửừứữ',
    u'ũ': u'uụủùúưựửừứữ',
    u'ư': u'uụủùúũựửừứữ',
    u'ự': u'uụủùúũưửừứữ',
    u'ử': u'uụủùúũưựừứữ',
    u'ừ': u'uụủùúũưựửứữ',
    u'ứ': u'uụủùúũưựửừữ',
    u'ữ': u'uụủùúũưựửừứ',
    u'y': u'ỵỷỳýỹ',
    u'ỵ': u'yỷỳýỹ',
    u'ỷ': u'yỵỳýỹ',
    u'ỳ': u'yỵỷýỹ',
    u'ý': u'yỵỷỳỹ',
    u'ỹ': u'yỵỷỳý'
}

VN_LOWERCASE = u'aạảàáã' \
               u'âậẩầấẫ' \
               u'ăặẳằắẵ' \
               u'bcdđ' \
               u'eẹẻèéẽ' \
               u'êệểềếễ' \
               u'fgh' \
               u'iịỉìíĩ' \
               u'jklmn' \
               u'oọỏòóõ' \
               u'ôộổồốỗ' \
               u'ơợởờớỡ' \
               u'pqrst' \
               u'uụủùúũ' \
               u'ưựửừứữ' \
               u'vwx' \
               u'yỵỷỳýỹ' \
               u'z'

VN_UPPERCASE = u'AẠẢÀÁÃ' \
               u'ÂẬẨẦẤẪ' \
               u'ĂẶẮẰẮẴ' \
               u'BCDĐ' \
               u'EẸẺÈÉẼ' \
               u'ÊỆỂỀẾỄ' \
               u'FGH' \
               u'IỊỈÌÍĨ' \
               u'JKLMN' \
               u'OỌỎÒÓÕ' \
               u'ÔỘỔỒỐỖ' \
               u'ƠỢỞỜỚỠ' \
               u'PQRST' \
               u'UỤỦÙÚŨ' \
               u'ƯỰỬỪỨỮ' \
               u'VWX' \
               u'YỴỶỲÝỸ' \
               u'Z'

VN_COMBINE_ACCENT_REPLACE = {
    u'à': u'à',
    u'á': u'á',
    u'ã': u'ã',
    u'ả': u'ả',
    u'ạ': u'ạ',
    u'è': u'è',
    u'é': u'é',
    u'ẽ': u'ẽ',
    u'ẻ': u'ẻ',
    u'ẹ': u'ẹ',
    u'ì': u'ì',
    u'í': u'í',
    u'ĩ': u'ĩ',
    u'ỉ': u'ỉ',
    u'ị': u'ị',
    u'ò': u'ò',
    u'ó': u'ó',
    u'õ': u'õ',
    u'ỏ': u'ỏ',
    u'ọ': u'ọ',
    u'ờ': u'ờ',
    u'ớ': u'ớ',
    u'ỡ': u'ỡ',
    u'ở': u'ở',
    u'ợ': u'ợ',
    u'ù': u'ù',
    u'ú': u'ú',
    u'ũ': u'ũ',
    u'ủ': u'ủ',
    u'ụ': u'ụ',
    u'ỳ': u'ỳ',
    u'ý': u'ý',
    u'ỹ': u'ỹ',
    u'ỷ': u'ỷ',
    u'ỵ': u'ỵ',
    u'â': u'â',
    u'ầ': u'ầ',
    u'ấ': u'ấ',
    u'ẫ': u'ẫ',
    u'ẩ': u'ẩ',
    u'ậ': u'ậ',
    u'ằ': u'ằ',
    u'ắ': u'ắ',
    u'ẵ': u'ẵ',
    u'ẳ': u'ẳ',
    u'ặ': u'ặ',
    u'ừ': u'ừ',
    u'ứ': u'ứ',
    u'ữ': u'ữ',
    u'ử': u'ử',
    u'ự': u'ự',
    u'ê': u'ê',
    u'ề': u'ề',
    u'ế': u'ế',
    u'ễ': u'ễ',
    u'ể': u'ể',
    u'ệ': u'ệ',
    u'ô': u'ô',
    u'ồ': u'ồ',
    u'ố': u'ố',
    u'ỗ': u'ỗ',
    u'ổ': u'ổ',
    u'ộ': u'ộ'
}

VN_CHARACTERS = VN_LOWERCASE + VN_UPPERCASE
DIGIT = u'0123456789'
SPEC_CHARACTERS = u'`~!@$%^&*()_=\|]}[{"\';:/?.>,<“”‘’…'
ADDITIONAL_CHARACTERS = u'`~!@#$%^&*()-_=+\|]}[{"\';:/?.>,<“”‘’…'

_DIGIT = set([x for x in DIGIT])
_ADDITIONAL_CHARACTERS = set([x for x in ADDITIONAL_CHARACTERS])
_VN_LOWERCASE = set([x for x in VN_LOWERCASE])


def vn_islowercase(char):
    """Check is lowercase for a vn character

    :param char: a unicode character
    :return:
    """
    if char in _DIGIT or char in _ADDITIONAL_CHARACTERS:
        return True

    return char in VN_LOWERCASE


def vn_isuppercase(char):
    """Check is uppercase for a vn character

    :param char: a unicode character
    :return:
    """
    if char in DIGIT or char in ADDITIONAL_CHARACTERS:
        return True

    return char in VN_UPPERCASE


def vn_tolowercase(s):
    """To lower case a vn string

    :param s: a unicode vn string
    :return:
    """
    ls = list(s)
    for c in range(0, len(ls)):
        if ls[c] in _DIGIT or ls[c] in _ADDITIONAL_CHARACTERS:
            continue

        if vn_isuppercase(ls[c]):
            ic = VN_UPPERCASE.index(ls[c])
            ls[c] = VN_LOWERCASE[ic]

    return u''.join(ls)


def vn_touppercase(s):
    """To upper case a vn string

    :param s: a unicode vn string
    :return:
    """
    ls = list(s)
    for c in range(0, len(ls)):
        if ls[c] in _DIGIT or ls[c] in _ADDITIONAL_CHARACTERS:
            continue

        if vn_isuppercase(ls[c]):
            ic = VN_LOWERCASE.index(ls[c])
            ls[c] = VN_UPPERCASE[ic]

    return u''.join(ls)


def vn_combine_accent_replace(s):
    """
    convert ascii+combine_accent -> unicode_char
    :param s:
    :return:
    """
    ss = set([x for x in s])
    for k, v in VN_COMBINE_ACCENT_REPLACE.items():
        if k in ss:
            s = s.replace(k, v)
    return s


def load_vocab(vocab_path):
    """ Loading a vocabulary file

    :param vocab_path: Path to vocabulary file
    :return: Array contains words
    """
    with codecs.open(vocab_path, encoding="utf-8") as fobj:
        vocab = fobj.readlines()
    return vocab


def remove_accent(s):
    return unidecode(s)


def smart_truncate(s, numner_of_words=6):
    TERMINATING_CHARS = '–-.,;?!#^'
    result = ' '.join(s.split()[:numner_of_words])
    result = result.strip(TERMINATING_CHARS)

    return result


def add_accent(s, number_of_words=0):
    results = []
    if number_of_words != 0:
        s_1 = smart_truncate(s, number_of_words)
        s_2 = s[len(s_1):]
        possibilities = [c + SUBSTITUTIONS.get(c, "") for c in s_1]
        prod = product(*possibilities)
        for item in prod:
            results.append("".join(item) + s_2)
    else:
        possibilities = [c + SUBSTITUTIONS.get(c, "") for c in s]
        prod = product(*possibilities)
        for item in prod:
            results.append("".join(item))
    # or item in results:
    #    item = item.join(s_2)
    return results


def vietnamese_edit_distance(text1, text2):
    distance = 0
    if (len(text1) == 0) or \
            (len(text2) == 0) or \
            (len(text1) != len(text2)) or \
            (remove_accent(text1) != remove_accent(text2)):
        return distance
    else:
        for i in range(len(text1)):
            if text1[i] != text2[i]:
                distance += 1
    return distance
