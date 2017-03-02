import numpy.ma as MA

marr = MA.masked_array(range(10), fill_value = -999)

print marr, marr.fill_value

marr[2] = MA.masked

print marr

print marr.mask

narr = MA.masked_where(marr > 6, marr)

print narr

print narr.fill_value

x = MA.filled(narr)

print x

print type(x)

print "\nex2:\n"

m1 = MA.masked_array(range(1,9))

print m1

m2 = m1.reshape(2, 4)

print m2

m3 = MA.masked_greater(m2, 6)

print "\n", m3


