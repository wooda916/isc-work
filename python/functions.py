def double_it (number):
    return 2 * number

print double_it (2)

print double_it(2.5)

print double_it ("oi ")

print double_it("\n")

def calc_hypo (a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        print "Bad Argument!"
        return False
    if a <= 0 or b <= 0:
        print "Bad Argument (you numpty!)"
        return False
    hypo = ((a**2.0)+(b**2.0))**0.5
    return hypo

print calc_hypo (1, 2)

print calc_hypo ("hi", "bi")

