from typing import Tuple

import numba
import numpy as np


@numba.njit(cache=True)
def rotation_matrix(roll: float, pitch: float, yaw: float) -> np.ndarray:
    s1 = np.sin(roll)
    c1 = np.cos(roll)
    s2 = np.sin(pitch)
    c2 = np.cos(pitch)
    s3 = np.sin(yaw)
    c3 = np.cos(yaw)

    return np.array(
        [
            [c2 * c3, s1 * s2 * c3 - c1 * s3, s1 * s3 + c1 * s2 * c3],
            [c2 * s3, c1 * c3 + s1 * s2 * s3, c1 * s2 * s3 - s1 * c3],
            [-s2, s1 * c2, c1 * c2],
        ]
    )


@numba.njit(cache=True)
def transform_matrix(x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> np.ndarray:
    matrix = np.eye(4)
    matrix[:3, :3] = rotation_matrix(roll, pitch, yaw)
    matrix[:3, 3] = np.array((x, y, z))
    return matrix


@numba.njit(cache=True)
def transform_inverse_matrix(x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> np.ndarray:
    tf = transform_matrix(x, y, z, roll, pitch, yaw)
    inverse_matrix = np.zeros_like(tf)
    inverse_matrix[:3, :3] = tf[:3, :3].T
    inverse_matrix[:3, 3] = np.dot(-tf[:3, :3].T, tf[:3, 3])
    inverse_matrix[3, 3] = 1
    return inverse_matrix


@numba.njit(cache=True)
def euler_angles(matrix: np.ndarray) -> Tuple[float, float, float]:

    sy = np.sqrt(matrix[0, 0] * matrix[0, 0] + matrix[1, 0] * matrix[1, 0])
    singular = sy < 1e-6

    if not singular:
        x = np.arctan2(matrix[2, 1], matrix[2, 2])
        y = np.arctan2(-matrix[2, 0], sy)
        z = np.arctan2(matrix[1, 0], matrix[0, 0])
    else:
        x = np.arctan2(-matrix[1, 2], matrix[1, 1])
        y = np.arctan2(-matrix[2, 0], sy)
        z = 0

    return x, y, z


@numba.njit(cache=True)
def transform_point(x: float, y: float, z: float, matrix: np.ndarray) -> np.ndarray:
    v = np.dot(matrix, np.array([x, y, z, 1.0]))
    return v[0:3] / v[3]


@numba.njit(cache=True)
def transform_vertices(vertices: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    return (np.dot(matrix[:3, :3], vertices.T) + np.expand_dims(matrix[:3, 3], -1)).T
