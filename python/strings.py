s = "I {0} to write \
{1}".format("LOVE", "python")
print s

split_s = s.split()

print split_s

for word in split_s:
    if word.find("o") > -1:
        print "Well, {0} has an 'o' in it, innit!".format(word)
        print "yes  it does, look - {0}".format(word)






