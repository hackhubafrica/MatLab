#Example: Smith Chart for Impedance Matching

import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

# Define the transmission line parameters
Z0 = 50  # Characteristic impedance in ohms
ZL = 75 + 25j  # Load impedance

# Create a transmission line object
#line = rf.TLine(frequency=rf.Frequency(1, 10, 101, 'ghz'), z0=Z0)
# Create a media object for the transmission line
line = rf.media.DistributedCircuit(freq, z0=Z0)
load = line.load(ZL)

# Calculate the reflection coefficient
#gamma = (ZL - Z0) / (ZL + Z0)

# Plot the Smith chart
#plt.figure()
#smith_chart = rf.SmithChart(gamma)
#plt.show()


# Plot the Smith chart
plt.figure()
load.plot_s_smith()
plt.title('Smith Chart for Impedance Matching')
plt.show()

'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/Transmission Line Analysis with Smith Chart.py", line 5, in <module>
    import skrf as rf
ModuleNotFoundError: No module named 'skrf'
[Finished in 742ms with exit code 1]
[cmd: ['python3', '-u', '/home/dora/Electrical_ENGINEERING/Transmission Line Analysis with Smith Chart.py']]
[dir: /home/dora/Electrical_ENGINEERING]
[path: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/var/lib/snapd/snap/bin]
'''