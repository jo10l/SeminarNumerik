#
# romberg.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
format long;

a = 0;
b = pi;
h = b - a;

function y = f(x)
	y = sin(x);
endfunction

function summe = M(h, a, b, f)
	x = a + h/2;
	s = 0;
	while (x < b)
		s = s + f(x);
		x = x + h;
	end
	summe = h * s;
endfunction

R = zeros(10, 4);

T = h * ( (1/2) * f(a) + (1/2) * f(b) )
R(1,1) = T;

N = 14

for k = (2:N)
	T = (1/2) * T + (1/2) * M(h, a, b, @f)
	R(k,1) = T;
	h = h/2;
endfor

for k = (2:N)
	R(k,2) = (4*R(k,1)-R(k-1,1))/3;
endfor

for k = (3:N)
	R(k,3) = (16*R(k,2)-R(k-1,2))/15;
endfor

for k = (4:N)
	R(k,4) = (64*R(k,3)-R(k-1,3))/63;
endfor

R

printf("%2d&%20.16f&                    &                    \\\\\n", 1, R(1,1));
printf("%2d&%20.16f&%20.16f&                    \\\\\n", 2, R(2,1), R(2,2));
for k = (3:N)
	printf("%2d&%20.16f&%20.16f&%20.16f\\\\\n", k, R(k,1), R(k,2), R(k,3));
endfor



