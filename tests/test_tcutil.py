# encoding: utf-8
# (C) 2001 - 2020 Rajkumar Palani <rajkumarpalani07@gmail.com>

import pytest

from tamil import tcutil

def test_is_vallinam():
    assert(tcutil.is_vallinam('ச்'))
    assert(tcutil.is_vallinam('அ') == False)

def is_mellinam():
    assert(tcutil.is_mellinam('ஞ்'))
    assert(tcutil.is_mellinam('அ') == False)

def test_is_idaiyinam():
    assert(tcutil.is_idaiyinam('ர்'))
    assert(tcutil.is_idaiyinam('அ') == False)

def test_is_grantham():
    assert(tcutil.is_grantham('ஷ்'))
    assert(tcutil.is_grantham('அ') == False)

def test_is_kuril():
    assert(tcutil.is_kuril('இ'))
    assert(tcutil.is_kuril('ஷ') == False)

def test_is_nedil():
    assert(tcutil.is_nedil('ஈ'))
    assert(tcutil.is_nedil('ஷ') == False)

def test_is_tamil():
    assert(tcutil.is_tamil('ஈ'))
    assert(tcutil.is_tamil('A') == False)    

def test_mei_to_agaram():
    expected1 = 'க'
    assert(tcutil.mei_to_agaram('க்') == expected1)
    expected2 = 'க்ஷ'
    assert(tcutil.mei_to_agaram('க்ஷ்') == expected2)
    expected3 = 'ஸ'
    assert(tcutil.mei_to_agaram('ஸ்') == expected3)
    expected4 = None
    assert(tcutil.mei_to_agaram('ஸ்ரீ') == expected4)

def test_mei_to_agaram_failing():
    with pytest.raises(ValueError, match = "Input value for mei less than two codepoints"):
        tcutil.mei_to_agaram('ஃ')

    with pytest.raises(ValueError, match = "Input value for mei less than two codepoints"):
        tcutil.mei_to_agaram('A')

def test_get_uyirmei():
    expected1 = 'க'
    assert(tcutil.get_uyirmei('அ', 'க்') == expected1)
    expected2 = 'கை'
    assert(tcutil.get_uyirmei('ஐ', 'க்') == expected2)
    expected3 = None
    assert(tcutil.get_uyirmei('A', 'க்') == expected3)
    expected4 = None
    assert(tcutil.get_uyirmei('A', '**') == expected4)

def test_get_uyirmei_failing():
    with pytest.raises(ValueError, match = "Input value for mei is not two codepoints"):
        tcutil.get_uyirmei('அ', 'க')

def test_is_controlcode():
    assert(tcutil.is_controlcode('\a') == True)
    assert(tcutil.is_controlcode('\b') == True)
    assert(tcutil.is_controlcode('\t') == True)
    assert(tcutil.is_controlcode('\r') == True)

def test_is_tamilonly():
    assert(tcutil.is_tamilonly('அக்டோபர்பார்ன்') == True)
    assert(tcutil.is_tamilonly('அக்டோபர்பார்ன்!') == True)
    assert(tcutil.is_tamilonly('அக்டோபர் பார்ன்') == True)
    assert(tcutil.is_tamilonly('அக்டோபர் பார்ன் OCTOBER BORN') == False)
    assert(tcutil.is_tamilonly('OCTOBER BORN') == False)

def test_is_tamilonly_failing():
    with pytest.raises(ValueError, match = "Input value is empty"):
        tcutil.is_tamilonly('') 

