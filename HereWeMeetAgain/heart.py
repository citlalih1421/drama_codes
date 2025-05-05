'''
Here We Meet Again,ep 13 -- cartesian heart
    function from plot_heart onwards was provided in the show at minute 18:34
    another code for the same output is in the second file under this directory
'''
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import random
import gif

def plot_scatter(ax, x, y, beta=0.15, layer=1, *, alpha=None):
    """
    Scatter points inward using exponential scaling.
    'layer' is a dummy label.
    'alpha' is optional and must be passed as keyword-only.
    """
    # Exponential inward ratios
    ratio_x = -beta * np.log(np.random.rand(x.shape[0]))
    ratio_y = -beta * np.log(np.random.rand(y.shape[0]))

    # Move points inward
    dx = ratio_x * x
    dy = ratio_y * y
    x_new = x - dx
    y_new = y - dy

    effective_alpha = alpha if alpha is not None else 0.6

    ax.scatter(x_new, y_new, s=3, c="#d66582", alpha=effective_alpha)
    
    
@gif.frame
def plot_heart(x, y, ratio):
    fig = plt.figure(figsize=(7, 7), facecolor="black")
    ax = plt.gca()
    ax.set_facecolor("black")
    x = x * np.sin(ratio)
    y = y * np.sin(ratio)

    ax.scatter(x, y, s=3, c="#d66582")

    plot_scatter(ax, x, y, 0.15, 1)
    plot_scatter(ax, x, y, 0.15, 2)
    plot_scatter(ax, x, y, 0.15, 3)

    xi = x[0:x.shape[0]:2] * np.sin(ratio) * 0.7
    yi = y[0:y.shape[0]:2] * np.sin(ratio) * 0.7
    plot_scatter(ax, xi, yi, 0.25, 4)

    xo = x[0:x.shape[0]:2] * np.sin(ratio) * 1.2
    yo = y[0:y.shape[0]:2] * np.sin(ratio) * 1.2

    np.random.seed(random.randint(1, 3))
    plot_scatter(ax, xo, yo, 0.1, 4, alpha=0.8)

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(bottom=False, labelbottom=False,
                left=False, labelleft=False)
    plt.xlim((-6*np.pi, 6*np.pi))
    plt.ylim((-6*np.pi, 6*np.pi))
    plt.tight_layout(pad=0)


# Generate frames
frames = []
# Setup figure and animation
for ratio in np.linspace(np.pi/3, 2*np.pi/3, 20):
    t = np.linspace(0, 2*np.pi, 2000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    of = plot_heart(x, y, ratio)
    frames.append(of)

gif.save(frames, "love.gif", duration=100)
im = Image.open("love.gif")
im.show()

