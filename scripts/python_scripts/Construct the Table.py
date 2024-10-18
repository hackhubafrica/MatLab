from sympy import symbols, laplace_transform, Heaviside, exp, sin, cos, sqrt, factorial, pi, Function, DiracDelta, inverse_laplace_transform
from sympy.abc import t, s, a, b, c

# Define symbols and functions
t, s, a, b, c = symbols('t s a b c')

# Table of Laplace Transforms (partial list)
laplace_table = {
    "1": laplace_transform(1, t, s)[0],
    "e^at": laplace_transform(exp(a*t), t, s)[0],
    "t^n, n = 1, 2, 3, ...": laplace_transform(t**n / factorial(n), t, s)[0],
    "t^p, p > -1": laplace_transform(t**p, t, s)[0],
    "sqrt(t)": laplace_transform(sqrt(t), t, s)[0],
    "sin(at)": laplace_transform(sin(a*t), t, s)[0],
    "cos(at)": laplace_transform(cos(a*t), t, s)[0],
    "t*sin(at)": laplace_transform(t*sin(a*t), t, s)[0],
    "t*cos(at)": laplace_transform(t*cos(a*t), t, s)[0],
    "sin(at) - at*cos(at)": laplace_transform(sin(a*t) - a*t*cos(a*t), t, s)[0],
    "sin(at) + at*cos(at)": laplace_transform(sin(a*t) + a*t*cos(a*t), t, s)[0],
    "cos(at) - at*sin(at)": laplace_transform(cos(a*t) - a*t*sin(a*t), t, s)[0],
    "cos(at) + at*sin(at)": laplace_transform(cos(a*t) + a*t*sin(a*t), t, s)[0],
    "sinh(at)": laplace_transform((exp(a*t) - exp(-a*t))/2, t, s)[0],
    "cosh(at)": laplace_transform((exp(a*t) + exp(-a*t))/2, t, s)[0],
    "e^at * sin(bt)": laplace_transform(exp(a*t)*sin(b*t), t, s)[0],
    "e^at * cos(bt)": laplace_transform(exp(a*t)*cos(b*t), t, s)[0],
    "t^n * e^at, n = 1, 2, 3, ...": laplace_transform(t**n * exp(a*t), t, s)[0],
    "f(ct), c > 0": 1/c * laplace_transform(Function('f')(c*t), t, s)[0],
    "u_c(t) = u(t-c)": exp(-c*s) / s,
    "δ(t-c)": exp(-c*s),
    "u_c(t) * f(t - c)": exp(-c*s) * laplace_transform(Function('f')(t - c), t, s)[0],
    "u_c(t) * g(t)": exp(-c*s) * laplace_transform(Function('g')(t + c), t, s)[0],
    "e^ct * f(t)": laplace_transform(exp(c*t) * Function('f')(t), t, s)[0],
    "t^n * f(t), n = 1, 2, 3, ...": factorial(n) * inverse_laplace_transform(s**(n+1) * Function('F')(s), s, t)[0],
    "1/t * f(t)": inverse_laplace_transform(Function('f')(t) / t, s, t)[0],
    "∫_0^t f(v) dv": inverse_laplace_transform(Function('F')(s) / s, s, t)[0],
    "∫_0^t f(t - τ) g(τ) dτ": inverse_laplace_transform(Function('F')(s) * Function('G')(s), s, t)[0],
    "f(t + T) / (1 - e^(-sT))": laplace_transform(Function('f')(t + T), t, s)[0] / (1 - exp(-s*T)),
    "f'(t)": s * Function('F')(s) - Function('f')(0),
    "f''(t)": s**2 * Function('F')(s) - s * Function('f')(0) - Function('f')(0),
    "f^(n)(t)": s**n * Function('F')(s) - sum(s**(n-i) * Function('f')**(i-1)(0) for i in range(1, n))
}

# Print the Laplace transforms table
print("Table of Laplace Transforms:")
for key, value in laplace_table.items():
    print(f"{key}: {value}")