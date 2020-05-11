#
# 6003l.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#

L = [
	0,  0,  0;
	5,  0,  0;
	9,  1,  0
]
D = [
	3,  0,  0;
	0,  1,  0;
	0,  0,  2
]
R = [
	0,  0,  2;
	0,  0, -1;
	0,  0,  0
]

b = [ 11; 16; 31];

BJacobi = inverse(D) * (L + R);
b0 = inverse(D) * b;
BGaussSeidel = inverse(L + D) * R;
c0 = inverse(L+D) * b;

y0 = rand(3,1);
x0 = [ 3.0001; 2.0001; 1.0001 ];
x = x0
y = y0
fn = fopen("6003iteration.tex", "w");
fprintf(fn, "\\def\\tabelleninhalt{\n");
fprintf(fn, "   & %.4f & %.4f & %.4f & %.4f & %.4f & %.4f \\\\\n",
	y0(1,1), y0(2, 1), y0(3, 1), x0(1,1), x0(2, 1), x0(3, 1));
fprintf(fn, "\\hline\n");
for i = (1:30)
	x = b0 - BJacobi * x;
	y = c0 - BGaussSeidel * y;
	fprintf(fn, "%d & %.4f & %.4f & %.4f & %.4f & %.4f & %.4f \\\\\n",
		i, y(1,1), y(2, 1), y(3, 1), x(1,1), x(2, 1), x(3, 1));
end
fprintf(fn, "}\n");
fclose(fn);



