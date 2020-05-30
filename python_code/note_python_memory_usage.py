from sys import getsizeof

print(getsizeof(5))
# 28

print(getsizeof(5.3))
# 24

from decimal import Decimal
print(getsizeof(Decimal(5.3)))
# 104

print(getsizeof(""))
# 49
print(getsizeof("1"))
# 50
print(getsizeof("1234"))
# 53

print(getsizeof([]))
# 72
print(getsizeof([1]))
# 80
print(getsizeof([1,2,3,4,5,6,7]))
# 128
print(getsizeof(["a long longlong string"]))
# 80

print(getsizeof(()))
# 56
print(getsizeof((1,)))
# 64
print(getsizeof((1,2,3,4)))
# 88
print(getsizeof(('a long longlong string')))
# 71

print(getsizeof(set()))
# 232
print(getsizeof(set([1])))
# 232
print(getsizeof(set([1,2,3,4,5,6,7])))
# 744

print(getsizeof({}))
# 248
print(getsizeof(dict(a=1)))
# 248

