#
# kondition.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
format long

N = 1000000;
A = [ N, N-1 ; N-1, N-2 ];

s = eig(A)

kappa = abs(s(2,1))/abs(s(1,1))

B = inverse(A)

A * B

