from openride.core.geometry import Geometry
from openride.core.numba import transform_point

from dataclasses import dataclass
from shapely import geometry
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from openride.core.transform import Transform


@dataclass
class Point(Geometry):

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def to_shapely(self) -> geometry.Point:
        return geometry.Point([self.x, self.y, self.z])

    def transform(self, transform: "Transform") -> "Point":
        return Point(*transform_point(self.x, self.y, self.z, transform.get_matrix()))

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, factor: float) -> "Point":
        return Point(factor * self.x, factor * self.y, factor * self.z)

    def __rmul__(self, factor: float) -> "Point":
        return self * factor

    def __repr__(self):
        return f"Point(x:{self.x:.2f}, y:{self.y:.2f}, z:{self.z:.2f})"
