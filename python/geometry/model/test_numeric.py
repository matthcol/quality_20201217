from decimal import Decimal
import numpy as np

def test_price_float():
    # given
    price = 0.1 # base 2: 0.000110011001100..
    expected_total = (0.2, 0.3)
    # when
    result_total = (2*price, 3*price)
    # then
    assert result_total == expected_total

def test_price_decimal():
    # given
    price = Decimal('0.1') # base 2: 0.000110011001100..
    expected_total = (Decimal('0.2'), Decimal('0.3'))
    # when
    result_total = (2*price, 3*price)
    # then
    assert result_total == expected_total
    
def test_integers_modulo():
    # given
    values = np.zeros(10, dtype='uint8') # 0-255
    # when : wrong usage
    values += 250
    values += 20 # overflow (modulo 256)
    # then 
    assert all(values == 270)
    
    
    
    
    
    
    
    
    
    
