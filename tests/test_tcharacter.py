# encoding: utf-8
# (C) 2001 - 2020 Rajkumar Palani <rajkumarpalani07@gmail.com>

import pytest

from tamil.tcharacter import TChar

def test_is_vowel_marker():
    assert(TChar.is_vowel_marker('\u0BC0') == True)
    assert(TChar.is_vowel_marker('அ') == False)
    assert(TChar.is_vowel_marker('A') == False)

def test_is_agaram():
    assert(TChar.is_agaram('\u0BC0') == False)
    assert(TChar.is_agaram('\u0BA4') == True)
    assert(TChar.is_agaram('A') == False)
    assert(TChar.is_agaram('ப') == True)

def test_is_uyir():
    assert(TChar.is_uyir('\u0B8E') == True)
    assert(TChar.is_uyir('அ') == True)
    assert(TChar.is_uyir('A') == False)

def test_is_mei():
    assert(TChar.is_mei('க', '\u0BCD') == True)
    assert(TChar.is_mei('அ', '\u0BCD') == False)
    assert(TChar.is_mei('A', '\u0BCD') == False)

def test_is_uyirmei():
    assert(TChar.is_uyirmei('க', '\u0BCD') == True)
    assert(TChar.is_uyirmei('க', '\u0BC7') == True)
    assert(TChar.is_uyirmei('A', '\u0BCD') == False)

def test_is_aytham():
    assert(TChar.is_aytham('ஃ') == True)
    assert(TChar.is_aytham('A') == False)
    assert(TChar.is_aytham('2') == False)
    assert(TChar.is_aytham('') == False)

def test_is_tnumeral():
    assert(TChar.is_tnumeral('௬') == True)
    assert(TChar.is_tnumeral('0') == False)
    assert(TChar.is_tnumeral('A') == False)

def test_is_tnumeral_failing():
    with pytest.raises(TypeError, match = "Input value is empty"):
        TChar.is_tnumeral('')

def test_is_tsymbol():
    assert(TChar.is_tsymbol('௵') == True)
    assert(TChar.is_tsymbol('௬') == False)
    assert(TChar.is_tsymbol('0') == False)

def test_is_tsymbol_failing():
    with pytest.raises(TypeError, match = "Input value is empty"):
        TChar.is_tsymbol('')

def test_is_grantha_agaram():
    assert(TChar.is_grantha_agaram('\u0BB6') == True)
    assert(TChar.is_grantha_agaram('௵') == False)
    assert(TChar.is_grantha_agaram('') == False)

def test_is_grantha_uyirmei():
    assert(TChar.is_grantha_uyirmei('\u0B9C', '\u0BC7') == True)
    assert(TChar.is_grantha_uyirmei('௵', '\u0BC7') == False)
    assert(TChar.is_grantha_uyirmei('', '') == False)

def test_is_all_grantha_uyirmei():
    assert(TChar.is_all_grantha_uyirmei('\u0B9C', '\u0BC7', None, None) == True)
    assert(TChar.is_all_grantha_uyirmei('\u0B95', '\u0BCD', '\u0BB7', '\u0BC8') == True) # க்ஷை

def test_is_ksha_uyirmei():
    assert(TChar.is_ksha_uyirmei('\u0B95', '\u0BCD', '\u0BB7', '\u0BC8') == True) # க்ஷை
    assert(TChar.is_ksha_uyirmei('\u0B9C', '\u0BC7', None, None) == False)

def test_is_sri():
    assert(TChar.is_sri('\u0BB8', '\u0BCD', '\u0BB0', '\u0BC0') == True) # ஸ்ரீ
    assert(TChar.is_sri('\u0B9C', '\u0BC7', None, None) == False)

def test_is_ksha_agaram():
    assert(TChar.is_ksha_agaram('\u0B95', '\u0BCD', '\u0BB7') == True) # க்ஷ
    assert(TChar.is_ksha_agaram('\u0B9C', '\u0BC7', None) == False) # க்ஷை

def test_get_TChar4():
    assert(TChar.get_TChar4('\u0BB8', '\u0BCD', '\u0BB0', '\u0BC0') == 'ஸ்ரீ') # ஸ்ரீ
    assert(TChar.get_TChar4('\u0B9C', '\u0BC7', '\u0BCD', '\u0BB7') == None)

def test_get_TChar3():
    assert(TChar.get_TChar3('\u0B95', '\u0BCD', '\u0BB7') == 'க்ஷ') # க்ஷ
    assert(TChar.get_TChar3('\u0B9C', '\u0BC7', '\u0BCD') == None)

def test_get_TChar2():
    assert(TChar.get_TChar2('ச', '\u0BC8') == 'சை') # சை
    assert(TChar.get_TChar2('\u0B9C', '\u0BC7') == 'ஜே')

def test_get_TChar1():
    assert(TChar.get_TChar1('\u0B9A') == 'ச') # ச
    assert(TChar.get_TChar1('A') == 'A')
    assert(TChar.get_TChar1('ஃ') == 'ஃ')
    assert(TChar.get_TChar1('Ж') == None)

def test_get_TChar_type():
    output1 = TChar.get_TChar_type('\u0B95\u0BCD\u0BB7\u0BC8') # க்ஷை
    assert ('TYPE = KSHA UYIR MEI with AI Marker' == output1)
    output2 = TChar.get_TChar_type('ஜ்') # ஜ்
    assert ('TYPE = GRANTHA MEI LETTER' == output2)
    output3 = TChar.get_TChar_type('ஜி') # ஜி
    assert ('TYPE = GRANTHA UYIR MEI LETTER' == output3)
    output4 = TChar.get_TChar_type('னி') # னி
    assert ('TYPE = UYIRMEI with I Marker' == output4)
    output5 = TChar.get_TChar_type('ச்') # ச்
    assert ('TYPE = MEI with PULLI' == output5)
    output6 = TChar.get_TChar_type('ஃ') # ஃ
    assert ('TYPE = AYTHAM LETTER' == output6)
    output7 = TChar.get_TChar_type('௬') # ௬
    assert ('TYPE = TAMIL NUMERAL' == output7)
    output8 = TChar.get_TChar_type('Ж') # Ж
    assert ('UNKNOWN CHAR TYPE...!' == output8)

def test_get_TChar_type_failing():
    with pytest.raises(ValueError, match = "Input value exceeded four codepoints"):
        TChar.get_TChar_type('Llama')
        TChar.get_TChar_type('அக்டோபர்')

def test_get_vmarker_name():
    expected1 = 'II'
    assert (TChar.get_vmarker_name('\u0BC0') == expected1)
    assert (TChar.get_vmarker_name('Ж') == None)

def test_get_vmarker_name_failing():
    with pytest.raises(ValueError, match = "Input value exceeded one codepoint for Vowel marker"):
        TChar.get_vmarker_name('ச்')
        TChar.get_vmarker_name('அக்டோபர்')

def test_get_agaram_name():
    expected1 = 'TAMIL LETTER CA'
    assert (TChar.get_agaram_name('ச') == expected1)
    assert (TChar.get_agaram_name('Ж') == None)

def test_get_agaram_name_failing():
    with pytest.raises(ValueError, match = "Input value exceeded one codepoint for Agaram"):
        TChar.get_agaram_name('ச்')
        TChar.get_agaram_name('அக்டோபர்')

def test_get_uyir_name():
    expected1 = 'TAMIL LETTER AA'
    assert (TChar.get_uyir_name('ஆ') == expected1)
    assert (TChar.get_uyir_name('Ж') == None)

def test_get_uyir_name_failing():
    with pytest.raises(ValueError, match = "Input value exceeded one codepoint for UyirEluthu"):
        TChar.get_uyir_name('ச்')
        TChar.get_uyir_name('அக்டோபர்')

def test_get_graphemes():
    expected1 = []
    expected1.append('அ')
    expected1.append('க்')
    expected1.append('டோ')
    expected1.append('ப')
    expected1.append('ர்')

    output = TChar.get_graphemes('அக்டோபர்')

    assert (output == expected1)

