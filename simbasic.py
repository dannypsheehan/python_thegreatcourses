#Basic simulation

from matplotlib.pyplot import plot, axis, show
xlist = range(0,6)
ylist = []
for i in xlist:
    ylist.append(i*i)
plot(xlist, ylist)
axis([0,5,0,25])
show()