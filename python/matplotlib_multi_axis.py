import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()

times = range(7)
co2 = 250, 256, 272, 260, 300, 320, 389

ax1.plot(times, co2, "b--")
ax1.set_ylabel('[$CO_2$]')
ax2 = ax1.twinx()

temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

ax2.set_ylabel("Temp (degC)")

plt.show()

#ex2

plt.subplot (1, 3, 1)
x = range(0, 10, 1)
plt.plot(x)

plt.subplot(1, 3, 2)
y = range(10, 0, -1)
plt.plt(y)
