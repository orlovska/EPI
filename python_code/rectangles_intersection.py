# Rectangles parallel to X-axis and Y-axis.
# Return their intersections as new rectangels with new parameters 

from sys import getsizeof
import collections
from operator import attrgetter

def formingTuple(parameters):
#     #check the input - list,tuple
    RECTANGLE = collections.namedtuple('RECTANGLE',('x','y','height','width'))
    List = []
    try:
        for item in range(len(parameters)): 
            List.append(RECTANGLE._make(parameters[item]))
        return List
    except:
        raise TypeError("4 required positional arguments:'y', 'height', and 'width'")


def sortedTuple(rectangles):
    return sorted(rectangles, key=attrgetter('x','width'))


def rectangle_intersection(parameters):
    RECTANGLE = collections.namedtuple('RECTANGLE',('x','y','height','width'))
    
    R = sortedTuple(formingTuple(parameters))
    Result = []
    count = 0
    for A in R[ :-1]: 
        nextr = count+1
        B = R[nextr]
        if A.x + A.width > B.x:
            newX = max(A.x, B.x)
            newY = max(A.y, B.y)

            Xend = min(A.x + A.width, B.x + B.width)
            new_width = Xend - newX

            Yend = min(A.y + A.height, B.y + B.height)
            new_height = Yend - newY

            Result.append(RECTANGLE(newX,newY,new_width,new_height))
            
        else:
            break
        count += 1

    return ('No intersections found' if Result == [] else Result)
