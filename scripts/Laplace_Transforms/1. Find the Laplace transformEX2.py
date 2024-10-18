import sympy as sp
#𝑓(𝑡)=cos⁡(3𝑡)
t = sp.symbols('t')
# Define the function
f = sp.cos(3*t)

# Compute the Laplace transform
F = sp.laplace_transform(f, t, s)
F

'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/scripts/1. Find the Laplace transformEX2.py", line 8, in <module>
    F = sp.laplace_transform(f, t, s)
                                   ^
NameError: name 's' is not defined. Did you mean: 'sp'?
[Finished in 536ms with exit code 1]
[cmd: ['python3', '-u', '/home/dora/Electrical_ENGINEERING/scripts/1. Find the Laplace transformEX2.py']]
[dir: /home/dora/Electrical_ENGINEERING/scripts]
[path: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/var/lib/snapd/snap/bin]
'''