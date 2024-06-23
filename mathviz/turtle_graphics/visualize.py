import matplotlib.pyplot as plt


def visualize(xs, ys):
    plt.figure(figsize=(10, 10))
    plt.plot(xs, ys, 'black')
    limits = [min(min(xs), min(ys)), max(max(xs), max(ys))]
    plt.xlim(limits)
    plt.ylim(limits)
    plt.axis('off')
    plt.show()