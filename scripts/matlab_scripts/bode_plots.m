pkg load control;  % Load the control package

% Define the transfer function H(s) = 1 / (s^2 + 2s + 1)
num = [1];         % Numerator coefficients
den = [1, 2, 1];   % Denominator coefficients
H = tf(num, den);  % Create transfer function

% Display the transfer function
disp(H);

figure;
bode(H);
title('Bode Plot of the Mass-Spring-Damper System');
grid on;

