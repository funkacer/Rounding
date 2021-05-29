import unittest
import importlib.util
import sys
import os
import datetime
import numpy as np

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

def rdv(x,y=0):
    ''' A classical mathematical rounding by Voznica '''
    try:
        fin = 1
        if x < 0: fin = -1
        m = int('1'+'0'*y) # multiplier - how many positions to the right
        q = abs(x)*m # shift to the right by multiplier
        c = int(q) # new number
        i = int( (q-c)*10 ) # indicator number on the right
        if i >= 5:
            c += 1
        c *= fin
        result = '{num:.{prec}f}'.format(num=c/m,prec=y)
    except:
        result = ''
    return result

#print(rdv(12.5))

class TestRounding(unittest.TestCase):

    with open ('Known_results.tst', 'r') as f:
        dic = {}
        columns = f.readline().split()
        for col in columns:
            dic[col] = []
        while True:
            try:
                values = f.readline().split()
                assert len(columns) == len(values), print('Error in reading more values: {}'.format(values))
                for i, col in enumerate(columns):
                    dic[col].append(values[i])
            except:
                print('Reading completed.')
                break

    test_cases = list(zip(*[value for value in dic.values()]))

    #print(test_cases)

    def test_known_cases(self):

        from src.rounding import rd

        for number, precision, result in self.test_cases:
            try:
                number, precision, result = float(number), int(precision), float(result)
            except:
                number, precision, result = None, None, None
            #print('Number {}, precision {}, excel_result {}, float(rd_result) {}, rd_result {}'.format(number,precision,result, float(rd(number, precision)), rd(number, precision)))

            rounded = rd(number, precision)
            self.assertIsInstance(rounded, str)
            self.assertEqual(float(rounded), result)


    def test_random_cases(self):

        from src.rounding import rd

        result = 0
        while result == 0:
            for i in range(1000):
                a = np.random.random()*10 - 5
                b = np.random.randint(0,3)
                c = rd(a,b)
                #print('Number {}, precision {}, float(rd_result) {}, rd_result {}, rv_result {}'.format(a ,b ,float(rd(a, b)), rd(a, b), rdv(a, b)))
                self.assertIsInstance(rd(a, b), str)
                self.assertEqual(rd(a, b), rdv(a, b))
                self.assertEqual(float(rd(a, b)), float(rdv(a, b)))
                if abs(a) < 0.1 and a < 0 and b == 0:
                    print('Number {}, precision {}, float(rd_result) {}, rd_result {}, rdv_result {}'.format(a, b ,float(rd(a, b)), rd(a, b), rdv(a, b)))
                    result=1

        print('Number {}, precision {}, float(rd_result) {}, rd_result {}, rdv_result {}'.format(a, b ,float(rd(a, b)), rd(a, b), rdv(a, b)))


    def test_str_number(self):

        from src.rounding import rd

        number = 'a'
        precision = 0
        self.assertIsInstance(rd(number), str)
        self.assertIsInstance(rd(number, precision), str)


    def test_str_precision(self):

        from src.rounding import rd

        number = 1.1
        precision = 'a'
        self.assertIsInstance(rd(number, precision), str)


    def test_negative_precision(self):

        from src.rounding import rd

        number = 1.1
        precision = -2
        self.assertIsInstance(rd(number, precision), str)

    def test_none_number(self):

        from src.rounding import rd

        number = None
        self.assertIsInstance(rd(number), str)

    def test_none_precision(self):

        from src.rounding import rd

        number = 1.1
        precision = None
        self.assertIsInstance(rd(number, precision), str)

    def test_no_precision(self):

        from src.rounding import rd

        number = 1.1
        precision = None
        self.assertIsInstance(rd(number), str)


runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(TestRounding)
result = runner.run(suite)

print ("---- START OF TEST RESULTS")
print (result)

print ("result::errors")
print (result.errors)

print ("result::failures")
print (result.failures)

print ("result::skipped")
print (result.skipped)

print ("result::successful")
print (result.wasSuccessful())

print ("result::test-run")
print (result.testsRun)
print ("---- END OF TEST RESULTS")

a = str(result)

with open ('rounding_test_results.txt', 'w') as file:
    file.write(str(datetime.datetime.now())+'\n')
    file.write(a)
