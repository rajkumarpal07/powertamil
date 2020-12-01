# encoding: utf-8
# (C) 2001 - 2020 Rajkumar Palani <rajkumarpalani07@gmail.com>


from itertools import chain


# Tamil Symbols
Tamil_Symbols = [u"௳", u"௴", u"௵", u"௶", u"௷", u"௸", u"௹", u"௺",
                u"பௌர்ணமி", u"அமாவாசை", u"கார்த்திகை", u"ராஜ", u"ௐ"]

Tamil_Numerals = [u"௦", u"௧", u"௨", u"௩", u"௪",
                u"௫", u"௬", u"௭", u"௮", u"௯", u"௰", u"௱", u"௲"]

# DONT use Fractions for now
Tamil_Fractions = [u"அரைக்கால்", u"கால்", u"அரை", u"முக்கால்", u"அரைவீசம்", u"வீசம்",
                u"மூவீசம்", u"அரைமா", u"ஒருமா", u"இரண்டுமா", u"மும்மா", u"நாலுமா",
                u"முந்திரி", u"அரைக்காணி", u"காணி", u"முக்காணி"]

Vowel_Markers = [u"்", u"ா", u"ி", u"ீ", u"ு", u"ூ",
                u"ெ", u"ே", u"ை", u"ொ", u"ோ", u"ௌ"]


Indian_Rupee = u"₹"


# Tamil Letters

# Letter :: அ
# UTF-8 (hex) 	0xE0 0xAE 0x85 (E0AE85)
# UTF-8 (binary) 	11100000:10101110:10000101
# UTF-16 (hex) 	0x0B85 (0b85)
# UTF-16 (decimal) 	2,949


Aytham_Letter = [u"ஃ"]

Uyir_Letters = [u"அ", u"ஆ", u"இ", u"ஈ", u"உ", u"ஊ",
                u"எ", u"ஏ", u"ஐ", u"ஒ", u"ஓ", u"ஔ"]


Mei_Letters = [u"க்", u"ங்", u"ச்", u"ஞ்", u"ட்", u"ண்", u"த்", u"ந்", u"ப்",
            u"ம்", u"ய்", u"ர்", u"ல்", u"வ்", u"ழ்", u"ள்", u"ற்", u"ன்"]

Grantha_Mei_Letters = [u"ஜ்", u"ஶ்", u"ஷ்", u"ஸ்", u"ஹ்", u"க்ஷ்"]

# Uyir Mei

KA_Uyir_Mei = [u"க", u"கா", u"கி", u"கீ", u"கு", u"கூ",
            u"கெ", u"கே", u"கை", u"கொ", u"கோ", u"கௌ"]

NGA_Uyir_Mei = [u"ங", u"ஙா", u"ஙி", u"ஙீ", u"ஙு", u"ஙூ",
                u"ஙெ", u"ஙே", u"ஙை", u"ஙொ", u"ஙோ", u"ஙௌ"]

CA_Uyir_Mei = [u"ச", u"சா", u"சி", u"சீ", u"சு", u"சூ",
            u"செ", u"சே", u"சை", u"சொ", u"சோ", u"சௌ"]

NYA_Uyir_Mei = [u"ஞ", u"ஞா", u"ஞி", u"ஞீ", u"ஞு", u"ஞூ",
                u"ஞெ", u"ஞே", u"ஞை", u"ஞொ", u"ஞோ", u"ஞௌ"]

TTA_Uyir_Mei = [u"ட", u"டா", u"டி", u"டீ", u"டு", u"டூ",
                u"டெ", u"டே", u"டை", u"டொ", u"டோ", u"டௌ"]

NNNA_Uyir_Mei = [u"ண", u"ணா", u"ணி", u"ணீ", u"ணு", u"ணூ",
                u"ணெ", u"ணே", u"ணை", u"ணொ", u"ணோ", u"ணௌ"]

TA_Uyir_Mei = [u"த", u"தா", u"தி", u"தீ", u"து", u"தூ",
            u"தெ", u"தே", u"தை", u"தொ", u"தோ", u"தௌ"]

NA_Uyir_Mei = [u"ந", u"நா", u"நி", u"நீ", u"நு", u"நூ",
            u"நெ", u"நே", u"நை", u"நொ", u"நோ", u"நௌ"]

PA_Uyir_Mei = [u"ப", u"பா", u"பி", u"பீ", u"பு", u"பூ",
            u"பெ", u"பே", u"பை", u"பொ", u"போ", u"பௌ"]

MA_Uyir_Mei = [u"ம", u"மா", u"மி", u"மீ", u"மு", u"மூ",
            u"மெ", u"மே", u"மை", u"மொ", u"மோ", u"மௌ"]

YA_Uyir_Mei = [u"ய", u"யா", u"யி", u"யீ", u"யு", u"யூ",
            u"யெ", u"யே", u"யை", u"யொ", u"யோ", u"யௌ"]

RA_Uyir_Mei = [u"ர", u"ரா", u"ரி", u"ரீ", u"ரு", u"ரூ",
            u"ரெ", u"ரே", u"ரை", u"ரொ", u"ரோ", u"ரௌ"]

LA_Uyir_Mei = [u"ல", u"லா", u"லி", u"லீ", u"லு", u"லூ",
            u"லெ", u"லே", u"லை", u"லொ", u"லோ", u"லௌ"]

VA_Uyir_Mei = [u"வ", u"வா", u"வி", u"வீ", u"வு", u"வூ",
            u"வெ", u"வே", u"வை", u"வொ", u"வோ", u"வௌ"]

LLLA_Uyir_Mei = [u"ழ", u"ழா", u"ழி", u"ழீ", u"ழு", u"ழூ",
                u"ழெ", u"ழே", u"ழை", u"ழொ", u"ழோ", u"ழௌ"]

LLA_Uyir_Mei = [u"ள", u"ளா", u"ளி", u"ளீ", u"ளு", u"ளூ",
                u"ளெ", u"ளே", u"ளை", u"ளொ", u"ளோ", u"ளௌ"]

RRA_Uyir_Mei = [u"ற", u"றா", u"றி", u"றீ", u"று", u"றூ",
                u"றெ", u"றே", u"றை", u"றொ", u"றோ", u"றௌ"]

NNA_Uyir_Mei = [u"ன", u"னா", u"னி", u"னீ", u"னு", u"னூ",
                u"னெ", u"னே", u"னை", u"னொ", u"னோ", u"னௌ"]

# Grantha Uyir Mei
JHA_Uyir_Mei = [u"ஜ", u"ஜா", u"ஜி", u"ஜீ", u"ஜு", u"ஜூ",
                u"ஜெ", u"ஜே", u"ஜை", u"ஜொ", u"ஜோ", u"ஜௌ"]

SA_Uyir_Mei = [u"ஶ", u"ஶா", u"ஶி", u"ஶீ", u"ஶு", u"ஶூ",
            u"ஶெ", u"ஶே", u"ஶை", u"ஶொ", u"ஶோ", u"ஶௌ"]

SHA_Uyir_Mei = [u"ஷ", u"ஷா", u"ஷி", u"ஷீ", u"ஷு", u"ஷூ",
                u"ஷெ", u"ஷே", u"ஷை", u"ஷொ", u"ஷோ", u"ஷௌ"]

SSA_Uyir_Mei = [u"ஸ", u"ஸா", u"ஸி", u"ஸீ", u"ஸு", u"ஸூ",
                u"ஸெ", u"ஸே", u"ஸை", u"ஸொ", u"ஸோ", u"ஸௌ"]

HA_Uyir_Mei = [u"ஹ", u"ஹா", u"ஹி", u"ஹீ", u"ஹு", u"ஹூ",
            u"ஹெ", u"ஹே", u"ஹை", u"ஹொ", u"ஹோ", u"ஹௌ"]

KSHA_Uyir_Mei = [u"க்ஷ", u"க்ஷா", u"க்ஷி", u"க்ஷீ", u"க்ஷு", u"க்ஷூ",
                u"க்ஷெ", u"க்ஷே", u"க்ஷை", u"க்ஷொ", u"க்ஷோ", u"க்ஷௌ"]

SRI_Uyir_Mei = ["ஸ்ரீ"]


# List formations follow.
UyirMei_List = list(chain(KA_Uyir_Mei, NGA_Uyir_Mei, CA_Uyir_Mei,
                        NYA_Uyir_Mei, TTA_Uyir_Mei, NNNA_Uyir_Mei, TA_Uyir_Mei, NA_Uyir_Mei,
                        PA_Uyir_Mei, MA_Uyir_Mei, YA_Uyir_Mei, RA_Uyir_Mei, LA_Uyir_Mei,
                        VA_Uyir_Mei, LLLA_Uyir_Mei, LLA_Uyir_Mei, RRA_Uyir_Mei, NNA_Uyir_Mei))

GranthaUyirMei_List = list(chain(JHA_Uyir_Mei, SA_Uyir_Mei, SHA_Uyir_Mei,
                                SSA_Uyir_Mei, HA_Uyir_Mei, KSHA_Uyir_Mei))


# Form a Union of all Tamil characters except fractions.
# order of addition is determined in TACE-16 order.
AllTAM_List = []
AllTAM_List = list(chain(Tamil_Symbols, Vowel_Markers, Tamil_Numerals, Aytham_Letter, Uyir_Letters,
                        Mei_Letters, Grantha_Mei_Letters, UyirMei_List, GranthaUyirMei_List, SRI_Uyir_Mei))


# Tamil_Symbols + VMarkers + Numerals + Aytham + Uyir + Mei + GranthaMei + UyirMei + GranthaUyirMei + Sri = 364
# TOTAL_TAM_LETTERS = 13 + 12 + 13 + 1 + 12 + 18 + 6 + 12*18(216) + 6*12(72) + 1 = 364


# 364
def get_tamil_utf_count():
    return len(AllTAM_List)

def get_tamil_utf():
    return AllTAM_List

def validate_char(utf8char:str) -> bool:
    # Validation for the utf8 tamil char.
    if(not isinstance(utf8char, str)):
        raise TypeError('Input value must be unicode string....!')
    if(len(utf8char) > 4 or len(utf8char) < 1):
        raise ValueError('Input value is empty or has more than 4 codepoints...!')
    
    validTChar = False
    for val in (utf8char):
        if (val in AllTAM_List):
            validTChar = True
        else:
            raise ValueError('Input value is not a valid utf8 tamil character...!')
    return validTChar

