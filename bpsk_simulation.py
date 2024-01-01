import matplotlib.pyplot as plt
import random

import utils
from bpsk import BPSKExperiment
import bep_formula

Ebs = [2000, 4000, 8000]
NUM_SAMPLES = 100000
N0 = 2000


def main():
    for Eb in Ebs:
        experiment = BPSKExperiment(Eb, N0, NUM_SAMPLES)
        result = experiment.perform()

        Eb_over_N0 = Eb / N0
        Eb_over_N0_in_db = utils.magnitude_to_dB(Eb_over_N0)
        print(f"====== Eb/N0 = {Eb_over_N0_in_db} db ======")
        # print(result)
        print(f"Theoretical BER: {bep_formula.coherent_BPSK(Eb_over_N0)}")
        print(f"BER from Experiment: {BPSKExperiment.calculate_BER(result)}")
        print("")


if __name__ == '__main__':
    main()
