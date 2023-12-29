import numpy as np
from scipy.stats import norm


def _Q(x: np.ndarray) -> np.ndarray:
    return 1 - norm.cdf(x)


def coherent_BPSK(Eb_N0: np.ndarray) -> np.ndarray:
    return _Q(np.sqrt(2 * Eb_N0))


def coherent_DPSK(Eb_N0: np.ndarray) -> np.ndarray:
    return (1 / 2) * np.exp(-1 * Eb_N0)


def coherent_BFSK(Eb_N0: np.ndarray) -> np.ndarray:
    return _Q(np.sqrt(Eb_N0))


def non_coherent_BFSK(Eb_No: np.ndarray) -> np.ndarray:
    return (1 / 2) * np.exp(-1 / 2 * Eb_No)
