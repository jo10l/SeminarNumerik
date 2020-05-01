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
	for i = (2:n+1)
		Y = Y + h * exp(Y);
		Z = Z + h * exp(Z + h * exp(Z)/2);
		W = W + h * (exp(W) + exp(W + h * exp(W)))/2;
	end
	printf("%02d & %20.16f & %20.16f & %20.16f \\\\\n", k, Y, Z, W)
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

