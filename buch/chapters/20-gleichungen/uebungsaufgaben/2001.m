#
# 2001.m -- Nullstelle mit Newton findn
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#

function retval = N(x)
	retval = x - (x^5-(5/4)*x^4+1/4)/(5*(x-1)*x^3);
endfunction

x = -0.0001;

format long

for i = (1:200)
	x = N(x)
endfor
