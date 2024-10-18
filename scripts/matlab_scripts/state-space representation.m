pkg load control;  % Load control package

% Define matrices A, B, C, D
A = [0 1; -1  -2];        % State matrix
B = [0; 1];               % Input matrix
C = [1 0];                % Output matrix
D = 0;                    % Feedforward matrix

% Create state-space system
sys_ss = ss(A, B, C, D);

% Display the state-space system
disp(sys_ss);

% Step response of the state-space system
figure;
step(sys_ss);
stepinfo(sys_ss)
title('Step Response of the State-Space Model');
grid on;


% Compute eigenvalues
eigenvalues = eig(A);
%For a continuous system, if all eigenvalues of matrix
%A have negative real parts, the system is stable.

% Display eigenvalues
disp('Eigenvalues of the system:');
disp(eigenvalues);

num = [1];         % Numerator coefficients
den = [1, 2, 1];   % Denominator coefficients
H = tf(num, den);  % Create transfer function

% Plot root locus
figure;
rlocus(H);
title('Root Locus of the System');
grid on;

