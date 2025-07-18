import unittest
import os
import sys
import collections
import datetime

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

print(SCRIPT_DIR)
import rounding

class KnownValues(unittest.TestCase):
    known_values_basic=[
        (123.5, 0, '124', {}),
        (-123.5, 0, '-124', {}),
        (17.456, 1, '17,5', {}),
        (-17.456, 1, '-17,5', {}),
        (123, 2, '123,00', {}),
        (-123, 2, '-123,00', {}),
        ('123.', 0, '123', {}),
        ('-123.', 0, '-123', {}),
        ('-999', -2, '-1000', {'thousands_separator':{'':''}}),
        ('999', -3, '1000', {'thousands_separator':{'':''}}),
        ]
    known_values_negative_decimal=[
        ('811', -1, '810', {}),
        ('811', -2, '800', {}),
        ('811', -3, '1000', {'thousands_separator':{'':''}}),
        ('811', -4, '0', {}),
        ('999', -1, '1000', {'thousands_separator':{'':''}}),
        ('999', -2, '1000', {'thousands_separator':{'':''}}),
        ('999', -3, '1000', {'thousands_separator':{'':''}}),
        ('-999', -1, '-1000', {'thousands_separator':{'':''}}),
        ('-999', -2, '-1000', {'thousands_separator':{'':''}}),
        ('-999', -3, '-1000', {'thousands_separator':{'':''}}),
        ('-999', -4, '0', {}),
        ]
    known_values_thousands=[
        (1234567, 0, '1 234 567', {'thousands_separator':{'':' '}}),
        (1234567, 2, '1 234 567,00', {'thousands_separator':{'':' '}}),
        (123, 1, '123,0', {'thousands_separator':{'':' '}}),
        (-123, 1, '-123,0', {'thousands_separator':{'':' '}}),
        ('1.234.567,555', 2, '1.234.567,56', {'thousands_separator':{'.':'.'}, 'decimal_separator':{',':','}}),
        (-11125, -1, '-11 130', {'thousands_separator':{'':' '}})
        ]
    known_values_specks=[
        ('.1', 0, '0', {}),
        ('-.1', 0, '0', {}),
        ]
    unknown_key = 'ahoj'

    #nactene pripady z old
    known_excel_classic_cases = []
    with open(os.path.join(SCRIPT_DIR, 'test_cases.tst'), 'r') as file:
        line = file.readline()
        if line:
            columns = line.replace('\n', '').split('\t')
            #print(columns)
            row_known_excel_classic_cases = collections.namedtuple('row_known_excel_classic_cases', columns)
            line = file.readline()
            while line:
                row = line.replace('\n', '').split('\t')
                known_excel_classic_cases.append(row_known_excel_classic_cases(row[0], row[1], row[2]))
                line = file.readline()
    
    #musi zacinat test
    def test_rounding_known_excel_classic_cases(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        #print(self.known_excel_classic_cases)
        for x, y, z in self.known_excel_classic_cases:
            result = rounding.rd(float(x), int(y))
            self.assertEqual(z, result)

    def test_rounding_known_values_basic(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        for x, y, z, kwargs in self.known_values_basic:
            result = rounding.rd(x, y, **kwargs)
            self.assertEqual(z, result)
    
    def test_rounding_known_values_negative_decimals(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        for x, y, z, kwargs in self.known_values_negative_decimal:
            result = rounding.rd(x, y, **kwargs)
            self.assertEqual(z, result)
            
    def test_rounding_known_values_thousands(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        for x, y, z, kwargs in self.known_values_thousands:
            result = rounding.rd(x, y, **kwargs)
            self.assertEqual(z, result)

    def test_rounding_known_values_specks(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        for x, y, z, kwargs in self.known_values_specks:
            result = rounding.rd(x, y, **kwargs)
            self.assertEqual(z, result)
    
    '''rd(None, 0, **{'separate_thousands':True})'''
    def test_rounding_null_value(self):
        '''rounding.rd(num, dec, kwargs) should give known result with None input'''
        self.assertEqual(rounding.rd(None, 0, **{}), '')
    
    '''TypeError: rd() got an unexpected keyword argument 'sseparate_thousands' '''
    def test_rounding_unknown_key_exception(self):
        '''rounding.rd(num, dec, kwargs) should raise TypeError with unknown key'''
        with self.assertRaises(Exception) as context:
            rounding.rd(123, 2, **{self.unknown_key: 0})
        self.assertEqual(context.exception.__class__, TypeError)
        self.assertTrue(f"rd() got an unexpected keyword argument '{self.unknown_key}'" in str(context.exception),
		f"rd() got an unexpected keyword argument '{self.unknown_key}'" + " != " + str(context.exception))

    '''ValueError: Decimal places must be an integer'''
    def test_rounding_wrong_decimal_exception(self):
        '''rounding.rd(num, dec, kwargs) should raise ValueError if decimals is not int'''
        with self.assertRaises(Exception) as context:
            rounding.rd(None, None)
        self.assertEqual(context.exception.__class__, ValueError)
        self.assertTrue(f"Decimal places must be an integer" in str(context.exception),
		f"Decimal places must be an integer" + " != " + str(context.exception))

#if __name__ == '__main__':
#    unittest.main()

# pokud neni runner tak odkrizkuj
#unittest.main(argv=[''], verbosity=2, exit=False)

runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(KnownValues)
result = runner.run(suite)

 
a = str(datetime.datetime.now()) + '\n'
a += __file__ + '\n'
a += str(result) + '\n'

if result.errors:
    a += 'result::errors' + '\n'
    for item in result.errors:
        for i in item:
            a += str(i)

if result.failures:
    a += 'result::failures' + '\n'
    for item in result.failures:
        for i in item:
            a += str(i)

if result.skipped:
    a += 'result::skipped' + '\n'
    for item in result.skipped:
        for i in item:
            a += str(i)

if result.testsRun:
    a += 'result::testsRun ' + str(result.testsRun) + '\n'

if result.wasSuccessful():
    a += 'TEST(S) SUCCESSFUL!' + '\n'
else:
    a += 'TEST(S) FAILED!!!' + '\n'

try:
    with open (os.path.join(SCRIPT_DIR,'test_results.txt'), 'r') as file:
        o = file.read()
except Exception as e:
    o = ''

with open (os.path.join(SCRIPT_DIR,'test_results.txt'), 'w') as file:
        file.write(a+'\n')
        file.write(o)
