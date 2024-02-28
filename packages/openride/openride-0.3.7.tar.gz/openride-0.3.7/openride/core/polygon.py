from openride.core.geometry import Geometry
from openride.core.point import Point
from openride.core.numba import transform_vertices

import copy
import numpy as np

from dataclasses import dataclass, field
from shapely import geometry
from typing import List, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from openride.core.transform import Transform


@dataclass
class Polygon(Geometry):

    vertices: Union[np.ndarray, List[Point]] = field(default_factory=list)

    def __post_init__(self):

        if isinstance(self.vertices, list):
            points = copy.deepcopy(self.vertices)
            self.vertices = np.zeros((len(points), 3))
            for i, point in enumerate(points):
                self.vertices[i] = point.x, point.y, point.z

        if np.any(self.vertices[0] != self.vertices[-1]):
            self.vertices = np.vstack([self.vertices, self.vertices[0]])

    def to_shapely(self) -> geometry.Polygon:
        return geometry.Polygon(self.vertices)

    def transform(self, transform: "Transform") -> "Polygon":
        return Polygon(transform_vertices(self.vertices, transform.get_matrix()))

    @classmethod
    def from_shapely(cls, polygon: geometry.Polygon) -> "Polygon":
        return cls([Point(*c) for c in polygon.exterior.coords])

    def get_area(self) -> float:
        return self.to_shapely().area
