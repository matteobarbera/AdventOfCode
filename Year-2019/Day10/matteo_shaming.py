import numpy as np
import time
import math
from functools import wraps
import warnings
warnings.filterwarnings("ignore")


def timer(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print(f'Function {f.__name__} took: {(end-start):.3f} seconds.')

        return res
    return wrapped


@timer
def matteo_best_location(asteroid_field: np.ndarray) -> (np.ndarray, int):
    best_location = asteroid_field[0]
    most_visible_asteroids = 0
    for asteroid in asteroid_field:
        relative_coords = asteroid_field - asteroid
        visible_asteroids = set()
        for i in relative_coords:
            if np.array_equal(i, [0, 0]):
                continue
            reduced_coords = tuple(i // math.gcd(*i))
            if reduced_coords not in visible_asteroids:
                visible_asteroids.add(reduced_coords)
        n_visible_asteroids = len(visible_asteroids)
        if n_visible_asteroids > most_visible_asteroids:
            best_location = asteroid
            most_visible_asteroids = n_visible_asteroids
    return best_location, most_visible_asteroids


@timer
def peter_best_location(asteroid_field: np.ndarray) -> (np.ndarray, int):

    # Make a square matrix the repeated asteroid_field vector:
    repeated_field = np.repeat(asteroid_field[:, :, np.newaxis], asteroid_field.shape[0], axis=2)

    # Shift the coordinates of each row by the asteroid:
    relative_field = repeated_field - repeated_field.T

    # Calculate the reduced (divided by GCD) relative vector for each position:
    reduced_field = np.zeros(relative_field.shape)
    for i, row in enumerate(relative_field):
        for j, coord in enumerate((row[:, i:]).T):
            c = coord // math.gcd(*coord)           # Let numpy take care of div 0 exceptions. We don't have time.
            reduced_field[i, :, i + j] = c
            reduced_field[i + j, :, i] = -c         # The matrix is C:\\Users\\PSere\\Desktop\\asteroid_field.txtsymmetric, but one half is negative.
    reduced_field = reduced_field.astype(int)

    # Count the unique vectors in each row:
    unique_count = np.zeros(shape=asteroid_field.shape[0], dtype=int)
    for i in range(reduced_field.shape[0]):
        row = [tuple(c) for c in reduced_field[i, :, :].T]
        unique_count[i] = len(list(set(row))) - 1               # -1 because of (0, 0)

    # Best asteroid:
    best_idx = np.argmax(unique_count)
    max_count = unique_count[best_idx]

    return asteroid_field[best_idx], max_count

def main():
    input_file = "day10_input.txt"

    asteroid_coordinates = []
    with open(input_file) as f:
        for y, line in enumerate(f):
            asteroid_coordinates += [[x, y] for x, char in enumerate(line) if char == "#"]

    asteroid_coordinates = np.array(asteroid_coordinates)

    station_coords_A, detectable_asteroids_A = matteo_best_location(asteroid_coordinates)
    station_coords_B, detectable_asteroids_B = peter_best_location(asteroid_coordinates)

    print(f'Matteo result: {station_coords_A} and {detectable_asteroids_A}')
    print(f'Peter result: {station_coords_B} and {detectable_asteroids_B}')


if __name__ == '__main__':
    main()
