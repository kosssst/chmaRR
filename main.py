import numpy as np
import matplotlib.pyplot as plt

lambd = 0.5

delta_x = 1
delta_y = 1
delta_z = 1

delta_t = 1

x_dots = np.arange(0, 11, delta_x)
y_dots = np.arange(0, 11, delta_y)
z_dots = np.arange(0, 11, delta_z)

X, Y, Z = np.meshgrid(x_dots, y_dots, z_dots)

O_start = 400
O_limit = 500
O_0 = 5

hi = 100
v = 5
a = 50

result = []

fig = plt.figure()

for t in range(10):
    result_at_t = []
    if t == 0:
        for x in range(11):
            result_at_x = []
            for y in range(11):
                result_at_y = []
                for z in range(11):
                    result_at_y.append(O_start)
                result_at_x.append(result_at_y)
            result_at_t.append(result_at_x)
        result.append(result_at_t)
        continue
    A = [[0 for i in range(9**3)] for i in range(9**3)]
    B = [0 for i in range(9**3)]
    k = 0
    for x in range(1, 10, 1):
        for y in range (1, 10, 1):
            for z in range(1, 10, 1):
                B[k] = (lambd / (1 - lambd))*(result[t-1][x][y][z] * (a - v) + hi * ((result[t-1][x+1][y][z] - 2*result[t-1][x][y][z] + result[t-1][x-1][y][z]) / (delta_x**2) + (result[t-1][x][y+1][z] - 2*result[t-1][x][y][z] + result[t-1][x][y-1][z]) / (delta_y**2) + (result[t-1][x][y][z+1] - 2*result[t-1][x][y][z] + result[t-1][x][y][z-1]) / (delta_z**2)) - result[t-1][x][y][z] / (delta_t * lambd)) + (v * O_0) / (lambd - 1)
                o_xyz = (a-v) + hi*((-2) / (delta_x**2) + (-2) / (delta_y**2) + (-2) / (delta_z**2)) - (1 / (delta_t * (1 - lambd)))
                if (x == 1):
                    B[k] -= hi*O_limit / (delta_x**2)
                else:
                    A[k][(x-2) * (9**2) + (y-1) * (9**1) + (z-1)] = hi / (delta_x**2)
                if (x == 9):
                    B[k] -= hi*O_limit / (delta_x**2)
                else:
                    A[k][(x) * (9**2) + (y-1) * (9**1) + (z-1)] = hi / (delta_x**2)
                if (y == 1):
                    B[k] -= hi*O_limit / (delta_y**2)
                else:
                    A[k][(x-1) * (9**2) + (y-2) * (9**1) + (z-1)] = hi / (delta_x**2)
                if (y == 9):
                    B[k] -= hi*O_limit / (delta_y**2)
                else:
                    A[k][(x-1) * (9**2) + (y) * (9**1) + (z-1)] = hi / (delta_x**2)
                if (z == 1):
                    B[k] -= hi*O_limit / (delta_z**2)
                else:
                    A[k][(x-1) * (9**2) + (y-1) * (9**1) + (z-2)] = hi / (delta_x**2)
                if (z == 9):
                    B[k] -= hi*O_limit / (delta_z**2)
                else:
                    A[k][(x-1) * (9**2) + (y-1) * (9**1) + (z)] = hi / (delta_x**2)
                A[k][(x-1) * (9**2) + (y-1) * (9**1) + (z-1)] = o_xyz
                k += 1
                
    solved = np.linalg.solve(A, B)
    u =0            



# print(result)

for i in range(len(result)):
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(X, Y, Z, c=np.array(result[i]).ravel(), cmap="gist_rainbow_r", vmin=0, vmax=O_limit)
    cbar = fig.colorbar(sc)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f"t = {i}")
    
plt.show()