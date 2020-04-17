#
# fuenf.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#

function retval = g(x, a, k)
	retval = (1/k) * ((k-1)*x + a/(x^(k-1)));
endfunction

a = 10;
k = 5;

format long

a^(1/k)

x = 10;
for i = (1:20)
	x = g(x, a, k)
endfor

