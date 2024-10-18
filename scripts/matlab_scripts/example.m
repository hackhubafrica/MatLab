pkg load control  # Load the control package
pkg load signal
% Define the transfer function H(s) = 1 / (s^2 + 2s + 1)
num = [1];
den = [1, 2, 1];
H = tf(num, den);

% Display the transfer function
disp(H);

% Example: Create a transfer function and apply a filter (signal processing)
H = tf([1], [1, 2, 1]);  % Transfer function from the control package
disp(H);
figure;
grid on;
