import matplotlib.pyplot as plt

f= open('out.txt', 'r')
N= []
T= []

for line in f:
    l = line.split(',')
    N.append(int(l[0]))
    T.append(float(l[1]))

plt.plot(T,N)
plt.xlabel('Time')
plt.ylabel('Number of survivors tracked')
plt.show()
