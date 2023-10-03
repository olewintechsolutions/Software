
# imagenary and real phase

import matplotlib as mp
import numpy as np

# Define the magnitude and phase of the electromagnetic field
amplitude = 2.0  # Magnitude of the field
phase_degrees = 45  # Phase of the field in degrees

# Convert phase from degrees to radians
phase_radians = np.deg2rad(phase_degrees)

# Calculate the real and imaginary parts using Euler's formula
real_part = amplitude * np.cos(phase_radians)
imaginary_part = amplitude * np.sin(phase_radians)

# Display the results
print("Amplitude:", amplitude)
print("Phase (degrees):", phase_degrees)
print("Phase (radians):", phase_radians)
print("Real Part:", real_part)
print("Imaginary Part:", imaginary_part)

phase_radians.set_title('title here')
phase_radians.set_xlabel('x-axis label')
phase_radians.set_ylabel('y-axis label')

plt.phase_radians()
plt.show()
plt.index()

imaginary_part.set_title('title here')
imaginary_part.set_xlabel('x-axis label')
imaginary_part.set_ylabel('y-axis label')
plt.imaginary_part()
plt.show()
plt.index()
