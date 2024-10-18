pkg load control

num = [5,0];         % Numerator coefficients
den = [1, 2, 1];   % Denominator coefficients
H = tf(num, den);  % Create transfer function

% Plot root locus
figure;
rlocus(H);
title('Root Locus of the System');
grid on;

