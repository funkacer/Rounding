# JC
import sys
import traceback

from src._rounding import rd

def main(argv):
    #print(argv)
    try:
        number = float(argv[0])
        #print(number)
    except IndexError:
        print('Usage: python -m main number, precision')
        return None
    except Exception as e:
        traceback.print_exc()
        print('Usage: python -m main number, precision')
        return None

    try:
        precision = int(argv[1])
    except IndexError:
        precision = 0
        print('Precision not specified, using 0')
    except Exception as e:
        traceback.print_exc()
        print('Usage: python -m main number, precision')
        return None

    print(f'Rounding number {number} with precision {precision}:', rd(number, precision))

if __name__ == '__main__':
    main(sys.argv[1:])
