import matplotlib.pyplot as plt

x = list(range(0, 256, 15))
y = [0.484, 0.484,
0.496,
0.590,
0.777,
0.966,
1.157,
1.351,
1.542,
1.728,
1.920,
2.112,
2.304,
2.493,
2.685,
2.878,
3.070,
3.262]

plt.plot(x, y, **{'color':'blue', 'marker': 'o'})
plt.show()
