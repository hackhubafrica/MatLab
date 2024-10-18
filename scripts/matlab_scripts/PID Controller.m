Kp = 2;  % Proportional gain
Ki = 1;  % Integral gain
Kd = 0.5;  % Derivative gain

% Create PID controller
C = pid(Kp, Ki, Kd);

% Closed-loop system (feedback)
sys_closed_loop = feedback(C * H, 1);

% Step response of the closed-loop system
figure;
step(sys_closed_loop);
title('Step Response of the Closed-Loop PID Controlled System');
grid on;

