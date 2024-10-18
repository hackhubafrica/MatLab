pkg load control;  % Load control package

% Define the transfer function H(s)
num = [10,0];         % Numerator coefficients
den = [3, 1, 6];   % Denominator coefficients
H = tf(num, den);  % Create transfer function

% Frequency vector (from 0.01 to 10 rad/s)
omega = logspace(-2, 1, 100);  % 100 points from 0.01 to 10 rad/s

% Compute frequency response
[mag, phase, w] = bode(H, omega);

% Convert magnitude to dB
mag_dB = 20 * log10(mag(:));

% Plot Magnitude and Phase Response
figure;
subplot(2, 1, 1);
semilogx(w, mag_dB);
xlabel('Frequency (rad/s)');
ylabel('Magnitude (dB)');
title('Magnitude Response');
grid on;

subplot(2, 1, 2);
semilogx(w, phase(:));
xlabel('Frequency (rad/s)');
ylabel('Phase (degrees)');
title('Phase Response');
grid on;


% Generate Bode plot for the transfer function
figure;
bode(H);
title('Bode Plot of the System');
grid on;

% Generate Nyquist plot for the transfer function
figure;
nyquist(H);
title('Nyquist Plot of the System');
grid on;

% Calculate gain and phase margins
[Gm, Pm, Wcg, Wcp] = margin(H);

% Display results
disp(['Gain Margin (dB): ', num2str(20*log10(Gm))]);
disp(['Phase Margin (degrees): ', num2str(Pm)]);
disp(['Gain Crossover Frequency (rad/s): ', num2str(Wcg)]);
disp(['Phase Crossover Frequency (rad/s): ', num2str(Wcp)]);

