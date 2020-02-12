#
# normal.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#

M = 10;
sy = 1;

fn = fopen("normpaths.tex", "w");

function	y = f(x)
	y = exp(-x.^2/2) / sqrt(2*pi);
endfunction

function	yi = inter(x, y, xi)
	yi = 0;
	n = size(x, 2);
	for i = (1:n)
		l = 1;
		for j = (1:n)
			if (j == i)
				continue;
			else
				l *= (xi - x(j)) / (x(i) - x(j));
			endif
		endfor
		yi += y(i) * l;
	endfor
endfunction

function	yi = inter1(x, y, xi)
	n = size(xi, 2);
	yi = zeros(1,n);
	for i = (1:n)
		yi(i) = inter(x, y, xi(i));
	endfor
endfunction

characters = "abcdefghijklmnopqrstuvwxyz";

for n = (1:17);
	N = 2*n;
	s = 5 / max(N);
	x = (0:N) * s;
	y = zeros(size(x));

	for i = (0:N)
		y(1,i+1) = f(s * i);
	endfor

	fprintf(fn, "\\def\\xwerte%c{\n", characters(n));
	for i = 0:N
		fprintf(fn, "\\fill[color=red] (%.4f,0) circle[radius={0.07/\\skala}];\n", x(i+1));
	endfor
	fprintf(fn, "}\n");

	fprintf(fn, "\\def\\punkte%c{%d}\n", characters(n), N);

	X = (0:500) * 0.01;
	Y = inter1(x, y, X);
	fehler = Y - f(X);
	maxfehler = max(abs(fehler));
	relfehler = fehler./Y;

	fehler = fehler/maxfehler;

	exponent = ceil(log10(maxfehler)-1)
	mantisse = maxfehler * 10^(-exponent);

	fprintf(fn, "\\def\\maxfehler%c{%.3f\\cdot 10^{%d}}\n", characters(n), mantisse, exponent);
	fprintf(fn, "\\def\\fehler%c{\n", characters(n));
	fprintf(fn, "\\draw[color=red,line width=1.4pt,line join=round] ({\\sx*(%.3f)},{\\sy*(%.4f)})", X(1,1), sy * fehler(1,1));
	for i = (1:500)
		fprintf(fn, "\n\t--({\\sx*(%.4f)},{\\sy*(%.4f)})", X(1,i+1), sy * fehler(1,i+1));
	endfor
	fprintf(fn, ";\n}\n");

	fprintf(fn, "\\def\\relfehler%c{\n", characters(n));
	fprintf(fn, "\\draw[color=blue,line width=1.4pt,line join=round] ({\\sx*(%.3f)},{\\sy*(%.4f)})", X(1,1), relfehler(1,1));
	for i = (1:500)
		fprintf(fn, "\n\t--({\\sx*(%.4f)},{\\sy*(%.4f)})", X(1,i+1), relfehler(1,i+1));
	endfor
	fprintf(fn, ";\n}\n");



endfor

fclose(fn);
