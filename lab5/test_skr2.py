from skr2 import get_bit_value

def test_get_bit_value1():
    assert get_bit_value(0, 0) == 0
    assert get_bit_value(1, 0) == 1
    assert get_bit_value(2, 0) == 0
    assert get_bit_value(2, 1) == 1
    assert get_bit_value(255, 7) == 1

    
def test_get_bit_value2():
    assert get_bit_value(263, 1) == 0

def test_get_bit_value3():
    assert get_bit_value(0, 0) == 0
    assert get_bit_value(0, 8) == 0
    
def test_get_bit_value4():
    assert get_bit_value(0, 0) == 1