import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def plot_mandelbrot(xmin, xmax, ymin, ymax, width=10, height=10, max_iter=256, cmap='twilight'):
    dpi = 80
    img_width = dpi * width
    img_height = dpi * height
    x, y, z = mandelbrot_set(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)

    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
    ticks = np.arange(0, img_width, 3 * dpi)
    x_ticks = xmin + (xmax - xmin) * ticks / img_width
    y_ticks = ymin + (ymax - ymin) * ticks / img_width
    plt.xticks(ticks, x_ticks)
    plt.yticks(ticks, y_ticks)
    ax.set_title("Mandelbrot Set")
    ax.imshow(z.T, origin='lower', cmap=cmap, extent=[xmin, xmax, ymin, ymax])
    plt.show()

# Define parameters
xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5
width, height = 10, 10
max_iter = 2048
cmap = 'twilight_shifted'

# Plot the Mandelbrot set
plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, cmap)
