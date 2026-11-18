import os
import matplotlib.pyplot as plt


def plot_load_distribution(results):
    os.makedirs("charts", exist_ok=True)

    for name, loads in results.items():
        labels = [f"Server {i + 1}" for i in range(len(loads))]
        plt.figure(figsize=(9, 5))
        bars = plt.bar(labels, loads)
        plt.title(f"{name}: Server Request Distribution")
        plt.xlabel("Servers")
        plt.ylabel("Number of requests")
        plt.grid(axis="y", linestyle="--", alpha=0.35)
        for bar, value in zip(bars, loads):
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                str(value),
                ha="center",
                va="bottom",
            )
        plt.tight_layout()
        filename = name.lower().replace(" ", "_") + "_distribution.png"
        plt.savefig(os.path.join("charts", filename), dpi=150)
        plt.close()


def plot_algorithm_comparison(metrics):
    os.makedirs("charts", exist_ok=True)
    names = list(metrics.keys())
    deviations = [metrics[name]["standard_deviation"] for name in names]
    ranges = [metrics[name]["load_range"] for name in names]

    plt.figure(figsize=(9, 5))
    plt.bar(names, deviations)
    plt.title("Load Imbalance Comparison (Standard Deviation)")
    plt.xlabel("Algorithm")
    plt.ylabel("Standard deviation of server loads")
    plt.grid(axis="y", linestyle="--", alpha=0.35)
    plt.tight_layout()
    plt.savefig("charts/standard_deviation_comparison.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.bar(names, ranges)
    plt.title("Load Range Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Maximum load - Minimum load")
    plt.grid(axis="y", linestyle="--", alpha=0.35)
    plt.tight_layout()
    plt.savefig("charts/load_range_comparison.png", dpi=150)
    plt.close()
