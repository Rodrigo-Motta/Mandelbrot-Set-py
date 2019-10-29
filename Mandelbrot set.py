import numpy as np
from pylab import imshow, plot, show, gray


N = 1000     # the number of the divisions on the axis
NIT = 10     # f(z) precision

real = np.linspace(-2, 2, N)                # Real axis
imaginario = np.linspace(-2, 2, N)          # Imaginary axis
matriz_c = np.zeros((N, N), dtype=complex)  # matrix for the c values

# now we add the c values on the subspace (limited axis)
for x in range(1, N):
    for y in range(1, N):
        matriz_c[x][y] = real[x] + 1j*imaginario[y]

# here we create the function to check the numbers inside and out of the mandelbrot set


def iterete(c, NIT):
    termo = 0
    for i in range(0, NIT):
        termo = termo*termo + c
    return termo

# now its time to check if the matrix numbers are in the mandelbrot


Mandel = np.zeros((N, N), dtype=float)
for x in range(1, N):
    for y in range(1, N):
        Mandel[x][y] = iterete(matriz_c[x][y], NIT)
        if abs(Mandel[x][y]) > 2:       # if the number is not in the set we change it to zero for the density graph
            Mandel[x][y] = 0
        else:
            Mandel[x][y] = abs(Mandel[x][y])

imshow(Mandel.transpose())
gray()
show()
