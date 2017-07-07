import sys

import numpy as np
import scipy.io.wavfile as wav
from scipy import signal


def find_region(f1, f2):
    c = signal.fftconvolve(f1, f2[::-1], mode='valid')
    top = np.argmax(c)
    return top

if __name__ == "__main__":

    f1_path = sys.argv[1]
    f2_path = sys.argv[2]

    f1_rate, f1 = wav.read(f1_path)
    f2_rate, f2 = wav.read(f2_path)

    top_corrs = find_region(f1, f2)

    print "\n\n\"{}\" most likely starts in \"{}\" at sample:  {}".format(f2_path, f1_path, top_corrs)
