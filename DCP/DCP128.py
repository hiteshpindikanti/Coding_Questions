"""
Tower of Hanoi
Print all the steps
"""


def move(source_rod: str, target_rod: str, num_rings: int, state: dict):
    if num_rings:
        remaining_rod = next(iter(state.keys() - {source_rod, target_rod}))
        move(source_rod, remaining_rod, num_rings - 1, state)
        print(f"{source_rod} -> {target_rod}, ring: {state[source_rod][-1]}")
        state[target_rod].append(state[source_rod].pop(-1))
        move(remaining_rod, target_rod, num_rings - 1, state)


def print_steps(num_rings: int, source_rod: str = 'A', target_rod: str = 'C'):
    if num_rings:
        remaining_rod = next(iter({'A', 'B', 'C'} - {source_rod, target_rod}))
        print_steps(num_rings - 1, source_rod, remaining_rod)
        print(f"{source_rod} -> {target_rod}")
        print_steps(num_rings - 1, remaining_rod, target_rod)


if __name__ == "__main__":
    print_steps(num_rings=4)
