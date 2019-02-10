import fileinput

for line in fileinput.input(inplace=1):
    line = line.rstrip()
    num = fileinput.lineno()
    print '%-40s # %2i' % (line, num)


set(range(10))
set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a = set([1, 2, 3])
b = set([2, 3, 4])
c = a & b
print c.issubset(a)
