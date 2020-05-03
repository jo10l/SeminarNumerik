#
# thomas.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
format long
n = 13
c = ones(n,1);
d = ones(n,1);
d(1,1) = d(1,1)/(-2);
c(1,1) = -0.5;
for i = (2:n)
	c(i,1) = 1/(-2-c(i-1,1));
	d(i,1) = (d(i,1)-d(i-1,1)) * c(i,1);
	c(i,1) * (i+1)
end
c
d

E = eye(n);
A = shift(E,1) + shift(E,-1) - 2*E ;
A(1,n) = 0;
A(n,1) = 0;

A \ ones(n,1)

