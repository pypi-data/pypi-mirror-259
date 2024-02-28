from openride import Point, BoundingBox

from typing import Tuple

import numpy as np


class Camera:
    def __init__(self, viewer):
        self.viewer = viewer
        self._camera = viewer.renderer.GetActiveCamera()
        self._camera.SetViewUp(0, 0, 1)
        self.set_clipping_range()

        self.set_position(Point(-10, 0, 5))
        self.set_focus(Point(0, 0, 0))

    def set_position(self, position: Point):
        self._camera.SetPosition(position.x, position.y, position.z)

    def set_focus(self, focus: Point):
        self._camera.SetFocalPoint(focus.x, focus.y, focus.z)

    def get_position(self) -> Point:
        return Point(*self._camera.GetPosition())

    def get_focus(self) -> Point:
        return Point(*self._camera.GetFocalPoint())
    
    def set_position_xyz(self, x: float, y: float, z: float):
        self._camera.SetPosition(x, y, z)

    def set_focus_xyz(self, x: float, y: float, z: float):
        self._camera.SetFocalPoint(x, y, z)

    def get_position_xyz(self) -> Tuple[float, float, float]:
        return tuple(self._camera.GetPosition())

    def get_focus_xyz(self) -> Tuple[float, float, float]:
        return tuple(self._camera.GetFocalPoint())
    
    def set_clipping_range(self, range:float=100000):
        self._camera.SetClippingRange(0.1, range)

    def follow(
        self,
        bounding_box: BoundingBox,
        distance: float = 15,
        height: float = 3,
        spring: float = 0.0,
        offset: float = 0.0,
    ):
        _offset = Point(
            x = offset * np.cos(bounding_box.rotation.yaw),
            y = offset * np.sin(bounding_box.rotation.yaw),
        )
        self.set_focus(bounding_box.position + _offset)

        x = -distance * np.cos(bounding_box.rotation.yaw)
        y = -distance * np.sin(bounding_box.rotation.yaw)
        z = height

        target_position = bounding_box.position + Point(x, y, z) + _offset
        self.set_position(spring * self.get_position() + (1 - spring) * target_position)

    def is_in_front(self, point: Point) -> bool:
        position = self.get_position()
        focus = self.get_focus()
        v1 = np.array([point.x - position.x, point.y - position.y, point.z - position.z])
        v2 = np.array([focus.x - position.x, focus.y - position.y, focus.z - position.z])
        return np.dot(v1, v2) >= 0
