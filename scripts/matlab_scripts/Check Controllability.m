pkg load control;  % Load control package

% Define matrices A, B, C, D
A = [0 1; -1  -2];        % State matrix
B = [0; 1];               % Input matrix
C = [1 0];                % Output matrix
D = 0;                    % Feedforward matrix


%Controllability determines whether the state of a system can be driven to any desired state using the inputs.
%Observability determines whether the current state of a system can be inferred by observing the output.


% Controllability matrix
Co = [B A*B];

% Rank check for controllability
if rank(Co) == size(A, 1)
    disp('The system is controllable.');
else
    disp('The system is not controllable.');
end


% Observability matrix
Ob = [C; C*A];

% Rank check for observability
if rank(Ob) == size(A, 1)
    disp('The system is observable.');
else
    disp('The system is not observable.');
end



