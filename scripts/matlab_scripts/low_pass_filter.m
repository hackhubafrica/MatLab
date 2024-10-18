pkg load control
% Define transfer function G
s = tf('s');

G1 = 1/(s+1)
G2 = 1/s(s+1)
G3 = s/(s+1)
h = figure;
%h.Position = [141, 379 ,800,240 ];
stepinfo(G1)
step(G1)
set(findall(gcf,'type','line' ),'linewidth',4);
stepinfo(G1)
