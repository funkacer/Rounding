import sys
import traceback

from src.rounding import rd
from src.check_input import check_input

def main(argv):
    #print(argv)

    number_str, precision_str = None, None

    try:
        number_str = argv[0]
    except IndexError:
        #traceback.print_exc()
        pass
    except Exception as e:
        #traceback.print_exc()
        pass

    try:
        precision_str = argv[1]
    except IndexError:
        #traceback.print_exc()
        pass
    except Exception as e:
        #traceback.print_exc()
        pass

    number, precision = None, None

    try:
        number = float(number_str)
        #print(number)
    except Exception as e:
        print('Usage: python -m rounding_interactive number, precision\n')
        print("Entering interactive mode.\n")
        #traceback.print_exc()

    try:
        precision = int(precision_str)
    except Exception as e:
        if number is not None:
            precision = 0
            print('Precision not specified, using 0.\n')
        #traceback.print_exc()

    if number is not None and precision is not None:
        print(f'Rounding number {number} with precision {precision}: ' + rd(number, precision) + '\n')
        print("Entering interactive mode.\n")
        answer = ''
        while answer not in ['yes','no']:
            answer = input("Do you want to continue? (yes, no):\n").lower()
            answer = check_input(answer, ['yes','no'])
        if answer != 'yes':
            return None

    answer = 'yes'

    while answer == 'yes':

        number, precision = None, None

        while number is None:
            number_str = input('Please enter a number to round (float or int):\n')
            try:
                #number = float(number_str)
                number = number_str
                print()
                #print(number)
            except Exception as e:
                print('Please enter valid number\n')
                #traceback.print_exc()

        while precision is None:
            precision_str = input('Please enter a precision(int):\n')
            try:
                #precision = int(precision_str)
                precision = precision_str
                print('')
                #print(precision)
            except Exception as e:
                precision = 0
                print('Precision not specified, using 0.\n')
                #traceback.print_exc()

        if number is not None and precision is not None:
            if precision == '':
                try:
                    print(f'Rounding number {number} with no precision given: ' + rd(number) + '\n')
                except Exception as e:
                    traceback.print_exc()
            else:
                try:
                    print(f'Rounding number {number} with precision {precision}: ' + rd(number, precision) + '\n')
                except Exception as e:
                    traceback.print_exc()

        answer = ''
        while answer not in ['yes','no']:
            answer = input("Do you want to continue? (yes, no):\n").lower()
            answer = check_input(answer, ['yes','no'])

if __name__ == '__main__':
    main(sys.argv[1:])
