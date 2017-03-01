n = 1

print "Exercise 1: \n " 

mylist = [1, 2, 3, 4, 5]

print mylist [1]

print mylist [-2]

print mylist [2:]

print mylist [1:3]

print "\nExercise 2: \n "

one_to_ten = range(1,11)

print one_to_ten

one_to_ten [0] = 10

print one_to_ten

one_to_ten.append(11)

print one_to_ten

one_to_ten.extend([12,13,14])

print one_to_ten

print "\nExercise 3: \n "

forward = []
backward = []

values = ["a", "b", "c"]

for thing in values:
    forward.append(thing)
    backward.insert(0, thing)

print "forward is: %s" % forward
print "backward is: %s" % backward

forward.reverse()

print "forward (reversed) is: %s" % forward

print "does forward = backward?", forward == backward

print "\nExercise 4: \n "

countries = ["uk", "usa", "uk", "uae"]

print countries.count("uk"), "\n"

