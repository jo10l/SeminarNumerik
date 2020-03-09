#
# basis.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
global n;
n = 6;
global steps;
steps = 201;
global xi;
xi = (0:n);
N = n + 1;
xi = -cos(pi * (2*(1:N)-1) / (2 * N))
global c;
c = ones(n+1,1);

for i = (0:n)
	for j = (0:n)
		if (i != j)
			c(i+1,1) = c(i+1,1) * (xi(j+1)-xi(i+1));
		endif
	endfor
	c(i+1) = 1 / c(i+1);
endfor

c

function y = l(x, i)
	global n;
	global xi;
	global c;
	y = c(i+1);
	for j = (0:n)
		if (i != j) 
			y = y * (x - xi(j+1));
		endif
	endfor
endfunction

fn = fopen("tschebasispaths.tex", "w");

fprintf(fn, "\\def\\stuetz{\n");
for i = (0:n)
	fprintf(fn, "\\draw ({%.4f*\\xskala},{-0.1/\\skala})--({%.4f*\\xskala},{0.1/\\skala});\n", xi(i+1), xi(i+1));
	if (i == 3)
		position = "below right";
	else
		position = "below";
	endif
	fprintf(fn, "\\node at ({%.4f*\\xskala},{-0.1/\\skala}) [%s] {$x_%d$};\n", xi(i+1), position, i);
endfor
fprintf(fn, "}\n");

function draw(fn, i, name)
	global xi;
	global steps;
	global n;
	fprintf(fn, "\\def\\basis%s{\n", name);
	x = -1 + (0:steps) * 2/steps;
	fprintf(fn, "\\draw[line width=1.4pt,color=red] ({%.4f*\\xskala},{%.4f*\\yskala})", x(1), l(x(1), i));
	for j = (1:steps)
		fprintf(fn, "\n\t--({%.4f*\\xskala},{%.4f*\\yskala})", x(j+1), l(x(j+1), i));
	endfor
	fprintf(fn, ";\n}\n");
	fprintf(fn, "\\def\\punkt%s{\n", name);
	fprintf(fn, "\\fill[color=red] ({%.4f*\\xskala},\\yskala) circle[radius={0.08/\\skala}];\n", xi(i+1));
	fprintf(fn, ";\n}\n");
endfunction

draw(fn, 0, "zero");
draw(fn, 1, "one");
draw(fn, 2, "two");
draw(fn, 3, "three");
draw(fn, 4, "four");
draw(fn, 5, "five");
draw(fn, 6, "six");

fclose(fn);
	
