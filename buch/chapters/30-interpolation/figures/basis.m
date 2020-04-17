#
# basis.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
global n;
n = 6;
s = 20;
global steps;
steps = (2 * s + 2) * (n + 1);
global xi;
xi = (0:n);
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

fn = fopen("basispaths.tex", "w");

function draw(fn, i, name)
	global steps;
	global n;
	fprintf(fn, "\\def\\basis%s{\n", name);
	x = -0.5 + (0:steps) * (n+1)/steps;
	fprintf(fn, "\\draw[line width=1.4pt,color=red] (%.4f,{%.4f*\\yskala})", x(1), l(x(1), i));
	for j = (1:steps)
		fprintf(fn, "\n\t--(%.4f,{%.4f*\\yskala})", x(j+1), l(x(j+1), i));
	endfor
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
	
