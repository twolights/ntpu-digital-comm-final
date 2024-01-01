from typing import Union

import numpy as np

ScalarOrNDArray = Union[float, np.ndarray]


def magnitude_to_dB(n: ScalarOrNDArray) -> ScalarOrNDArray:
    return 10 * np.log10(n)


def restore_dB(num_in_dB: ScalarOrNDArray) -> ScalarOrNDArray:
    return 10 ** (num_in_dB / 10)


def AWGN_like(target: np.ndarray, N_0: float) -> np.ndarray:
    return np.random.normal(0, (N_0 / 2), target.shape[0])


def power(x: ScalarOrNDArray) -> ScalarOrNDArray:
    return sum(x ** 2) / len(x)
