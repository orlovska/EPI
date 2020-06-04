import unittest 
import context
from python_code import phone_mnemonics

class TestBasic(unittest.TestCase):

    def test_different_inputs(self):
        self.assertRaises(TypeError, phone_mnemonics(''), [2])
        self.assertRaises(TypeError, phone_mnemonics(''), (2,3,4))
        self.assertRaises(TypeError, phone_mnemonics(''), 1)

    def test_empty_input(self):
        self.assertEqual(phone_mnemonics(''), [''])

    def test_easy_mnemonic(self):
        self.assertEqual(phone_mnemonics("2"), ['A', 'B', 'C'])
        self.assertEqual(phone_mnemonics("9"), ['W', 'X', 'Y', 'Z'])
        self.assertEqual(phone_mnemonics("1"), ['1'])
        
    def test_long_phone_number(self):
        self.assertEqual(phone_mnemonics("23"), ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF'])
        self.assertEqual(len(phone_mnemonics("1906")), 12)
        self.assertEqual(phone_mnemonics("1906")[0], '1W0M')
        self.assertEqual(len(phone_mnemonics("222")), 27)
        self.assertEqual(phone_mnemonics("222")[-1],'CCC')
        self.assertEqual(len(phone_mnemonics("234")), 27)
        self.assertEqual(phone_mnemonics("234")[-1],'CFI')
        self.assertEqual(len(phone_mnemonics("2345")), 81)
        self.assertEqual(phone_mnemonics("2345")[-1], 'CFIL')



if __name__=='__main__':
    unittest.main()