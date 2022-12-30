import numpy as np


def day13_part1():
    with open("day13_input.txt") as f:
        timestamp = int(f.readline())
    bus_ids = np.genfromtxt("day13_input.txt", dtype=int, delimiter=",", missing_values="x", skip_header=1)
    bus_ids = bus_ids[bus_ids != -1]

    departure_times = np.floor_divide(timestamp, bus_ids) * bus_ids + bus_ids
    time_to_departure = departure_times - timestamp
    idx = np.where(time_to_departure == min(time_to_departure))

    return (bus_ids[idx] * time_to_departure[idx])[0]


def day13_part2():
    bus_ids = np.genfromtxt("day13_input.txt", dtype=int, delimiter=",", missing_values="x", skip_header=1)
    max_id = max(bus_ids)
    constrained_timestamps = np.where(bus_ids != -1)[0]
    valid_buses = bus_ids[constrained_timestamps]
    idx_max_bus = np.where(bus_ids == max_id)[0][0]

    # With some speedup tricks thanks to u/WhipsAndMarkovChains
    timestamp_differences = constrained_timestamps - idx_max_bus
    num_increase = valid_buses[~((valid_buses != np.abs(timestamp_differences)) & (timestamp_differences != 0))]
    num_increase = np.prod(num_increase)
    check_remainders = valid_buses[(valid_buses != np.abs(timestamp_differences)) & (timestamp_differences != 0)]
    rem_ts_diff = timestamp_differences[(valid_buses != np.abs(timestamp_differences)) & (timestamp_differences != 0)]
    timestamp = num_increase * np.ones(len(check_remainders), dtype=int) + rem_ts_diff

    while np.count_nonzero(np.remainder(timestamp, check_remainders)) != 0:
        timestamp += num_increase
    return timestamp[0]


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Bus ID * time to departure: {day13_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Timestamp: {day13_part2()}")
