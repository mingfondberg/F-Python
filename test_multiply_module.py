from multiply_module import multiply_two_numbers

def test_multiply():
    assert multiply_two_numbers(2, 3) == 6
    assert multiply_two_numbers(-1, 5) == -5
    assert multiply_two_numbers(0, 100) == 0
    assert multiply_two_numbers(4, 2.5) == 10.0
    