print "\nExercise 1: \n "

with open("weather.csv", "r") as reader:
    data = reader.read()

print data

print "\nExercise 2: \n "

with open("weather.csv", "r") as reader:
    line = reader.readline()
    
