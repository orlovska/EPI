import unittest
from python_code import permute_elements

class BasicTest(unittest.TestCase):
    def test_empty_strings(self):
        self.assertRaises(TypeError, permute_elements(['a','b'], ['1','0']), [], [])
        self.assertRaises(TypeError, permute_elements(['a','b'], ['1','0']), "", "")
        self.assertRaises(TypeError, permute_elements(['a','b'], ['1','0']), set(), set())
        self.assertRaises(TypeError, permute_elements(['a','b'], ['1','0']), dict(), dict())
        self.assertRaises(TypeError, permute_elements(['a','b'], ['1','0']), True, False)

    def test_on_the_same_place(self):
        self.assertEquals(permute_elements(['a','b','c'], [0,1,2]), ['a','b','c'])
        self.assertEquals(permute_elements(['a','b','c', 'd'], [0,1,2,3]), ['a','b','c', 'd'])

    def test_easy_case(self):
        self.assertEqual(permute_elements(['a','b','c', 'd'], [1,2,0,3]), ['b','c','a','d'])

if __name__ == '__main__':
    unittest.main()