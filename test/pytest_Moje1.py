import unittest

def moje(i):
    return str(i)

class TestMoje(unittest.TestCase):

    testcases = [1,2,3,4,5,'a']

    def test_moje_formats(self):
        for i in self.testcases:
            self.assertIsInstance(int(moje(i)), int)
            self.assertIsInstance(moje(i), str)
            
    def test_moje_shode(self):
        for i in self.testcases:
            self.assertEqual(i, int(moje(i)),\
             'Chyba!!!')
            
    
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMoje)
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

with open ('moje1.txt', 'w') as file:
    file.write(a)



