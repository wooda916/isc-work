import numpy as np

a = np.array([range(4), range(10, 14)])

b = np.array([2, -1, 1, 0])

print "\n", a, "\n"

print b


print "\nThis is a x b: "
 
print a * b

b1 = b * 100
b2 = b * 100.0

print "\n", b1

print "\n", b2

print b1 == b2
