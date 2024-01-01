import matplotlib.pyplot as plt
import numpy as np

import bep_formula
import utils

X_START, X_END, NUM = -8, 17, 10001
Y_LIMIT = 10 ** -7, 1
FIGURE_SIZE = 5, 6

PADDING = 2.5

SHANNON_LIMIT = -1.6
SHANNON_LIMIT_Y = 10 ** -0.25


def setup_plot():
    plt.figure(figsize=FIGURE_SIZE)
    plt.yscale('log')
    plt.ylim(*Y_LIMIT)
    plt.tight_layout(pad=PADDING)
    plt.plot([SHANNON_LIMIT, SHANNON_LIMIT], [SHANNON_LIMIT_Y, Y_LIMIT[0]],
             color='black',
             label='Shannon Limit (-1.6 dB)')
    plt.plot([X_START, SHANNON_LIMIT], [SHANNON_LIMIT_Y, SHANNON_LIMIT_Y], color='black')
    plt.ylabel('Bit Error Probability $P_B$')
    plt.xlabel(r'$E_b/N_0$ (dB)')
    plt.margins(x=0)
    plt.xticks(np.arange(-8, 18, step=2))


def main():
    x = np.linspace(X_START, X_END, NUM)
    x_in_magnitude = utils.restore_dB(x)
    LINES = (
        (bep_formula.coherent_BPSK, 'Coherent BPSK', ),
        (bep_formula.coherent_DPSK, 'Coherent DPSK', ),
        (bep_formula.coherent_BFSK, 'Coherent BFSK', ),
        (bep_formula.non_coherent_BFSK, 'Non-Coherent BFSK', ),
    )
    setup_plot()
    for f, label in LINES:
        y = f(x_in_magnitude)
        plt.plot(x, y, label=label)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
