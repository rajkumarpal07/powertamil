import pytest

from tamil import utf8

def test_get_tamil_utf_count():
    expected = 364
    assert(utf8.get_tamil_utf_count() == expected)


def test_get_tamil_utf():
    expected = 364
    assert(len(utf8.get_tamil_utf()) == expected)

    temp1 = list(filter(lambda x: (x == 'அ'), utf8.get_tamil_utf()))
    assert(('அ' in temp1[0]) == True)


def test_validate_char():
    input1 = "ட"
    assert(utf8.validate_char(input1) == True)
    input2 = 'அ'
    assert(utf8.validate_char(input2) == True)
    

def test_validate_char_failing():
    input1 = 1000
    with pytest.raises(TypeError, match="Input value must be unicode string"):
        utf8.validate_char(input1)

    input2 = ''
    with pytest.raises(ValueError, match="Input value is empty"):
        utf8.validate_char(input2)

    input3 = 'Ж'
    with pytest.raises(ValueError, match="Input value is not a valid utf8 tamil character"):
        utf8.validate_char(input3)











