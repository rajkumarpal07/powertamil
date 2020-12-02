# encoding: utf-8
# (C) 2001 - 2020 Rajkumar Palani <rajkumarpalani07@gmail.com>

import re


"""
A FEW POINTS:
* Unicode Sign ANUSVARA use is discouraged. So omitted from this interface.
* TAMIL SIGN VIRAMA is named as PULLI as the word VIRAMA is not in use.
* <a href="https://unicode.org/charts/PDF/U0B80.pdf">Character names-Version 10.0</a> 
* This file contains an excerpt from the character code tables and 
* list of character names for
* The Unicode Standard, Version 10.0
"""

# TA constants
TA_SYMBOLS_LEN = 13
TA_VMARKER_LEN = 12
TA_NUMERALS_LEN = 13
TA_AYUDHA_LEN = 1
TA_UYIR_LEN = 12
TA_MEI_LEN = 18
TA_AGARAM_LEN = 18
TA_UYIRMEI_LEN = 12*18
TA_GRANTHAMEI_LEN = 6
TA_GRANTHAUYIRMEI_LEN = 6*12
TA_SRI_LEN = 1
TA_LETTERS_LEN = TA_SYMBOLS_LEN + TA_VMARKER_LEN + TA_NUMERALS_LEN + TA_AYUDHA_LEN + TA_UYIR_LEN + \
    + TA_MEI_LEN + TA_GRANTHAMEI_LEN + TA_UYIRMEI_LEN + TA_GRANTHAUYIRMEI_LEN + TA_SRI_LEN  #364

# Standard Unicode Aytham (Visarga)
AYTHAM = "TAMIL LETTER AYTHAM"

# Standard Unicode 12 Vowel Sign Names
VOWEL_MARKER_PULLI = "PULLI"
VOWEL_MARKER_AA = "AA"
VOWEL_MARKER_I = "I"
VOWEL_MARKER_II = "II"
VOWEL_MARKER_U = "U"
VOWEL_MARKER_UU = "UU"
VOWEL_MARKER_E = "E"
VOWEL_MARKER_EE = "EE"
VOWEL_MARKER_AI = "AI"

# Standard Unicode Two Part Dependent Vowel Sign Names
VOWEL_MARKER_O = "O"
VOWEL_MARKER_OO = "OO"
VOWEL_MARKER_AU = "AU"

# Standard Unicode Uyir Names (Vowels - Independent)
UYIR_A = "TAMIL LETTER A"
UYIR_AA = "TAMIL LETTER AA"
UYIR_I = "TAMIL LETTER I"
UYIR_II = "TAMIL LETTER II"
UYIR_U = "TAMIL LETTER U"
UYIR_UU = "TAMIL LETTER UU"
UYIR_E = "TAMIL LETTER E"
UYIR_EE = "TAMIL LETTER EE"
UYIR_AI = "TAMIL LETTER AI"
UYIR_O = "TAMIL LETTER O"
UYIR_OO = "TAMIL LETTER OO"
UYIR_AU = "TAMIL LETTER AU"

# Standard Unicode Agaram Names (Consonants)
AGARAM_KA = "TAMIL LETTER KA"
AGARAM_NGA = "TAMIL LETTER NGA"
AGARAM_CA = "TAMIL LETTER CA"
AGARAM_NYA = "TAMIL LETTER NYA"
AGARAM_TTA = "TAMIL LETTER TTA"
AGARAM_NNA = "TAMIL LETTER NNA"
AGARAM_TA = "TAMIL LETTER TA"
AGARAM_NA = "TAMIL LETTER NA"
AGARAM_PA = "TAMIL LETTER PA"
AGARAM_MA = "TAMIL LETTER MA"
AGARAM_YA = "TAMIL LETTER YA"
AGARAM_RA = "TAMIL LETTER RA"
AGARAM_LA = "TAMIL LETTER LA"
AGARAM_VA = "TAMIL LETTER VA"
AGARAM_LLLA = "TAMIL LETTER LLLA"
AGARAM_LLA = "TAMIL LETTER LLA"
AGARAM_RRA = "TAMIL LETTER RRA"
AGARAM_NNNA = "TAMIL LETTER NNNA"

# Standard Unicode Tamil Digits
DIGIT_0 = "TAMIL DIGIT ZERO"
DIGIT_1 = "TAMIL DIGIT ONE"
DIGIT_2 = "TAMIL DIGIT TWO"
DIGIT_3 = "TAMIL DIGIT THREE"
DIGIT_4 = "TAMIL DIGIT FOUR"
DIGIT_5 = "TAMIL DIGIT FIVE"
DIGIT_6 = "TAMIL DIGIT SIX"
DIGIT_7 = "TAMIL DIGIT SEVEN"
DIGIT_8 = "TAMIL DIGIT EIGHT"
DIGIT_9 = "TAMIL DIGIT NINE"

# Standard Unicode Tamil Numbers
NUMBER_10 = "TAMIL NUMBER TEN"
NUMBER_100 = "TAMIL NUMBER HUNDRED"
NUMBER_1000 = "TAMIL NUMBER THOUSAND"

# Standard Unicode Tamil Symbol Names
SYMBOL_OM = "TAMIL OM"
SYMBOL_DAY = "TAMIL DAY SIGN"
SYMBOL_MONTH = "TAMIL MONTH SIGN"
SYMBOL_YEAR = "TAMIL YEAR SIGN"
SYMBOL_DEBIT = "TAMIL DEBIT SIGN"
SYMBOL_CREDIT = "TAMIL CREDIT SIGN"
SYMBOL_AS_ABOVE = "TAMIL AS ABOVE SIGN"
SYMBOL_RUPEE = "TAMIL RUPEE SIGN"
SYMBOL_NUMBER = "TAMIL NUMBER SIGN"


# regex pattern strings follow
ALLVMARKER_PATTERN = "\u0BCD|\u0BBE|\u0BBF|\u0BC0|\u0BC1|\u0BC2|\u0BC6|\u0BC7|\u0BC8|\u0BCA|\u0BCB|\u0BCC"
UMVMARKER_PATTERN = "\u0BBE|\u0BBF|\u0BC0|\u0BC1|\u0BC2|\u0BC6|\u0BC7|\u0BC8|\u0BCA|\u0BCB|\u0BCC"
SRI_PATTERN = "[\u0BB8][\u0BCD][\u0BB0][\u0BC0]"
KSHAUYIRMEI_PATTERN = "[\u0B95][\u0BCD][\u0BB7]" + "[" + UMVMARKER_PATTERN + "]"
KSHA_PATTERN = "[\u0B95][\u0BCD][\u0BB7]"
GRANTHAAGARAM_PATTERN = "[\u0B9C|\u0BB7|\u0BB8|\u0BB9|\u0BB6]"
GRANTHAMEI_PATTERN = "[\u0B9C|\u0BB7|\u0BB8|\u0BB9|\u0BB6][\u0BCD]"
GRANTHAUYIRMEI_PATTERN = "[\u0B9C|\u0BB7|\u0BB8|\u0BB9|\u0BB6]" + "[" + ALLVMARKER_PATTERN + "]"
AGARAM = "\u0B95|\u0B9A|\u0B9F|\u0BA4|\u0BAA|\u0BB1|\u0B9E|\u0B99|\u0BA3|\u0BA8|\u0BAE|\u0BA9|\u0BAF|\u0BB0|\u0BB2|\u0BB5|\u0BB4|\u0BB3"
VMARKER_PATTERN = "\u0BBE|\u0BBF|\u0BC0|\u0BC1|\u0BC2|\u0BC6|\u0BC7|\u0BC8|\u0BCA|\u0BCB|\u0BCC"
UYIRMEI_PATTERN = "[" + AGARAM + "]"+"[" + VMARKER_PATTERN + "]"
MEI_PATTERN = "[" + AGARAM + "]"+"[" + "\u0BCD" + "]"
AGARAM_PATTERN = "[" + AGARAM + "]"
UYIR_PATTERN = "[\u0B85|\u0B86|\u0B87|\u0B88|\u0B89|\u0B8A|\u0B8E|\u0B8F|\u0B90|\u0B92|\u0B93|\u0B94]"
AYTHAM_PATTERN = "\u0B83"
NUMERAL_PATTERN = "[\u0BE6|\u0BE7|\u0BE8|\u0BE9|\u0BEA|\u0BEB|\u0BEC|\u0BED|\u0BEE|\u0BEF|\u0BF0|\u0BF1|\u0BF2]"



class TChar:
    """represents a Tamil character with functions"""

    def __init__(self):
        pass

    @staticmethod
    def is_vowel_marker(cp):
        return cp == '\u0BCD' or cp == '\u0BBE' or cp == '\u0BBF' or \
            cp == '\u0BC0' or cp == '\u0BC1' or cp == '\u0BC2' or \
            cp == '\u0BC6' or cp == '\u0BC7' or cp == '\u0BC8' or  \
            cp == '\u0BCA' or cp == '\u0BCB' or cp == '\u0BCC'

    # Checks for presence of Agaram Letters (Tamil Agaram).
    @staticmethod
    def is_agaram(cp1):
        return cp1 == '\u0B95' or cp1 == '\u0B99' or cp1 == '\u0B9A' or cp1 == '\u0B9E' or cp1 == '\u0B9F' or cp1 == '\u0BA3' or\
            cp1 == '\u0BA4' or cp1 == '\u0BA8' or cp1 == '\u0BAA' or cp1 == '\u0BAE' or cp1 == '\u0BAF' or cp1 == '\u0BB0' or \
            cp1 == '\u0BB2' or cp1 == '\u0BB5' or cp1 == '\u0BB4' or cp1 == '\u0BB3' or cp1 == '\u0BB1' or cp1 == '\u0BA9'

    # Checks for the presence of Uyir Letter (Tamil Vowel).
    # 0xb85 0xb86 0xb87 0xb88 0xb89 0xb8a 0xb8e 0xb8f 0xb90 0xb92 0xb93 0xb94
    @staticmethod
    def is_uyir(cp1):
        return cp1 == '\u0B85' or cp1 == '\u0B86' or cp1 == '\u0B87' or cp1 == '\u0B88' or cp1 == '\u0B89' or cp1 == '\u0B8A' or\
            cp1 == '\u0B8E' or cp1 == '\u0B8F' or cp1 == '\u0B90' or cp1 == '\u0B92' or cp1 == '\u0B93' or cp1 == '\u0B94'

    # Checks for the presence of Mei Letter (Tamil Consonant).
    def is_mei(cp1, cp2):
        return (TChar.is_agaram(cp1) and (cp2 == '\u0BCD'))

    # Checks for the presence of UyirMei Letter (Tamil Vowel-Consonant).
    @staticmethod
    def is_uyirmei(cp1, cp2):
        return (TChar.is_agaram(cp1)) and (TChar.is_vowel_marker(cp2))

    # Checks if the given Code Point is an Aytham.
    @staticmethod
    def is_aytham(cp1):
        return (cp1 == '\u0B83')

    # Checks if the given Code Point is an tamil numeral.
    @staticmethod
    def is_tnumeral(cp1):
        if (len(cp1) == 0):
            raise TypeError('Input value is empty...!')
        else:
            return ord(cp1) > 3046 and ord(cp1) < 3055

    # Checks if the given Code Point is an tamil symbol.
    @staticmethod
    def is_tsymbol(cp1):
        if (len(cp1) == 0):
            raise TypeError('Input value is empty...!')
        else:
            return ord(cp1) > 3055 and ord(cp1) < 3067

    # Checks if the given Code Point is an grantha agaram.
    @staticmethod
    def is_grantha_agaram(cp1):
        return (cp1 == '\u0B9C') | (cp1 == '\u0BB6') | (cp1 == '\u0BB7') | (cp1 == '\u0BB8') | (cp1 == '\u0BB9')

    # Checks for the presence of Grantha Uyir Mei (excluding kshaUyirMei since it is of 4 CPs).
    @staticmethod
    def is_grantha_uyirmei(cp1, cp2):
        return TChar.is_grantha_agaram(cp1) and TChar.is_vowel_marker(cp2)

    # Checks for the presence of all Grantha Uyir Mei (including kshaUyirMei).
    @staticmethod
    def is_all_grantha_uyirmei(cp1, cp2, cp3, cp4):
        if (cp3 is None and cp4 is None):
            return TChar.is_grantha_uyirmei(cp1, cp2)
        else:
            return TChar.is_ksha_uyirmei(cp1, cp2, cp3, cp4)

    # Checks for KshaUyirMei Tamil letters.
    @staticmethod
    def is_ksha_uyirmei(cp1, cp2, cp3, cp4):
        if ((cp1 == ('\u0B95')) and (cp2 == ('\u0BCD')) and (cp3 == ('\u0BB7'))):
            return TChar.is_vowel_marker(cp4)
        return False

    # Checks for presence of Sri Character.
    @staticmethod
    def is_sri(cp1, cp2, cp3, cp4):
        return ((cp1 == ('\u0BB8')) and (cp2 == ('\u0BCD')) and (cp3 == ('\u0BB0')) and (cp4 == ('\u0BC0')))

    # Checks for Ksha agaram.
    @staticmethod
    def is_ksha_agaram(cp1, cp2, cp3):
        return ((cp1 == ('\u0B95')) and (cp2 == ('\u0BCD')) and (cp3 == ('\u0BB7')))

    # Identify a Tamil Character with 4 Code Points.
    @staticmethod
    def get_TChar4(cp1, cp2, cp3, cp4):
        tc4 = cp1 + cp2 + cp3 + cp4
        if (TChar.is_ksha_uyirmei(cp1, cp2, cp3, cp4)):
            return tc4
        elif(TChar.is_sri(cp1, cp2, cp3, cp4)):
            return tc4
        else:
            return None

    # Identify a Tamil Character with 3 Code Points.
    @staticmethod
    def get_TChar3(cp1, cp2, cp3):
        tc3 = cp1 + cp2 + cp3
        if (TChar.is_ksha_agaram(cp1, cp2, cp3)):
            return tc3
        else:
            return None

    # Identify a Tamil Character with 2 Code Points.
    @staticmethod
    def get_TChar2(cp1, cp2):
        tc2 = cp1 + cp2
        if (TChar.is_uyirmei(cp1, cp2) or TChar.is_grantha_uyirmei(cp1, cp2)):
            return tc2
        else:
            return None

    # Identify a Tamil Character with 1 Code Point and allow ASCII.
    @staticmethod
    def get_TChar1(cp1):
        tc1 = cp1
        if (TChar.is_uyir(cp1) or TChar.is_agaram(cp1) or TChar.is_grantha_agaram(cp1) or TChar.is_tnumeral(cp1)
                or TChar.is_aytham(cp1) or TChar.is_tsymbol(cp1) or (ord(cp1) < 0xFF)):
            return tc1
        else:
            return None

    @staticmethod
    def get_TChar_type(utftamilchar:str) -> str:
        # Identifies character Type from CodePoints of a TamilCharacter
        CHAR_TYPE = "TYPE = "

        cpcount = len(utftamilchar)
        if (cpcount > 4):
            raise ValueError('Input value exceeded four codepoints...!')

        # A whittle down approach is followed.
        if (cpcount == 4):
            KshaUyirMeiMatch = re.search(KSHAUYIRMEI_PATTERN,  utftamilchar)
            if (KshaUyirMeiMatch):
                VM_NAME = TChar.get_vmarker_name((utftamilchar[3]))
                return CHAR_TYPE + "KSHA UYIR MEI with " + VM_NAME + " Marker"

            SriMatch = re.search(SRI_PATTERN,  utftamilchar)
            if (SriMatch):
                return CHAR_TYPE + "SRI LETTER"

        elif (cpcount == 3):
            KshaCharMatch = re.search(KSHA_PATTERN,  utftamilchar)
            if (KshaCharMatch):
                return CHAR_TYPE + "KSHA LETTER"

        elif (cpcount == 2):
            GranthaMeiMatch = re.search(GRANTHAMEI_PATTERN,  utftamilchar)
            if (GranthaMeiMatch):
                return CHAR_TYPE + "GRANTHA MEI LETTER"

            GranthaUyirMeiMatch = re.search(GRANTHAUYIRMEI_PATTERN,  utftamilchar)
            if (GranthaUyirMeiMatch):
                return CHAR_TYPE + "GRANTHA UYIR MEI LETTER"

            UyirMeiMatch = re.search(UYIRMEI_PATTERN,  utftamilchar)
            if (UyirMeiMatch):
                VM_NAME = TChar.get_vmarker_name(utftamilchar[1])
                return CHAR_TYPE + "UYIRMEI with " + VM_NAME + " Marker"

            MeiMatch = re.search(MEI_PATTERN,  utftamilchar)
            if (MeiMatch):
                VM_NAME = TChar.get_vmarker_name(utftamilchar[1])
                return CHAR_TYPE + "MEI with " + VM_NAME

        elif (cpcount == 1):
            GranthaAgaramMatch = re.search(GRANTHAAGARAM_PATTERN,  utftamilchar) 
            if (GranthaAgaramMatch):
                return CHAR_TYPE + "GRANTHA AGARAM LETTER"

            AgaramMatch = re.search(AGARAM_PATTERN,  utftamilchar)
            if (AgaramMatch):
                AGARAM_NAME = TChar.get_agaram_name(utftamilchar)
                return CHAR_TYPE + "AGARAM: " + AGARAM_NAME 

            UyirMatch = re.search(UYIR_PATTERN,  utftamilchar)
            if (UyirMatch):
                UYIR_NAME = TChar.get_uyir_name(utftamilchar)
                return CHAR_TYPE + "UYIR: " + UYIR_NAME

            AythamMatch = re.search(AYTHAM_PATTERN,  utftamilchar)
            if (AythamMatch):
                return CHAR_TYPE + "AYTHAM LETTER"

            NumeralMatch = re.search(NUMERAL_PATTERN,  utftamilchar)
            if (NumeralMatch):
                return CHAR_TYPE + "TAMIL NUMERAL"
        return "UNKNOWN CHAR TYPE...!"

    @staticmethod
    def get_vmarker_name(vmarker:str) -> str:
        # Return unicode standard descriptions of the vowelMarker.
        vmcpcount = len(vmarker)
        if(vmcpcount > 1):
            raise ValueError('Input value exceeded one codepoint for Vowel marker...!')

        if (vmarker[0] == '\u0BCD'):
            return VOWEL_MARKER_PULLI
        elif (vmarker[0] == '\u0BBE'):
            return VOWEL_MARKER_AA
        elif (vmarker[0] == '\u0BBF'):
            return VOWEL_MARKER_I
        elif (vmarker[0] == '\u0BC0'):
            return VOWEL_MARKER_II
        elif (vmarker[0] == '\u0BC1'):
            return VOWEL_MARKER_U
        elif (vmarker[0] == '\u0BC2'):
            return VOWEL_MARKER_UU
        elif (vmarker[0] == '\u0BC6'):
            return VOWEL_MARKER_E
        elif (vmarker[0] == '\u0BC7'):
            return VOWEL_MARKER_EE
        elif (vmarker[0] == '\u0BC8'):
            return VOWEL_MARKER_AI
        elif (vmarker[0] == '\u0BCA'):
            return VOWEL_MARKER_O
        elif (vmarker[0] == '\u0BCB'):
            return VOWEL_MARKER_OO
        elif (vmarker[0] == '\u0BCC'):
            return VOWEL_MARKER_AU
        return None

    @staticmethod
    def get_agaram_name(agaram:str) -> str:
        # Return unicode standard descriptions of the Agaram.
        acpcount = len(agaram)
        if(acpcount > 1):
            raise ValueError('Input value exceeded one codepoint for Agaram...!')

        if (agaram[0] == '\u0B95'):
            return AGARAM_KA
        elif (agaram[0] == '\u0B99'):
            return AGARAM_NGA
        elif (agaram[0] == '\u0B9A'):
            return AGARAM_CA
        elif (agaram[0] == '\u0B9E'):
            return AGARAM_NYA
        elif (agaram[0] == '\u0B9F'):
            return AGARAM_TTA
        elif (agaram[0] == '\u0BA3'):
            return AGARAM_NNA
        elif (agaram[0] == '\u0BA4'):
            return AGARAM_TA
        elif (agaram[0] == '\u0BA8'):
            return AGARAM_NA
        elif (agaram[0] == '\u0BAA'):
            return AGARAM_PA
        elif (agaram[0] == '\u0BAE'):
            return AGARAM_MA
        elif (agaram[0] == '\u0BAF'):
            return AGARAM_YA
        elif (agaram[0] == '\u0BB0'):
            return AGARAM_RA
        elif (agaram[0] == '\u0BB2'):
            return AGARAM_LA
        elif (agaram[0] == '\u0BB5'):
            return AGARAM_VA
        elif (agaram[0] == '\u0BB4'):
            return AGARAM_LLLA
        elif (agaram[0] == '\u0BB3'):
            return AGARAM_LLA
        elif (agaram[0] == '\u0BB1'):
            return AGARAM_RRA
        elif (agaram[0] == '\u0BA9'):
            return AGARAM_NNNA
        return None

    @staticmethod
    def get_uyir_name(uyireluthu:str) -> str:
        # Return unicode standard descriptions of the UyirEluthu.
        ucpcount = len(uyireluthu)
        if(ucpcount > 1):
            raise ValueError('Input value exceeded one codepoint for UyirEluthu...!')

        if (uyireluthu[0] == '\u0B85'):
            return UYIR_A
        if (uyireluthu[0] == '\u0B86'):
            return UYIR_AA
        elif (uyireluthu[0] == '\u0B87'):
            return UYIR_I
        elif (uyireluthu[0] == '\u0B88'):
            return UYIR_II
        elif (uyireluthu[0] == '\u0B89'):
            return UYIR_U
        elif (uyireluthu[0] == '\u0B8A'):
            return UYIR_UU
        elif (uyireluthu[0] == '\u0B8E'):
            return UYIR_E
        elif (uyireluthu[0] == '\u0B8F'):
            return UYIR_EE
        elif (uyireluthu[0] == '\u0B90'):
            return UYIR_AI
        elif (uyireluthu[0] == '\u0B92'):
            return UYIR_O
        elif (uyireluthu[0] == '\u0B93'):
            return UYIR_OO
        elif (uyireluthu[0] == '\u0B94'):
            return UYIR_AU
        return None

    @staticmethod
    def get_graphemes(utf8tamilstr:str) -> list:

        dst = []
        reslist = []

        for codepoint in utf8tamilstr:
            dst.append(codepoint)
        strlen = len(dst)
        i = 0
        # iterate on code points one by one
        while(i < strlen):
            # cp intialized to ASCII Null character
            cp1 = '\0'
            cp2 = '\0'
            cp3 = '\0'
            cp4 = '\0'
            # load code points
            if ((strlen - i) > 3):  # can load four CPs or less
                print("loading 4 ----------------" + str(i))
                cp1 = dst[i]
                cp2 = dst[i + 1]
                cp3 = dst[i + 2]
                cp4 = dst[i + 3]
                tc4 = TChar.get_TChar4(cp1, cp2, cp3, cp4)
                if (tc4 is not None):
                    #print("hit 4 -4 " + str(i))
                    reslist.append(tc4)
                    i = i + 3
                elif ((tc4 := TChar.get_TChar3(cp1, cp2, cp3)) is not None):
                    #print("hit 4 - 3 " + str(i))
                    reslist.append(tc4)
                    i = i + 2

                elif ((tc4 := TChar.get_TChar2(cp1, cp2)) is not None):
                    #print("hit 4 - 2 " + str(i))
                    reslist.append(tc4)
                    i = i + 1

                elif ((tc4 := TChar.get_TChar1(cp1)) is not None):
                    #print("hit 4 - 1 " + str(i))
                    reslist.append(tc4)
                    i = i + 0

            elif((strlen - i) > 2):  # can load three CPs or less
                print("loading 3----------------"  + " " + str(i))
                cp1 = dst[i]
                cp2 = dst[i + 1]
                cp3 = dst[i + 2]
                tc3 = TChar.get_TChar3(cp1, cp2, cp3)
                if (tc3 is not None):
                    #print("hit 3 - 3 " + str(i))
                    reslist.append(tc3)
                    i = i + 2

                elif ((tc3 := TChar.get_TChar2(cp1, cp2)) is not None):
                    #print("hit 3 - 2 " + str(i))
                    reslist.append(tc3)
                    i = i + 1

                elif ((tc3 := TChar.get_TChar1(cp1)) is not None):
                    #print("hit 3 - 1 " + str(i))
                    reslist.append(tc3)

            elif((strlen - i) > 1):  # can load remaining 2 CPs or less
                print("loading 2----------------" + " " + str(i))
                cp1 = dst[i]
                cp2 = dst[i + 1]
                tc2 = TChar.get_TChar2(cp1, cp2)
                if (tc2 is not None):
                    print("hit 2 - 2 " + str(i) + tc2)
                    reslist.append(tc2)
                    i = i + 1
                elif ((tc2 := TChar.get_TChar1(cp1)) is not None):
                    print("hit 2 - 1 " + str(i))
                    reslist.append(tc2)

            elif((strlen - i) == 1):  # can load only one CP
                print("loading 1----------------" + str(i))
                cp1 = dst[i]
                tc1 = TChar.get_TChar1(cp1)
                if (tc1 is not None):
                    #print("hit 1 - 1 " + str(i))
                    reslist.append(tc1)
            i = i + 1
        return reslist
