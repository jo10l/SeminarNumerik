#
# gs2.m
#
# (c) 2020 Prof Dr Andreas Müller, Hohschule Rapperswil
#
R = [
	0, 1, 0, 1;
	0, 0, 1, 0;
	0, 0, 0, 1;
	0, 0, 0, 0
]
L = [
	0, 0, 0, 0;
	1, 0, 0, 0;
	0, 1, 0, 0;
	1, 0, 1, 0
]
D = diag([1, 2, 2, 1])

A = R + D + L

B = inverse(D+L)*R
[V, lambda] = eig(B)
spectralradius = max(abs(diag(lambda)))

b = [4;2;1;3]
global d;
d = 2;
global w;
w = 6;

x0 = inverse(A) * b

b0 = inverse(D+L) * b;

x = [ 4; 2; 1; 3 ]


#
#A =
#
#   1   1   0   1
#   1   2   1   0
#   0   1   2   1
#   1   0   1   1
#
#spectralradius =  2.3315
#b =
#
#   4
#   2
#   1
#   3
#

function retval = f(x)
	global d;
	global w;
	y = abs(x);
	s = sprintf("%.*f", d, y);
	if (x < 0)
		if (length(s) < w)
			retval = sprintf("\\phantom{%0*d}\\hbox{$-%s$}", w - length(s), 0, s);
		else
			retval = sprintf("\\hbox{$-%s$}", s);
		end
	else
		if (length(s) < w)
			retval = sprintf("\\phantom{+%0*d}%s", w - length(s), 0, s);
		else
			retval = sprintf("\\phantom{+}%s", s);
		end
	end
end

fn = fopen("gs2.tex", "w")

for l = (1:7)
	fprintf(fn, "\\only<%d>{\n", l+1);
	fprintf(fn, "Iteration $n=%d$:\n", l);
	fprintf(fn, "\\[\n");
	fprintf(fn, "\\begin{linsys}{6}\n");

	xneu = b0 - inverse(D+L) * R * x;

	for i = (1:4)
		s = f(xneu(i, 1));
		fprintf(fn, "{\\color{red}%s}&=&", s);
		fprintf(fn, "\\s\\displaystyle\\frac{1}{%d}\\cdot\\bigl(%d", A(i,i), b(i,1));
		for k = (1:4)
			if (i == k)
				fprintf(fn, "& &             ");
			else
				if (k <= i)
					s = f(xneu(k, 1));
					fprintf(fn, "&-&\\s %d\\cdot({\\color{red}%s})", A(i, k), s);
				else
					s = f(x(k, 1));
					fprintf(fn, "&-&\\s %d\\cdot(%s)", A(i, k), s);
				end
			end
		end
		fprintf(fn, "\\bigr)\\\\\n");
	end
	fprintf(fn, "\\end{linsys}\n");
	fprintf(fn, "\\]\n");
	fprintf(fn, "}\n");

	x = xneu;
end

fclose(fn);

A * x
