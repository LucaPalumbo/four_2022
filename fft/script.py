import numpy as np
import matplotlib.pyplot as plt
import os


# plot in the same figure 2 plots. One above and the other below. The upper one is the real data over time, the lower one is the fft output over frequency
def plot_fft(time, signal, fft_output, frequencies_x, file_name):
    fig, (ax1, ax2) = plt.subplots(2, 1,constrained_layout=True)
    #fig.tight_layout()
    ax1.plot(time, signal)
    ax1.set_xlabel('Time [us]')
    ax1.set_ylabel('Signal [arb.un]')
    ax2.plot(frequencies_x / 1e3, fft_output)
    ax2.set_yscale('log')
    ax2.set_ylabel('FFT [arb.un]')
    ax2.set_xlabel('Frequency [kHz]')
    plt.savefig(f"./plots/{file_name}.png")
    #plt.show()


if __name__ == "__main__":
    files_list = os.listdir("./rlc")
    # remove the extension from the file name
    files_list = [file_name.split(".")[0] for file_name in files_list]
    # leave in files_list only the string that contains "fft"
    files_list = [file_name for file_name in files_list if "fft" in file_name]

    for file_name in files_list:
        time, signal = np.loadtxt(f'./rlc/{file_name}.txt', delimiter=' ', unpack=True)
        N = len(time)
        time = time * 1e-6

        # real data
        C = 0.22e-6 # F
        L = 0.5 # H
        omega = 1 / np.sqrt(L*C)
        print(f"frequency = {omega / (2*np.pi)} Hz")

        # calculate the sampling frequency
        fs = 1 / (np.mean(np.diff(time)) )
        dteff = np.mean(np.diff(time))
        f_max = 1 / (2 * dteff)
        print(f"delta t while sampling data: {dteff} us")
        print(f"max frequency in fourier analysis {f_max}")

        # perform fft real
        fft_output = abs(np.fft.rfft(signal))
        print(f"how many fft data?: {len(fft_output)}") # should be N/2 + 1 = 1025

        # calculate the frequency axis
        frequencies_x = np.linspace(0,f_max,len(fft_output))

        plot_fft(time, signal, fft_output, frequencies_x, file_name)







