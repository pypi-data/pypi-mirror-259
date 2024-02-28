from openride.core.numba import rotation_matrix, euler_angles

from dataclasses import dataclass

import numpy as np


@dataclass
class Rotation:

    roll: float = 0.0
    pitch: float = 0.0
    yaw: float = 0.0

    def __post_init__(self):
        self.roll = self.roll % (2 * np.pi)
        self.pitch = self.pitch % (2 * np.pi)
        self.yaw = self.yaw % (2 * np.pi)

    def get_matrix(self) -> np.ndarray:
        return rotation_matrix(self.roll, self.pitch, self.yaw)

    @classmethod
    def from_matrix(cls, matrix: np.ndarray) -> "Rotation":
        return cls(*euler_angles(matrix))

    def __add__(self, other: "Rotation") -> "Rotation":
        return Rotation(self.roll + other.roll, self.pitch + other.pitch, self.yaw + other.yaw)

    def __sub__(self, other: "Rotation") -> "Rotation":
        return Rotation(self.roll - other.roll, self.pitch - other.pitch, self.yaw - other.yaw)
