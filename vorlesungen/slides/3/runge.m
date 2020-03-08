#
# runge.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#

function y = f(x)
	y = 1;
	for k = (-6:6)
		y = y * (x - k);
	end
endfunction

fn = fopen("rungepath.tex", "w");

s = 1e-7;

fprintf(fn, "\\draw[color=red,line width=1.4pt] (%.4f,%.4f)", -6, s * f(-6));
for x = (-599:600) * 0.01
	fprintf(fn, "\n\t--(%.4f,%.4f)", x, s*f(x));
end
fprintf(fn, ";\n");
fclose(fn);
