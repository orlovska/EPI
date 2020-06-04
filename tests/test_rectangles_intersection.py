import unittest 
import context
from python_code import rectangle_intersection, formingTuple, sortedTuple
from sys import getsizeof
import collections
from operator import attrgetter, itemgetter

RECTANGLE=collections.namedtuple('RECTANGLE',('x','y','height','width'))

class BasicTest(unittest.TestCase):
    
    def test_input_sort(self):
        self.assertEqual(formingTuple([(5, 4, 1, 1)]), 
        [RECTANGLE(x=5, y=4, height=1, width=1)])
        self.assertEqual(formingTuple([(5, 4, 1, 1),(3, 3, 2, 3)]), 
        [RECTANGLE(x=5, y=4, height=1, width=1), RECTANGLE(x=3, y=3, height=2, width=3)])
    
    def test_empty_input(self):
        self.assertRaises(TypeError, formingTuple([]), [])
        self.assertRaises(TypeError, formingTuple([]), "1,2")
        self.assertRaises(TypeError, formingTuple([]), 1,2,3)

    def test_sorting(self):
        self.assertEqual(sortedTuple([RECTANGLE(x=5, y=4, height=1, width=1), RECTANGLE(x=3, y=3, height=2, width=3)]), 
        [RECTANGLE(x=3, y=3, height=2, width=3), RECTANGLE(x=5, y=4, height=1, width=1)])

    def test_first_rectangle_intersection(self):
        self.assertEqual(rectangle_intersection([(5, 4, 1, 1),(3, 3, 2, 3)]), 
        [RECTANGLE(x=5, y=4, height=1, width=1)])

    def test_rectangles_with_no_intersection(self):
        self.assertEqual(rectangle_intersection([(5, 4, 1, 1), (6, 5, 1, 2)]),
        'No intersections found')

    def test_rectangels_with_3intersections(self):
        self.assertEqual(rectangle_intersection([(6, 5, 1, 2), (5, 4, 1, 1), (3, 3, 2, 3), (1, 2, 2, 3), (1, 1, 2, 1)]), 
        [RECTANGLE(x=1, y=2, height=1, width=1), RECTANGLE(x=3, y=3, height=1, width=1), RECTANGLE(x=5, y=4, height=1, width=1)])   

if __name__=='__main__':
    unittest.main()