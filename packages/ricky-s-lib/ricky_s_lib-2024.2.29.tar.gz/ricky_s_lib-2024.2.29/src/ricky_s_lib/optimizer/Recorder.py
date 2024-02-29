import json

import matplotlib.pyplot as plt


class Recorder:
    def __init__(s):
        s.data = []

    def add(s, x, y, labels, sort):
        s.data.append([x, y])
        s.data = list(sorted(s.data, key=lambda xy: sort(xy[1])))
        # plots y1 vs y0, y2 vs y0 ...
        n = len(y) - 1
        plt.figure(figsize=(6, n * 4))
        for i in range(1, len(y)):
            plt.subplot(n, 1, i)
            plt.title(f"{labels[i]} vs {labels[0]}")
            a = [xy[1][0] for xy in s.data]
            b = [xy[1][i] for xy in s.data]
            plt.scatter(a, b)
        plt.tight_layout()
        plt.savefig("recorder.png")
        plt.close()
        with open("recorder.json", "w+") as f:
            json.dump(s.data, f, indent=2)
