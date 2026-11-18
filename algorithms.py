import random


def randomized_load_balancer(server_count, request_count):
    """Assign each request to one uniformly random server."""
    loads = [0] * server_count
    for _ in range(request_count):
        selected = random.randrange(server_count)
        loads[selected] += 1
    return loads


def round_robin_load_balancer(server_count, request_count):
    """Assign requests sequentially, cycling through the servers."""
    loads = [0] * server_count
    for request_index in range(request_count):
        selected = request_index % server_count
        loads[selected] += 1
    return loads


def power_of_two_choices(server_count, request_count):
    """Choose two distinct random servers and assign to the less-loaded one."""
    if server_count < 2:
        raise ValueError("Power of Two Choices requires at least two servers.")

    loads = [0] * server_count
    for _ in range(request_count):
        first, second = random.sample(range(server_count), 2)
        if loads[first] <= loads[second]:
            loads[first] += 1
        else:
            loads[second] += 1
    return loads
