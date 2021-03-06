# encoding: utf-8
# (C) 2001 - 2020 Rajkumar Palani <rajkumarpalani07@gmail.com>

from .tcharacter import TChar
from .tace16 import Tace16
from . import tcutil


def reverse(ts1: str) -> str:
    # Reverse a Tamil word
    slist = TChar.get_graphemes(ts1)
    slist.reverse()
    return u"".join(slist)


def length(ts1: str) -> int:
    # get the tamil string length
    slist = TChar.get_graphemes(ts1)
    return len(slist)


def substring(ts1: str, start: int, fin: int) -> str:
    # substring for a tamil string
    if (start < 0 or fin > len(ts1)):
        raise ValueError("String Index Out Of Bounds Error...!")

    if ((start == 0) and (fin == len(ts1))):
        return ts1
    else:
        slist = TChar.get_graphemes(ts1)
        tlist = slist[start:fin]
        return u"".join(tlist)


def replace(ts1: str, oldtc: str, newtc: str) -> str:
    # Replace a tamil grapheme with a new grapheme in ts1
    if(len(ts1) == 0):
        raise ValueError('Input string supplied is empty...!')
    else:
        slist = TChar.get_graphemes(ts1)
        tlist = list(map(lambda x: x.replace(oldtc, newtc), slist))
        return u"".join(tlist)

# deprecated as of V1.0
def _compare_lexicaly(tstr1: str, tstr2: str) -> int:
    # -ve :: if tstr1 < tstr2
    # 0 :: if tstr1 == tstr2
    # +ve :: if tstr1 > tstr2
    if ((tcutil.is_tamilonly(tstr1)) and (tcutil.is_tamilonly(tstr2))):
        tace1 = Tace16._to_tace16(tstr1)
        tace2 = Tace16._to_tace16(tstr2)
        len1 = len(tace1)
        len2 = len(tace2)
        pos1 = 0
        pos2 = 0
        for i in range(min(len1, len2)):
            tc1 = tace1[i]
            tc2 = tace2[i]
            pos1 = ord(tc1)
            pos2 = ord(tc2)
            if((pos1 == pos2) and (len1 != len2)):
                return len1 - len2
        return pos1 - pos2
    else:
        return None


# sort key as per tace order
# Usage:: listtosort.sort(key=tace_sort_key)
def tace_sort_key(tword):
    ords = []
    tace1 = Tace16._to_tace16(tword)
    for tletter in tace1:
        ords.append(ord(tletter))
    return ords
