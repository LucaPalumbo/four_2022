import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq
from scipy.signal import hann

time,  signal,  = np.loadtxt('./rlc/indallsegfin_fft.txt', delimiter=' ', unpack=True)
time = time
signal = signal
N = len(time)

plt.plot(time, signal)
plt.show()

# Calculate the sampling frequency
fs = 1 / (np.mean(np.diff(time)) )

# Perform FFT on the windowed data
fft_output = fft(signal)


# Calculate the frequency axis
freqs = fftfreq(len(signal), 1/fs)[:N//2]


# Plot the magnitude of the FFT output versus frequency
plt.plot(freqs, 2/N * np.abs(fft_output[:N//2]))
plt.yscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.show()