from typing import Tuple

def auto_coordinates(grid) -> Tuple[int, int, int]:
    _shape = grid.shape
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            for z in range(grid.shape[2]):
                if grid[x, y, z] is None:
                    return (x, y, z)
    return (_shape[0]-1, _shape[1]-1, _shape[2]-1)
