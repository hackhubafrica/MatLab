pkg load control
% Define transfer function G
s = tf('s');
G = (s+2)/(s^2+s+2);

%Step Response
[x,t] = step(G);

%display(stepinfo(G));
stepinfo(G);

plot(t, x,'LineWidth',2);
grid;
legend('s-domain function');
hold all

% Build Time Vector
dt = 0.01;
t = 0:dt:14;

% Build step input
u = ones(size(t));
u(1) = 0;

% Initial condition
y0 = 0;
yd0 = 0;
ud0 = 0;

% Predefine the size of inpu/output vectors
ud = zeros(size(t));
y = zeros(size(t));
yd = zeros(size(t));
ydd = zeros(size(t));


% Step through time and solve the differentila equation
for i = 1:length(t)
    if i == 1
        ud(i) = ud0;
        yd(i) = yd0;
        y(i) = y0;
        ydd(i) = ud(i) + 2*u(i) -2*y(i);
    else
        ud(i) = (u(i) - u(i-1))/dt;
        yd(i) = yd(i-1) + dt*ydd(i-1);
        y(i) = y(i-1) + dt*yd(i-1);
        ydd(i) = ud(i) + 2*u(i) - yd(i) - 2*y(i);
    end
end

scatter(t, y, 3);
legend('s-domain function' , 'Differantial equation approach')


% Convert to state space representation
sys = ss(G);
A = [-1, -2; 1, 0];
B = [2; 0];
C = [0.5, 1];
D = 0;


% Initial conditions
x0 = [0; 0];
xd0 = [0; 0];

% Predefine the size of state/output vectors
x = zeros(2, length(t));
xd = zeros(2, length(t));
y = zeros(size(t));

% step through time and solve the DE
for i = 1:length(t)
    if i == 1
        x(:, i) = x0;
        xd(:, i) = A*x0 + B*u(i);
        y(i) = C*x0 + D*u(i);
    else
        x(:, i) = x0;
        xd(:,i) = A*x0 + B*u(i);
        y(i) = C*x(:,i) + D*u(i);

    end
end

scatter(t, y,3);
legend('s-domain function', 'Differential equation approach','state-space approach')
