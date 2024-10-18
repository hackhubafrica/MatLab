# f(t)=sin(2t)cos(2t)
import sympy as sp

# Define the variable and function
t = sp.symbols('t')
f = sp.sin(2*t) * sp.cos(2*t)

# Compute the Laplace transform
F = sp.laplace_transform(f, t, sp)
F

'''
Result:
F(s)= 4/s**2 +4

Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/scripts/1. Find the Laplace transform of the following functions.py", line 9, in <module>
    F = sp.laplace_transform(f, t, sp)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/sympy/integrals/laplace.py", line 1457, in laplace_transform
    LT, p, c = LaplaceTransform(f, t, s).doit(noconds=False,
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/sympy/core/cache.py", line 72, in wrapper
    retval = cfunc(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/sympy/core/function.py", line 466, in __new__
    result = super().__new__(cls, *args, **options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/sympy/core/cache.py", line 72, in wrapper
    retval = cfunc(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/sympy/core/function.py", line 297, in __new__
    args = list(map(sympify, args))
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/sympy/core/sympify.py", line 465, in sympify
    raise SympifyError('cannot sympify object of type %r' % type(a))
sympy.core.sympify.SympifyError: SympifyError: "cannot sympify object of type <class 'module'>"
[Finished in 533ms with exit code 1]
[cmd: ['python3', '-u', '/home/dora/Electrical_ENGINEERING/scripts/1. Find the Laplace transform of the following functions.py']]
[dir: /home/dora/Electrical_ENGINEERING/scripts]
[path: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/var/lib/snapd/snap/bin]
'''


