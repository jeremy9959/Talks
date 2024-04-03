import numpy as np
from bokeh.plotting import figure, show, output_file
import math

# x = np.linspace(0, 1, 100)
# y = 1
# F = figure(title="Uniform Distribution", x_range=(0, 1), y_range=(0, 2))
# F.varea(x, 0, y, fill_color="lightgray", alpha=0.5)
# F.line(x, y)
# show(F)


def beta(a, b):
    return math.gamma(a) * math.gamma(b) / math.gamma(a + b)


x = np.linspace(0, 1, 100)
y = (x**7 * (1 - x) ** 3) / beta(8, 4)
F = figure(title="Posterior Distribution", x_range=(0, 1), width=300, height=300)
F.line(x, y, color="red")
show(F)

# y1 = (x**12 * (1 - x) ** 8) / beta(13, 9)
# F.line(x, y1, color="blue")
# show(F)
