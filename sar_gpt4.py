import numpy as np
import matplotlib.pyplot as plt

# Radar parameters
frequency = 5.3e9                 # Radar frequency (5.3 GHz)
wavelength = 3e8 / frequency      # Radar wavelength
antenna_height = 500              # Antenna height (meters)
range_resolution = 1              # Range resolution (meters)
scene_length = 1000               # Scene length (meters)

# SAR processing parameters
pulse_length = 1e-6               # Pulse length (seconds)
pulse_bandwidth = 1 / pulse_length
sampling_rate = 2 * pulse_bandwidth
range_sampling = 3e8 / (2 * sampling_rate)
n_samples = int(scene_length / range_sampling)

# Synthetic aperture
n_pulses = 100                    # Number of transmitted pulses
aperture_length = 100             # Aperture length (meters)
aperture_velocity = 20            # Aperture velocity (m/s)
aperture_sampling = aperture_length / n_pulses
pulse_interval = aperture_sampling / aperture_velocity

# Create a flat surface
surface = np.zimport numpy as np
import matplotlib.pyplot as plt

# Radar parameters
frequency = 5.3e9                 # Radar frequency (5.3 GHz)
wavelength = 3e8 / frequency      # Radar wavelength
antenna_height = 500              # Antenna height (meters)
range_resolution = 1              # Range resolution (meters)
scene_length = 1000               # Scene length (meters)

# SAR processing parameters
pulse_length = 1e-6               # Pulse length (seconds)
pulse_bandwidth = 1 / pulse_length
sampling_rate = 2 * pulse_bandwidth
range_sampling = 3e8 / (2 * sampling_rate)
n_samples = int(scene_length / range_sampling)

# Synthetic aperture
n_pulses = 100                    # Number of transmitted pulses
aperture_length = 100             # Aperture length (meters)
aperture_velocity = 20            # Aperture velocity (m/s)
aperture_sampling = aperture_length / n_pulses
pulse_interval = aperture_sampling / aperture_velocity

# Create a flat surface
surface = np.zeros(n_samples)

# Simulate radar backscatter
for pulse in range(n_pulses):
    time_delay = 2 * antenna_height / 3e8
    time_index = int(time_delay * sampling_rate)
    surface[time_index] += 1

# Range compression
range_compressed = np.fft.ifft(np.fft.fft(surface) * np.fft.fft(surface))

# Plot the result
plt.plot(range_compressed.real)
plt.xlabel("Range (m)")
plt.ylabel("Amplitude")
plt.title("SAR range-compressed signal")
plt.show()eros(n_samples)

# Simulate radar backscatter
for pulse in range(n_pulses):
    time_delay = 2 * antenna_height / 3e8
    time_index = int(time_delay * sampling_rate)
    surface[time_index] += 1

# Range compression
range_compressed = np.fft.ifft(np.fft.fft(surface) * np.fft.fft(surface))

# Plot the result
plt.plot(range_compressed.real)
plt.xlabel("Range (m)")
plt.ylabel("Amplitude")
plt.title("SAR range-compressed signal")
plt.show()