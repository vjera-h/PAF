import matplotlib.pyplot as plt

x = [5, -6, 7, 8]
y = [-1, 2, 3, -4]

tocke = [[-2,5],[4,1],[0,-0.5]]

plt.figure()
plt.scatter(x,y)
plt.plot(zip(tocke))

plt.show()
#bitno je stavit koordinantne osi plt.ax/plt.ay
#plotanje vektora je plt.quiver