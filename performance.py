import statistics


def calculate_metrics(loads, elapsed_seconds=0.0):
    """Calculate descriptive load-balance and runtime metrics."""
    if not loads:
        raise ValueError("The server-load list cannot be empty.")

    average = statistics.mean(loads)
    return {
        "total_requests": sum(loads),
        "maximum_load": max(loads),
        "minimum_load": min(loads),
        "average_load": average,
        "standard_deviation": statistics.pstdev(loads),
        "load_range": max(loads) - min(loads),
        "execution_time_ms": elapsed_seconds * 1000,
    }


def print_comparison(metrics):
    print("\n" + "=" * 92)
    print("PERFORMANCE COMPARISON")
    print("=" * 92)
    print(
        f"{'Algorithm':<24}{'Max':>8}{'Min':>8}{'Average':>12}"
        f"{'Std Dev':>12}{'Range':>9}{'Time (ms)':>14}"
    )
    print("-" * 92)

    for name, values in metrics.items():
        print(
            f"{name:<24}"
            f"{values['maximum_load']:>8}"
            f"{values['minimum_load']:>8}"
            f"{values['average_load']:>12.2f}"
            f"{values['standard_deviation']:>12.2f}"
            f"{values['load_range']:>9}"
            f"{values['execution_time_ms']:>14.4f}"
        )

    print("-" * 92)
    print("Lower standard deviation and load range indicate a more even distribution.")
    print("Execution times are machine- and run-dependent.")
