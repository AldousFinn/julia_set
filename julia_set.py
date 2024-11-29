import numpy as np
import matplotlib.pyplot as plt



num_iterations = 1000


x = np.linspace(-1.5, 1.5, 1000)
y = np.linspace(-1.5, 1.5, 1000)
X, Y = np.meshgrid(x, y)

real = X
imag = Y * 1j
complex_pair = real + imag 

image = np.zeros(complex_pair.shape, dtype=int)
c = -0.8 + 0.156j



for i in range(num_iterations):
    complex_pair = complex_pair**2 + c
    mask = np.abs(complex_pair) > 2 
    image[mask] = i #excludes points that won't be graphed well




plt.imshow(image, extent=(-1.5, 1.5, -1.5, 1.5), cmap='twilight')
plt.show()