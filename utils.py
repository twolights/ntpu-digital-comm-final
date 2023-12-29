import numpy as np


def restore_dB(num_in_dB: np.ndarray) -> np.ndarray:
    return 10 ** (num_in_dB / 10)
