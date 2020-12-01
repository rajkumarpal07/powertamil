import pytest

from tamil.tace16 import Tace16

def test_get_tamil_tace16_count():
    expected1 = 364
    assert(Tace16.get_tamil_tace16_count() == expected1)

def test_get_tace16_emptyspots_count():
    expected2 = 112
    assert(Tace16.get_tace16_emptyspots_count() == expected2)

def test_get_tace16_futurespots_count():
    expected3 = 84
    assert(Tace16.get_tace16_futurespots_count() == expected3)

def test_get_tamil_tace16():
    expected4 = 364
    assert(len(Tace16.get_tamil_tace16()) == expected4)

    expected5 ='\uE100'
    assert(Tace16.get_tamil_tace16().get('௳') == expected5)

    expected6 ='\uE38D'
    assert(Tace16.get_tamil_tace16().get('ஸ்ரீ') == expected6)
 
def test_to_tace16tamil():
    expected7 = '\uE201\uE210\uE25B\uE291\uE2C0' 
    assert(Tace16.to_tace16tamil('அக்டோபர்') == expected7)

    expected8 = '\uE38D\u0020\uE2C2\uE2A1\u0020\uE281\uE2E1\uE2A3' 
    assert(Tace16.to_tace16tamil('ஸ்ரீ ராம நவமி') == expected8)

    expected9 = '\uE388\uE270\uE2C2\uE251\uE321\uE2A0' 
    assert(Tace16.to_tace16tamil('க்ஷேத்ராடனம்') == expected9)

    expected10 = '\ue205\ue291\ue283\ue351\ue271\ue2a0' 
    assert(Tace16.to_tace16tamil('உபநிஷதம்') == expected10)

    expected11 = '\ue29c\ue2c0\ue261\ue2a3' 
    assert(Tace16.to_tace16tamil('பௌர்ணமி') == expected11)

    expected12 = '\ue284\ue301\ue2a0\u0020\ue201\ue211\ue2d1\ue2a0' 
    assert(Tace16.to_tace16tamil('நீளம் அகலம்') == expected12)


def test_mei_to_agaram_failing():
    with pytest.raises(ValueError, match="is not a valid TACE16 codepoint"):
        Tace16.to_utf8tamil('\uF284\uF301\uF2a0')













