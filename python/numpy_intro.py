import numpy as np

x = range(1,11)

a1 = np.array(x, np.int32)

a2 = np.array(x, np.float64)

print a1.dtype

print a2.dtype


print "\nex2\n"

arr1 = np.zeros((3, 1, 4, 5))
arr2 = np.ones((2, 3, 4))
arr3 = np.arange((1000))

print "this is array 1: \n", arr1, "\n"
print "this is array 2: \n", arr2, "\n"
print "this is array 3: \n", "arr3 would be here", "\n"

print "========================================="
print "\nex3::\n"

a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])

print a
print a[1]
print a[1:4]

a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],
             [1, 22, 4, 0.1, 5.3, -9],
             [3, 1, 2.1, 21, 1.1, -2]])

print "\nthis is a[:, 3]"
print a[:, 3]

print (38/31)*5


