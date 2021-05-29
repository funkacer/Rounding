import sys
import traceback

def rd(number: float, precision: int = 0) -> str:
    '''
    Returns rounded string with defined precicion.

    INPUT:
    number: float, to be rounded
    precision: int, precision used whe rounding

    OUTPUT:
    round_str: str
    '''
    num, prec = None, None

    if isinstance(number, float):
        num = number
    else:
        try:
            num = float(number)
        except Exception as e:
            #traceback.print_exc()
            pass

    if isinstance(precision, int):
        if precision >= 0:
            prec = precision
        else:
            prec = abs(precision)
    else:
        try:
            prec = abs(int(precision))
        except Exception as e:
            #traceback.print_exc()
            pass

    assert num is not None, '\nPlease specify valid number\n'
    assert prec is not None, '\nPlease specify valid precision\n'

    fin = 1
    if num < 0: fin = -1
    num1 = num*10**prec
    if abs(num1 - int(num1)) >= .5:
        num1 += fin
    round_float = int(num1)/10**prec
    round_str = '{num:.{prec}f}'.format(num=round_float,prec=prec)
    return round_str


def main(argv):
    #print(argv)

    number, precision = None, None

    try:
        number = argv[1]
    except IndexError:
        filename = sys.argv[0].split('\\')[-1].split('.')[0]
        print('\nUsage: python -m ' +  filename + ' number, precision\n')
        #traceback.print_exc()
        return None
    except Exception as e:
        #traceback.print_exc()
        pass

    try:
        precision = argv[2]
    except IndexError:
        precision = 0
        print('\nPrecision not specified, using 0.')
        #traceback.print_exc()
        pass
    except Exception as e:
        #traceback.print_exc()
        pass

    print(f'\nRounding number {number} with precision {precision}: ' + rd(number, precision) + '\n')

if __name__ == '__main__':
    main(sys.argv)
