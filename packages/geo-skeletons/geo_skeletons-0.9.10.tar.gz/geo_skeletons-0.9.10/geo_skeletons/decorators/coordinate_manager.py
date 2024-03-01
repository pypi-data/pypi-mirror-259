class CoordinateManager:
    """Keeps track of coordinates and data variables that are added to classes
    by the decorators."""

    def __init__(self) -> None:
        self.coords = {}
        self.coords["grid"] = []
        self.coords["gridpoint"] = []
        self.coords["initial"] = []

        self.vars = {}
        self.vars["added"] = {}
        self.vars["initial"] = {}

        self.masks = {}
        self.masks["added"] = {}

        self.default_values = {}

    def add_var(self, name: str, coords: str, default_value: float) -> None:
        """Add a variable that the Skeleton will use."""
        self.vars["added"][name] = coords
        self.default_values[name] = default_value

    def add_mask(self, name: str, coords: str, default_value: int) -> None:
        """Add a mask that the Skeleton will use."""
        self.masks["added"][f"{name}_mask"] = coords
        self.default_values[f"{name}_mask"] = default_value

    def add_coord(self, name: str, grid_coord: bool) -> None:
        """Add a coordinate that the Skeleton will use.

        grid_coord = True means that the coordinate describes the outer
        dimensions (e.g. x, y)

        grid_coord = False means that the coordinates describes the inner
        dimensions of one grid point (e.g. frequency, direction)

        E.g. time can be either one (outer dimesnion in spectra, but inner
        dimension in time series)
        """
        if grid_coord:
            self.coords["grid"].append(name)
        else:
            self.coords["gridpoint"].append(name)

    def set_initial_vars(self, initial_vars: dict) -> None:
        """Set dictionary containing the initial variables of the Skeleton"""
        if not isinstance(initial_vars, dict):
            raise ValueError("initial_vars needs to be a dict of tuples!")
        self.vars["initial"] = initial_vars

    def set_initial_coords(self, initial_coords: dict) -> None:
        """Set dictionary containing the initial coordinates of the Skeleton"""
        if not isinstance(initial_coords, list):
            raise ValueError("initial_coords needs to be a list of strings!")
        self.coords["initial"] = initial_coords

    def initial_vars(self) -> dict:
        return self.vars["initial"]

    def initial_coords(self) -> dict:
        return self.coords["initial"]

    def added_vars(self) -> dict:
        return self.vars["added"]

    def added_masks(self) -> dict:
        return self.masks["added"]

    def added_coords(self, coords: str = "all") -> list[str]:
        """Returns list of coordinates that have been added to the fixed
        Skeleton coords.

        'all': All added coordinates
        'grid': coordinates for the grid (e.g. z, time)
        'gridpoint': coordinates for a grid point (e.g. frequency, direcion or time)
        """
        if coords not in ["all", "grid", "gridpoint"]:
            print("Variable type needs to be 'all', 'grid' or 'gridpoint'.")
            return None

        if coords == "all":
            return self.added_coords("grid") + self.added_coords("gridpoint")
        return self.coords[coords]
