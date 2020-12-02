# encoding: utf-8
# (C) 2001 - 2020 Rajkumar Palani <rajkumarpalani07@gmail.com>

import pytest

from tamil import tstring

def test_reverse():
    expected1 = 'ர்படோக்அ'
    output1 = tstring.reverse('அக்டோபர்')
    assert(output1 == expected1)

def test_length():
    assert(tstring.length('அக்டோபர்') == 5)

def test_substring(): #அக்டோபர்பார்ன்பாய்
    expected1 = 'அக்டோபர்'
    output1 = tstring.substring('அக்டோபர்பார்ன்பாய்', 0, 5)
    assert(output1 == expected1)

def test_replace():# அக்டோபர்பார்ன்ராஜ்குமார்
    expected1 = 'அக்டோப-பா-ன்ராஜ்குமா-'
    output1 = tstring.replace('அக்டோபர்பார்ன்ராஜ்குமார்', 'ர்', '-')
    assert(output1 == expected1)

def test_compare_lexicaly():
    result = tstring.compare_lexicaly('அப்பா', 'அம்மா')
    assert(result < 0)

    result = tstring.compare_lexicaly('அம்மா', 'அப்பா')
    assert(result > 0)

    result = tstring.compare_lexicaly('அம்மா', 'அம்மா')
    assert(result == 0)