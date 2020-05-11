#
# 6001.m -- Berechnungen zur Aufgabe 6001.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
N = 6;

E = eye(N*N);
A = 4 * E;

A = A - shift(E, 1);
A = A - shift(E, -1);

A = A - shift(E, 10);
A = A - shift(E, -10);

sum(A);
sum(A,2);

eig(A)
max(abs(eig(A)))

D = E - 0.1 * A;

eig(D)
max(abs(eig(D)))
