from typing import Union

import numpy as np
from scipy.stats import norm


InputType = Union[np.ndarray, float, int]


def _Q(x: InputType) -> InputType:
    return 1 - norm.cdf(x)


def coherent_BPSK(Eb_N0: InputType) -> InputType:
    return _Q(np.sqrt(2 * Eb_N0))


def coherent_DPSK(Eb_N0: InputType) -> InputType:
    return (1 / 2) * np.exp(-1 * Eb_N0)


def coherent_BFSK(Eb_N0: InputType) -> InputType:
    return _Q(np.sqrt(Eb_N0))


def non_coherent_BFSK(Eb_No: InputType) -> InputType:
    return (1 / 2) * np.exp(-1 / 2 * Eb_No)
