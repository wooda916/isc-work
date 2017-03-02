a = set([0, 1, 2, 3, 4, 5])
b = set([2, 4, 6, 8])

print a.union(b)

print a.intersection(b)

print "\nExercise 2\n"

band = ["mel", "geri", "victoria", "mel", "emma"]

counts = {}

for name in band:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

for name in counts:
    print name, counts[name]

print "\nExercise 3\n"

if {}: print 'hi'

d = {"maggie": "uk", "ronnie": "usa"}

print d.items()
print d.keys()
print d.values()

print d.get("maggie", "nowhere")

print d.get("turd", "nowhere")

res = d.setdefault("mikhail", "ussr")

print res, d["mikhail"]


