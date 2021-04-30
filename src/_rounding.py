def rd(number: float, precision: int = 0) -> str:
    '''
    Returns rounded string with defined precicion.
    
    INPUT:
    number: float, to be rounded
    precision: int, precision used whe rounding
    
    OUTPUT:
    round_str: str
    '''
    fin = 1
    if number < 0: fin = -1      
    number1 = number*10**(precision)
    if abs(number1 - int(number1)) >= .5:
        number1 += fin
    round_float = int(number1)/10**(precision)
    round_str = '{num:.{prec}f}'.format(num=round_float,prec=precision)
    return round_str
