# encoding: utf-8
# (C) 2001 - 2020 Rajkumar Palani <rajkumarpalani07@gmail.com>

from . import utf8
from .tcharacter import TChar
import copy as _copy
import string as _string

VALLINAM = ['க்', 'ச்', 'ட்', 'த்', 'ப்', 'ற்']
MELLINAM = ['ங்', 'ஞ்', 'ண்', 'ந்', 'ம்', 'ன்']
IDAIYINAM = ['ய்', 'ர்', 'ல்', 'வ்', 'ழ்', 'ள்']
GRANTHAM = ['ஜ்', 'ஷ்', 'ஸ்', 'ஹ்', 'க்ஷ்', 'ஶ்']
KURIL_VOWELS = ['அ', 'இ', 'உ', 'எ', 'ஒ']
NEDIL_VOWELS = ['ஆ', 'ஈ', 'ஊ', 'ஏ', 'ஐ', 'ஓ', 'ஔ']
AGARAM = ['க', 'ச', 'ட', 'த', 'ப', 'ற', 'ஞ', 'ங', 'ண', 'ந', 'ம', 'ன', 'ய', 'ர', 'ல' ,'வ','ழ', 'ள']

VOWEL_RESOLVER = {'அ': '', 'ஆ': '\u0BBE', 'இ': '\u0BBF', 'ஈ': '\u0BC0', 'உ': '\u0BC1', 'ஊ': '\u0BC2', 
                  'எ': '\u0BC6', 'ஏ': '\u0BC7', 'ஐ': '\u0BC8', 'ஒ': '\u0BCA', 'ஓ': '\u0BCB', 'ஔ': '\u0BCC' }


AllTA_List = _copy.copy(utf8.AllTAM_List)
AllTA_List.extend(_string.whitespace)
AllTA_List.extend(_string.punctuation)

def is_vallinam(vinam: str) -> bool:
    if(vinam in VALLINAM):
        return True
    return False

def is_mellinam(minam: str) -> bool:
    if(minam in MELLINAM):
        return True
    return False

def is_idaiyinam(iinam:str) -> bool:
    if(iinam in IDAIYINAM):
        return True
    return False

def is_grantham(grantham:str) -> bool:
    if(grantham in GRANTHAM):
        return True
    return False

def is_kuril(kuril:str) -> bool:
    if(kuril in KURIL_VOWELS):
        return True
    return False

def is_nedil(nedil:str) -> bool:
    if(nedil in NEDIL_VOWELS):
        return True
    return False

def is_tamil(tc1:str) -> bool:
    # check if the letter tc1 is a unicode tamil-letter.
    if (tc1 in AllTA_List):
        return True
    return False

def mei_to_agaram(mei:str) -> str:
    # From the mei character, Extract agaram
    seperated = []
    for val in mei:
        seperated.append(val)

    if (len(seperated) >4 ):
        raise ValueError('Input value for mei exceeded three codepoints...!')
    if (len(seperated) <2 ):
        raise ValueError('Input value for mei less than two codepoints...!')
    if (len(seperated) == 4) and (TChar.is_ksha_uyirmei(seperated[0], seperated[1], seperated[2], seperated[3])):
        # 'க்ஷ்' to 'க்ஷ'
        return u"".join(seperated[0] + seperated[1] + seperated[2])
    elif (len(seperated) == 2) and (mei in GRANTHAM):
        # Handle regular grantham mei except 'க்ஷ்'
        # 'ஸ்' to 'ஸ'
        return (seperated[0])
    elif (len(seperated) == 2) and TChar.is_agaram(seperated[0]):
        # Handle regular mei
        # 'க்' to 'க'
        return (seperated[0])
    return None

def get_uyirmei(uyir:str, mei:str) -> str:
    # uyir   : அ
    # mei    : க்
    # return : க
    if(not len(mei) == 2):
        raise ValueError('Input value for mei is not two codepoints...!')
    if(TChar.is_uyir(uyir) and TChar.is_mei(mei[0], mei[1])):
        assert(TChar.is_agaram(mei[0]))
        resolvedvowel = VOWEL_RESOLVER.get(uyir)
        return (mei[0] + resolvedvowel) 
    return None

def is_controlcode(controlChar:str) -> str:
    # Check for ASCII Control char
    intval = ord(controlChar)
    return (0 < intval and intval < 32) or (127 < intval and intval < 159)

def is_basiclatin(BasicLChar:str) -> str:
    # Check for Basic Latin char
    intval = ord(BasicLChar)
    return (32 < intval and intval < 126)

def is_latin1supplement(L1SupChar:str) -> str:
    # Check for Latin1Supplement char
    intval = ord(L1SupChar)
    return (160 < intval and intval < 255)

def is_tamilonly(tword1:str) -> bool:
    # Checks for tamil letters. 
    # Whitespaces and Punctuations are allowed to pass through.
    if (len(tword1) == 0) :
        raise ValueError('Input value is empty...!')

    flist = list(filter(lambda c: c in AllTA_List, tword1))

    alltamilflag:bool = True
    for val in (tword1):
        if (val not in flist):
            alltamilflag = False
    return alltamilflag


# TODO: implement later
def mathirai(word:str) -> int:
    pass

