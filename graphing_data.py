import matplotlib.pyplot as plt
import scipy
import pandas as pd
import numpy as np
import scipy.datasets
import scipy.signal

ekg = scipy.datasets.electrocardiogram()

ekg = pd.Series(ekg)

r_waves, metadata = scipy.signal.find_peaks(ekg[:21600], height= 1.0)

print("BPM:", len(r_waves))
print("Peak Heights:", metadata["peak_heights"])

plt.figure(figsize=(13, 10))
plt.plot(ekg[:21600], label="ECG Signal")
plt.plot(r_waves, ekg[r_waves], "x", label="R-peaks", color="red")
plt.title("ECG Signal with Detected R-peaks")
plt.xlabel("Time Steps")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()