import unittest 
import context
from python_code import phone_mnemonics, chars_for_digit, check_for_more_values

class TestBasic(unittest.TestCase):

    def test_different_inputs(self):
        self.assertRaises(TypeError, phone_mnemonics(''), [2])
        self.assertRaises(TypeError, phone_mnemonics(''), (2,3,4))
        self.assertRaises(TypeError, phone_mnemonics(''), 1)

    def test_chars_for_digit_return(self):
        self.assertEqual(chars_for_digit("3"), 'DEF')
        self.assertEqual(chars_for_digit("0"), '0')
        self.assertEqual(chars_for_digit("1"), '1')
        self.assertEqual(chars_for_digit("5"), 'JKL')
        self.assertEqual(chars_for_digit("9"), 'WXYZ')

    def test_check_for_more_values_function(self):
        self.assertEqual(check_for_more_values("2", []), True)
        self.assertEqual(check_for_more_values("", []), True)
        self.assertEqual(check_for_more_values("2", ['A', 'B', 'C']), False)
        self.assertEqual(check_for_more_values("9", ['W', 'X', 'Y', 'Z']), False)

    def test_empty_input(self):
        self.assertEqual(phone_mnemonics(''), [])

    def test_easy_mnemonic(self):
        self.assertEqual(phone_mnemonics("2"), ['A', 'B', 'C'])
        self.assertEqual(phone_mnemonics("9"), ['W', 'X', 'Y', 'Z'])
        self.assertEqual(phone_mnemonics("1"), ['1'])
        
    def test_long_phone_number(self):
        self.assertEqual(phone_mnemonics("23"), ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF'])
        self.assertEqual(phone_mnemonics("234"), ['ADG', 'ADH', 'ADI', 'AEG', 'AEH', 'AEI', 'AFG', 'AFH', 'AFI', 'BDG', 'BDH', 'BDI', 'BEG', 'BEH', 'BEI', 'BFG', 'BFH', 'BFI', 'CDG', 'CDH', 'CDI', 'CEG', 'CEH', 'CEI', 'CFG', 'CFH', 'CFI'])
        self.assertEqual(phone_mnemonics("2345"), ['ADGJ', 'ADGK', 'ADGL', 'ADHJ', 'ADHK', 'ADHL', 'ADIJ', 'ADIK', 'ADIL', 'AEGJ', 'AEGK', 'AEGL', 'AEHJ', 'AEHK', 'AEHL', 'AEIJ', 'AEIK', 'AEIL', 'AFGJ', 'AFGK', 'AFGL', 'AFHJ', 'AFHK', 'AFHL', 'AFIJ', 'AFIK', 'AFIL', 'BDGJ', 'BDGK', 'BDGL', 'BDHJ', 'BDHK', 'BDHL', 'BDIJ', 'BDIK', 'BDIL', 'BEGJ', 'BEGK', 'BEGL', 'BEHJ', 'BEHK', 'BEHL', 'BEIJ', 'BEIK', 'BEIL', 'BFGJ', 'BFGK', 'BFGL', 'BFHJ', 'BFHK', 'BFHL', 'BFIJ', 'BFIK', 'BFIL', 'CDGJ', 'CDGK', 'CDGL', 'CDHJ', 'CDHK', 'CDHL', 'CDIJ', 'CDIK', 'CDIL', 'CEGJ', 'CEGK', 'CEGL', 'CEHJ', 'CEHK', 'CEHL', 'CEIJ', 'CEIK', 'CEIL', 'CFGJ', 'CFGK', 'CFGL', 'CFHJ', 'CFHK', 'CFHL', 'CFIJ', 'CFIK', 'CFIL'])
        self.assertEqual(phone_mnemonics("1906"), ['1W0M', '1W0N', '1W0O', '1X0M', '1X0N', '1X0O', '1Y0M', '1Y0N', '1Y0O', '1Z0M', '1Z0N', '1Z0O'])


if __name__=='__main__':
    unittest.main()