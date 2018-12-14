#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.animation as manim
import numpy as np

from main import Track

class AnimateTrack(Track):
    def __init__(self, track_map):
        super().__init__(track_map)
        self.fig, self.ax = plt.subplots(1, 1)

    def initialize_plot(self):
        self.fig.set_size_inches(8,8)
        self.ax.set_aspect('equal')
        self.ax.invert_yaxis()
        self.ax.set_axis_off()
        self.title = self.ax.set_title('Tick: {}, Carts remaining: {}'.format(self.tick, len(self.carts)))
        self.plot_track()
        self.cart_line = None
        self.plot_carts()
        plt.tight_layout()
        return (self.cart_line, self.title)

    def get_lines(self):
        for i, j, chars in [(0, 1, '/|\\+'), (1, 0, '/-\\+')]:
            lines = set([k[i] for k, v in self.tracklines.items() if v in chars])
            for line in lines:
                segment = []
                for p in sorted([k for k, v in self.tracklines.items()
                        if k[i] == line and v in chars]):
                    if not segment:
                        segment.append(p)
                        continue
                    if p[j] - segment[-1][j] != 1:
                        yield np.asarray(segment)
                        segment = [p]
                    else:
                        segment.append(p)
                yield np.asarray(segment)

    def plot_track(self):
        for line in self.get_lines():
            self.ax.plot(*line.T, color = 'C0', linewidth = 0.5)

    def plot_carts(self):
        carts = np.asarray([c.position for c in self.carts])
        if self.cart_line is None:
            self.cart_line, = self.ax.plot(*carts.T, linestyle = '', marker =
            '.', color = 'C1')
        else:
            self.cart_line.set_data(*carts.T)

    def animate(self, ticks = None, fps = 25):
        def f(frame):
            self.step()
            self.plot_carts()
            self.title.set_text('Tick: {}, Carts remaining: {}'.format(self.tick, len(self.carts)))
            return (self.cart_line, self.title)
        return manim.FuncAnimation(self.fig, f, init_func = self.initialize_plot,
                frames = ticks, interval = 1000/fps)

if __name__ == '__main__':
    with open('input', 'r') as f:
        animated_track = AnimateTrack(f.read())
    ani = animated_track.animate(fps = 25)
    plt.show()

