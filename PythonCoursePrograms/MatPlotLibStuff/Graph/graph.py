import matplotlib.pyplot as plt

figure = plt.figure()
ax1 = figure.add_subplot()
ax2 = figure.add_subplot()

ax1.plot([1,2,3,4], [3,4,5,6])
ax2.plot([5,6,7,8], [8,9,0,0])

plt.show()
