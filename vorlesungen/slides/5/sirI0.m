#
# sir.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
global beta;
global betamax;
global forcebeta;
global gamma;
global N;
global Ithreshold;
global starttime;
global endtime;
global duration;

forcebeta = 0;
beta = 0.6;
betamax = 0.8;
gamma = 0.2;
N = 300;
Ithreshold = 0.10;
starttime = 0;
endtime = 0;

global regime;
regime = 0;

lsode_options("maximum step size", 0.05)

function yprime = f(y, t)
	global beta;
	global betamax;
	global forcebeta;
	global gamma;
	global regime;
	global Ithreshold;
	global starttime;
	global endtime;
	global duration;
	S = y(1,1);
	I = y(2,1);
	R = y(3,1);
	if (regime == 0)
		if (I > Ithreshold)
			starttime = t
			regime = 1;
		end
	end
	if (regime > 0)
		beta0 = gamma / abs(S);
		if (forcebeta > 0)
			if beta0 > betamax
				beta0 = betamax;
			end
		else
			if (beta0 > beta)
				beta0 = beta;
			end
		end
		if (beta0 > betamax)
			beta0 = betamax;
		end
		if (endtime == 0)
			if (I < 0.95 * Ithreshold)
				endtime = t
				duration = endtime - starttime;
			end
		end
	else
		beta0 = beta;
	end
	yprime = [
		-beta0 * S * I;
		+beta0 * S * I - gamma * I;
		                 gamma * I
	];
endfunction

global fn;
fn = fopen("sirI0path.tex", "w");
global xscale;
global yscale;
xscale = 12/N;
yscale = 5;

function retval = kurve(I0, name)
	global regime;
	global xscale;
	global yscale;
	global fn;
	global beta;
	global gamma;
	global N;
	global starttime;
	global endtime;
	global Ithreshold;
	Ithreshold = I0;
	regime = 0;
	starttime = 0;
	endtime = 0;
	x0 = [ 0.999999; 0.000001; 0 ];
	t = (1:N);
	x = lsode(@f, x0, t);

	fprintf(fn, "\\def\\lockdown%s{\n", name);
	fprintf(fn, "\\fill[color=gray!50] (%.4f,0) rectangle (%.4f,%.4f);\n", xscale * starttime, xscale * endtime, yscale * 1);
        fprintf(fn, "\\draw (%.4f,0)--(%.4f,0);\n", xscale * starttime, xscale * endtime);
        fprintf(fn, "\\draw[line width=0.5pt] (%.4f,%.4f)--(%.4f,%.4f);\n", xscale * starttime, yscale, xscale * endtime, yscale);

	fprintf(fn, "}\n");

	fprintf(fn, "\\def\\S%s{\n", name);
	fprintf(fn, "\\draw[color=blue,line width=1.4pt,line join=round] (%.4f,%.4f)", 0, yscale * x0(1,1));
	for i = 1:N
		fprintf(fn, "\n\t--(%.4f,%.4f)", xscale * t(1,i), yscale * x(i, 1));
	endfor
	fprintf(fn, ";\n}\n");

	fprintf(fn, "\\def\\I%s{\n", name);
	fprintf(fn, "\\draw[color=red,line width=1.4pt,line join=round] (%.4f,%.4f)", 0, yscale * x0(2,1));
	for i = 1:N
		fprintf(fn, "\n\t--(%.4f,%.4f)", xscale * t(1,i), yscale * x(i, 2));
	endfor
	fprintf(fn, ";\n}\n");

	fprintf(fn, "\\def\\R%s{\n", name);
	fprintf(fn, "\\draw[color=darkgreen,line width=1.4pt,line join=round] (%.4f,%.4f)", 0, yscale * x0(3,1));
	for i = 1:N
		fprintf(fn, "\n\t--(%.4f,%.4f)", xscale * t(1,i), yscale * x(i, 3));
	endfor
	fprintf(fn, ";\n}\n");

	fprintf(fn, "\\def\\all%s{\n", name);
	fprintf(fn, "\\lockdown%s \\S%s \\R%s \\I%s\n", name, name, name, name);
	fprintf(fn, "\\draw[color=red,line width=0.5pt] (0,%.4f)--(12,%.4f);\n", yscale * Ithreshold, yscale * Ithreshold);
	fprintf(fn, "\\node[color=red] at (0,%.4f) [above right] {$I_0=%.3f$};\n", yscale * Ithreshold, Ithreshold);
	fprintf(fn, "\\node at (3,5.3) [above] {$\\beta = %.2f$};\n", beta);
	fprintf(fn, "\\node at (9,5.3) [above] {$\\gamma = %.2f$};\n", gamma);
	fprintf(fn, "}\n");

	retval = 0;
endfunction

kurve(0.01, "ab");
kurve(0.02, "ac");
kurve(0.03, "ad");
kurve(0.04, "ae");
kurve(0.05, "af");
kurve(0.06, "ag");
kurve(0.07, "ah");
kurve(0.08, "ai");
kurve(0.09, "aj");

kurve(0.10, "ba");
kurve(0.11, "bb");
kurve(0.12, "bc");
kurve(0.13, "bd");
kurve(0.14, "be");
kurve(0.15, "bf");
kurve(0.16, "bg");
kurve(0.17, "bh");
kurve(0.18, "bi");
kurve(0.19, "bj");

kurve(0.20, "ca");

fclose(fn);




