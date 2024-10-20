import matplotlib.pyplot as plt

def plot_data(x: list, y: list, title: str = ""):
    plt.plot(x, y, marker='o')
    plt.xlabel('Number of Rows')
    plt.ylabel('Execution Time (ms)')
    plt.title(title)
    plt.xscale('log')
    # plt.yscale('log') # Uncomment for log scale on Y axis
    plt.grid(True)
    plt.show()