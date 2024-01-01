from typing import Tuple, Any

import numpy as np

import utils

PHI_T = 1
PHI_OMEGA = 2 * np.pi * 4
PHI_NUM_SAMPLES = 1000


class BPSKExperiment:
    x: np.ndarray
    N_0: float
    E_b: float

    phi: np.ndarray
    signals: Tuple[np.ndarray, np.ndarray]

    source: np.ndarray
    detected: np.ndarray
    received: list = []

    @staticmethod
    def calculate_BER(result: dict):
        num_successful = result[0][0] + result[1][0]
        num_failed = result[1][1] + result[0][1]
        return num_failed / (num_successful + num_failed)

    def __init__(self, E_b: float, N_0: float, num_samples: int):
        self.E_b, self.N_0 = E_b, N_0
        self.x = np.linspace(0, PHI_T, PHI_NUM_SAMPLES)

        self.phi = np.cos(PHI_OMEGA * self.x)
        self.signals = np.sqrt(2 * E_b / PHI_T) * self.phi, -1 * np.sqrt(2 * E_b / PHI_T) * self.phi

        self.source = np.random.randint(0, 2, size=num_samples)

    def _perform_matched_filter(self, received: np.ndarray) -> Any:
        length = received.shape[0]
        return np.sum(received * self.phi / length)

    def _detect(self, received: np.ndarray) -> int:
        matched_filter_output = self._perform_matched_filter(received)
        if matched_filter_output > 0:
            return 0
        else:
            return 1

    def _transmit_and_detect(self, bit: int):
        transmitted = self.signals[bit]
        received = transmitted + utils.AWGN_like(transmitted, self.N_0)
        self.received.append(received)
        return self._detect(received)

    def perform(self):
        result = {
            0: [0, 0],
            1: [0, 0],
        }
        self.detected = self.source.copy()
        for i, bit in enumerate(self.source):
            self.detected[i] = self._transmit_and_detect(bit)
        for i, received in enumerate(self.detected):
            bit = self.source[i]
            if received == bit:
                result[bit][0] += 1
            else:
                result[bit][1] += 1
        return result

