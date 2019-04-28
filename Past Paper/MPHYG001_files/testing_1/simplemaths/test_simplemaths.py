from pytest import raises
from simplemaths.simplemaths import SimpleMaths as sm
import math

class TestSimpleMaths():
    def test_input_float(self):
        with raises(ValueError) as exception: 
            test=sm(3.)
    
    def test_input_string(self):
        with raises(ValueError) as exception: 
            test=sm('3')
    
    def test_input_bool(self):
        with raises(ValueError) as exception: 
            test=sm(True)
    
    def test_input_complex(self):
        with raises(ValueError) as exception: 
            test=sm(3j)

    def test_square(self):
        for num in range(5):
            test=sm(num)
            assert test.square() == num**2

    def test_factorial(self):
        for num in range(5):
            test=sm(num)
            assert test.factorial() == math.factorial(num)

    def test_power(self):
        for num in range(5):
            test=sm(num)
            assert test.power() == num**3
            for x in range(5):
                assert test.power(x) == num**x

    def test_parity(self):
        for num in range(5):
            test=sm(2*num)
            assert test.odd_or_even() == 'Even'
            test=sm(2*num+1)
            assert test.odd_or_even() == 'Odd'

    def test_root(self):
        for num in range(5):
            test=sm(num)
            assert test.square_root() == math.sqrt(num)
    
    pass
