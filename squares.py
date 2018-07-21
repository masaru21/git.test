import numpy as np
data = np.loadtxt("/Users/Masaru/Desktop/data.txt",skiprows = 1)

N = 24
x = data[:,0]
y = data[:,1]

sum_x = np.sum(x for x in data[:,0])
sum_y = np.sum(y for y in data[:,1])
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2 for x in data[:,0])

a = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x ** 2)
#回帰直線の傾き

b = (sum_x2 * sum_y - sum_xy * sum_x) / (N * sum_x2 - sum_x ** 2)
#回帰直線の切片

R = np.corrcoef(x, y)[0,1]
#相関係数


print("傾き: " + str(a))
print("切片: " + str(b))
print("相関係数: " + str(R))
