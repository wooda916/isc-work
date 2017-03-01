print "Exercise 1: \n"

t = (1,)

print t[-1]

r1 = range(100,201)

print "r1 = ", r1

t1 = tuple(r1)

print "tuple value 1 = ", t1[0], "tuple value 2 = ", t1[-1]

print "\nExercise 2: \n "

mylist = [23, "hi", 2.4e-10]

for item in mylist:
    print "%s (index: %s)" % (item, mylist.index(item))

print "\nconvert to enumerate\n"

for (count, item) in enumerate(mylist):
    print "index:", count, "item:", item

print "\nExercise 3: \n "

(first, middle, last) = mylist

print first,"\n", middle, "\n",last

first,  middle, last = middle, last, first

print first,middle,last



