#
# gs.m
#
# (c) 2020 Prof Dr Andreas Müller, Hohschule Rapperswil
#
R = [
	0, 1, 1, 1;
	0, 0, 1, 1;
	0, 0, 0, 1;
	0, 0, 0, 0
]
L = [
	0, 0, 0, 0;
	1, 0, 0, 0;
	1, 1, 0, 0;
	1, 1, 1, 0
]
D = diag([8, 6, 5, 7])

A = R + D + L
B = inverse(D+L)*R
[V, lambda] = eig(B)
spectralradius = max(abs(diag(lambda)))

b = [4;2;1;3]

x0 = inverse(A) * b

b0 = inverse(D+L) * b;

x = zeros(4,1);

fn = fopen("gs.tex", "w")

for l = (1:10)
	fprintf(fn, "\\only<%d>{\n", l+1);
	fprintf(fn, "Iteration $n=%d$:\n", l);
	fprintf(fn, "\\[\n");
	fprintf(fn, "\\begin{linsys}{6}\n");

	xneu = b0 - inverse(D+L) * R * x;

	for i = (1:4)
		fprintf(fn, "{\\color{red}%.6f}&=&", xneu(i, 1));
		fprintf(fn, "\\s\\displaystyle\\frac{1}{%d}\\cdot(%d", A(i,i), b(i,1));
		for k = (1:4)
			if (i == k)
				fprintf(fn, "& &             ");
			else
				if (k <= i)
					fprintf(fn, "&-&\\s %d\\cdot {\\color{red}%.6f} ", A(i, k), xneu(k, 1));
				else
					fprintf(fn, "&-&\\s %d\\cdot %.6f ", A(i, k), x(k, 1));
				end
			end
		end
		fprintf(fn, ")\\\\\n");
	end
	fprintf(fn, "\\end{linsys}\n");
	fprintf(fn, "\\]\n");
	fprintf(fn, "}\n");

	x = xneu;
end

fclose(fn);

A * x
