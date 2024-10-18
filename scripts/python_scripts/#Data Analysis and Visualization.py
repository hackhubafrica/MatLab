'''
Libraries:
	Pandas: For data manipulation and analysis.
	Matplotlib: For plotting data.

'''

import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
data = pd.read_csv('data.csv')

# Plot data
plt.plot(data['time'], data['voltage'])
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Time')
plt.grid(True)
plt.show()


'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/#Data Analysis and Visualization.py", line 12, in <module>
    data = pd.read_csv('data.csv')
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
             ^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
[Finished in 4.5s with exit code 1]
[cmd: ['python3', '-u', '/home/dora/Electrical_ENGINEERING/#Data Analysis and Visualization.py']]
[dir: /home/dora/Electrical_ENGINEERING]
[path: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/var/lib/snapd/snap/bin]
'''