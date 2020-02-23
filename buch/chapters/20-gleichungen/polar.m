#
# polar.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
format long

function retval = f(v, x, y)
	r = v(1,1);
	phi = v(2,1);
	f = [ r*cos(phi) - x; r*sin(phi) - y ];
	D = [ cos(phi), -r * sin(phi) ; sin(phi) , r * cos(phi) ];
	retval = v - inverse(D) * f;
endfunction

r = 1;
phi = 1;
x = r * cos(phi);
y = r * sin(phi);

v = [ pi; exp(-1) ]

printf("%d & %20.16f & %20.16f \\\\\n", 0, v(1,1), v(2, 1));

for k = (1:20)
	v = f(v, x, y);
	printf("%d & %20.16f & %20.16f \\\\\n", k, v(1,1), v(2, 1));
endfor
