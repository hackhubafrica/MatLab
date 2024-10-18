% Define transfer function G
s = tf('s');
G = (s+2)/(s^2+s+2);

% Step Response using Transfer Function
[x_tf,t_tf] = step(G);

figure;
plot(t_tf, x_tf,'LineWidth',2);
grid;
legend('s-domain function');
hold all

% Build Time Vector
dt = 0.01;
t = 0:dt:14;

% Build step input
u = ones(size(t));
u(1) = 0;

% Initial conditions
y0 = 0;
yd0 = 0;
ud0 = 0;

% Predefine the size of input/output vectors for numerical solution
ud = zeros(size(t));
y = zeros(size(t));
yd = zeros(size(t));
ydd = zeros(size(t));

% Numerical solution using Euler method
for i = 1:length(t)
    if i == 1
        ud(i) = ud0;
        yd(i) = yd0;
        y(i) = y0;
        ydd(i) = ud(i) + 2*u(i) - 2*y(i);
    else
        ud(i) = (u(i) - u(i-1))/dt;
        yd(i) = yd(i-1) + dt*ydd(i-1);
        y(i) = y(i-1) + dt*yd(i-1);
        ydd(i) = ud(i) + 2*u(i) - yd(i) - 2*y(i);
    end
end    

% Plot numerical solution
scatter(t, y, 3);
legend('s-domain function' , 'Differential equation approach');

% Convert to state-space representation
sys = ss(G);

% Simulate using state-space model
[x_ss, t_ss] = lsim(sys, u, t);

% Plot state-space solution
plot(t_ss, x_ss, '--r', 'LineWidth', 2);
legend('s-domain function' , 'Differential equation approach', 'State-space approach');
hold off

% Display the state-space matrices
[A, B, C, D] = ssdata(sys);
disp('State-space matrices:');
disp('A = '), disp(A)
disp('B = '), disp(B)
disp('C = '), disp(C)
disp('D = '), disp(D)
