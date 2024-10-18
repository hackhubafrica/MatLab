% Define the function as an anonymous function
f = @(x) (x.^2)/2 + x + 1/2;

% Create a range of x values
x = linspace(0, 3, 100);  % From x = 0 to x = 3

% Calculate corresponding y values using the function
y = f(x);

% Plot the results
figure;
plot(x, y, 'b-', 'LineWidth', 2);
hold on;
plot(1, 2, 'ro', 'MarkerSize', 8); % Initial condition point
text(1, 2, ' (1, 2)', 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
xlabel('x');
ylabel('y');
title('Solution of the Differential Equation dy/dx = x + 1');
grid on;
legend('y = (x^2)/2 + x + 1/2', 'Initial Condition (1, 2)');
hold off;