#
# 5002.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
format long

N = 13
Y = 0;
for k = (0:N)
	h = 2^(-k);
	n = 2^k;
	Y = 0;
	Z = 0;
	W = 0;
	U = 0;
	for i = (2:n+1)
		Y = Y + h * exp(Y);
		Z = Z + h * exp(Z + h * exp(Z)/2);
		W = W + h * (exp(W) + exp(W + h * exp(W)))/2;
		
		k1 = exp(U);
		k2 = exp(U + (h/2) * k1);
		k3 = exp(U + (h/2) * k2);
		k4 = exp(U + h * k3);
		U = U + (h/6) * (k1 + 2*k2 + 2*k3 + k4);
	end
	printf("%2d & %14.8f & %14.8f & %14.8f & %14.8f\\\\\n", k, Y, Z, W, U)
end

function retval = f(x, t)
	retval = exp(x);
end

M=7
t = zeros(M,1);
for k = (1:M-1)
	t(k+1,1) = 1 - 10^(-k);
end
t

lsode_options()
lsode_options("step limit", 1000000000)
lsode_options()

x = lsode(@f, 0, t)

X = x
X(1:M,2) = -log(1-t)

printf("Vereinfachte Runge-Kutta Schritte\n")

function xneu = vrk(h, t, x)
	k = f(x, t);
	xneu = x + (h/2) * (k + f(x + h * k, t + h));
end

printf("Runge-Kutta Schritt\n")

k1 = 1
k2 = exp(0.5 * k1)
k3 = exp(0.5 * k2)
k4 = exp(k3)

(1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
