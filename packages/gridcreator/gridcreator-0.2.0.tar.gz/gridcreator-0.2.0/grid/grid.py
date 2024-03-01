import numpy as np
from typing import AnyStr, Tuple, Any
from .element import Element
from .coord import auto_coordinates
from .hash import sha256
class Grid:
    """Class of the Grid."""
    def __init__(self, name: AnyStr="Cool Grid", size: Tuple[int, int, int]=(3, 3, 3)):
        """
        Initializes the Cool Grid with the given name and size.

        Args:
            name (AnyStr, optional): The name of the grid. Defaults to "Cool Grid".
            size (Tuple[int, int, int], optional): The size of the grid. Defaults to (3, 3, 3).

        Raises:
            ValueError: If the size is (32, 32, 32), as the size is too big.

        Returns:
            None
        """
        if size == (32, 32, 32):
            raise ValueError("The size is too big. We don't have good optimization yet, so we have limits.")
        self.grid_name = name
        self.grid = np.empty(size, dtype=object)
        self.grid.fill(None)
        self.size = size
        self._neighbors_offsets = [ # Offsets for neighbors. Helps with receiving them.
            (1, 0, 0), (-1, 0, 0), (0, 1, 0),
            (0, -1, 0), (0, 0, 1), (0, 0, -1)
        ]
    def import_pair(self, access_key, private_key, public_key):
        """
        Import account into the grid cache.
        """
        to_hash = {access_key, private_key, public_key}
        hashed = sha256(to_hash)
        self.grid[0, 0, 1]["data"]["accounts"].append(f"{self.grid_name}{hashed}")
    def genesis(self):
        """
        Creates a new element which will be the base of the grid.
        """
        self.add("Genesis Element", {"grid_name": self.grid_name, "size": self.size}, coordinates=(0,0,0))
    def cache(self):
        """
        Creates a new element which will be used to keep cache and save all available info of the grid and element in.
        """
        self.add("Cache Element", dict({"accounts": []}), coordinates=(0,0,1), hash=False)
    def addel(self, element: Element):
        """Adds a new element via class Element."""
        self._add_to_grid(element.get())

    def add(self, name: AnyStr, data: Any, coordinates: Tuple[int, int, int]=None, hash: bool=True):
        """
        Add a new element.

        Parameters:
        name (AnyStr): The name of the new element.
        data (Any): The data which the element will contain.
        coordinates (Tuple[int, int, int]: The coordinates of the new element.
        hash (bool): Add hash? Or not.
        """
        if coordinates is None:
            coordinates = auto_coordinates(self.grid)
        element = Element(name, data, coordinates, self._get_neighbors(coordinates), hash)
        self._add_to_grid(element)
    
    def get_size(self) -> Tuple[int, int, int]:
        return self.size

    def _add_to_grid(self, element: Element):
        x, y, z = element.get_coordinates()
        self.grid[x, y, z] = element.get()

    def get(self) -> np.ndarray:
        """
        Get all grid.
        """
        return self.grid

    def _get_neighbors(self, coord) -> list:
        """
        Receiving the neighbors of the given coordinate.
        """

        neighbors = []
        for offset in self._neighbors_offsets:
            nx, ny, nz = coord[0] + offset[0], coord[1] + offset[1], coord[2] + offset[2]
            if 0 <= nx < self.size[0] and 0 <= ny < self.size[1] and 0 <= nz < self.size[2]:
                if self.grid[nx, ny, nz] is not None:
                    neighbor_element = self.grid[nx, ny, nz]
                    neighbors.append(((nx, ny, nz), neighbor_element))
        """
        This function iterates through the offsets of neighboring coordinates and checks if the coordinates are within the grid boundaries.
        If a neighbor exists at the calculated coordinates, it is added to the list of neighbors.
        """
        return neighbors
    
    def setdata(self, coordinates: Tuple[int, int, int], data: Any):
        self.grid[coordinates]["data"] = data
    
    def setname(self, coordinates: Tuple[int, int, int], name: str):
        self.grid[coordinates]["name"] = name
    
    def sethash(self, coordinates: Tuple[int, int, int], hash: AnyStr):
        self.grid[coordinates]["hash"] = hash

    def upn_all(self):
        """
        Updates neighbors of all elements of the grid.
        """
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                for z in range(self.size[2]):
                    element = self.grid[x, y, z]
                    if element is not None:
                        self.upn((x, y, z))
        """ Just a simple loop."""
    
    def upn(self, coord: Tuple[int, int, int]):
        """
        Updates neighbors of the given coordinate.
        """
        self.grid[coord]["neighbors"] = self._get_neighbors(coord)

    def save(self):
        """Save grid in .pkl format."""
        np.savez_compressed(f'{self.grid_name}.npz', arr=self.grid)
    
    def load(self, filename):
        """Load grid in .pkl format."""
        self.grid = np.load(filename, allow_pickle=True)['arr']
        
    def setneighbors(self, coordinates: Tuple[int, int, int], neighbors):
        self.grid[coordinates]["neighbors"] = neighbors