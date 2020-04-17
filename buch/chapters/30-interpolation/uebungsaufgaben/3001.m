#
# 3001.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#

function y = li(x, i)
	c = 1;
	xi = i * pi/2;
	p = 1;
	for k = (-10:10)
		if (k != i)
			xk = k * pi/2;
			p = p * (x - xk);
			c = c * (xi - xk);
		end
	endfor
	y = p / c;
endfunction

function y = f(x)
	y = 0;
	for i = (-10:10)
		y = y + sin(i * pi/2) * li(x, i);
	endfor
endfunction

N = 100;
s = 10000;
fn = fopen("3001path.tex", "w");
fprintf(fn, "\\draw[color=red,line width=1.4pt]\n\t({\\xskala*%.4f},{\\yskala*%.4f})", -pi/2, 0);
for j = (-(N-1):N)/N
	x = j * pi/2;
	fprintf(fn, "\n\t--({\\xskala*%.4f},{\\yskala*%.4f})", x, s * (f(x)-sin(x)));
endfor
fprintf(fn, ";\n\n");
fclose(fn);

N = 20;
x = -10.5 * pi/2;

fn = fopen("3001graph.tex", "w");
fprintf(fn, "\\draw[color=red,line width=1.2pt]\n\t({\\xskala*%.4f},{\\yskala*%.4f})", x, f(x));
for i = (-10.5*N+1:10.5*N) / N
	xi = i * pi/2;
	fprintf(fn, "\n\t--({\\xskala*%.4f},{\\yskala*%.4f})", xi, f(xi));
endfor
fprintf(fn, ";\n");
fclose(fn);
