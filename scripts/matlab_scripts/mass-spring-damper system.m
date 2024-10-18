pkg load control;  % Load the control package

% Define the transfer function H(s) = 1 / (s^2 + 2s + 1)
num = [1];         % Numerator coefficients
den = [1, 2, 1];   % Denominator coefficients
H = tf(num, den);  % Create transfer function

% Display the transfer function
disp(H);

% Compute and plot the step response
figure;
t =20
step(H ,T=t);
title('Step Response of the Mass-Spring-Damper System');
%grid on;

info = stepinfo(H);  % Get step response characteristics

% Display the characteristics
fprintf('Rise Time: %f s\n', info.RiseTime);
fprintf('Overshoot: %f %%\n', info.Overshoot);
fprintf('Settling Time: %f s\n', info.SettlingTime);
fprintf('Steady-State Error: %f\n', abs(1 - info.SettlingMin)); % assuming final value is 1


figure;
bode(H);
title('Bode Plot of the Mass-Spring-Damper System');
grid on;

