import random
import time
from algorithms import (
    randomized_load_balancer,
    round_robin_load_balancer,
    power_of_two_choices,
)
from performance import calculate_metrics, print_comparison
from visualization import plot_load_distribution, plot_algorithm_comparison


def get_positive_int(prompt, minimum=1):
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=" * 64)
    print("       RANDOMIZED LOAD BALANCER FOR SERVICE REQUESTS")
    print("=" * 64)
    print("This project compares three ways of distributing requests.")
    print("")

    server_count = get_positive_int("Enter number of servers (minimum 2): ", 2)
    request_count = get_positive_int("Enter number of service requests: ", 0)

    # Use the same seed for reproducible demonstrations.
    seed = int(time.time())
    random.seed(seed)

    algorithms = {
        "Randomized": randomized_load_balancer,
        "Round Robin": round_robin_load_balancer,
        "Power of Two Choices": power_of_two_choices,
    }

    results = {}
    timings = {}

    for name, algorithm in algorithms.items():
        start = time.perf_counter()
        results[name] = algorithm(server_count, request_count)
        timings[name] = time.perf_counter() - start

    print("\n" + "=" * 64)
    print("SERVER REQUEST DISTRIBUTION")
    print("=" * 64)
    for name, loads in results.items():
        print(f"\n{name}")
        print("-" * 40)
        for index, load in enumerate(loads, start=1):
            print(f"Server {index:>2}: {load:>6} requests")

    metrics = {
        name: calculate_metrics(loads, timings[name])
        for name, loads in results.items()
    }

    print_comparison(metrics)

    print("\nGenerating charts...")
    try:
        plot_load_distribution(results)
        plot_algorithm_comparison(metrics)
        print("Charts saved in the 'charts' folder.")
    except ImportError:
        print("Matplotlib is not installed. Run: pip install -r requirements.txt")

    print("\nProject execution completed.")


if __name__ == "__main__":
    main()
