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

beta = 0.29;
betamax = 0.8;
forcebeta = 0;
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
	global gamma;
	global regime;
	global Ithreshold;
	global starttime;
	global endtime;
	global duration;
	global forcebeta
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
			if (beta0 > betamax)
				beta0 = betamax;
			end
		else
			if (beta0 > beta)
				beta0 = beta;
			end
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
fn = fopen("sirbetapath.tex", "w");
global xscale;
global yscale;
xscale = 12/N;
yscale = 5;

function retval = kurve(b, name)
	global regime;
	global xscale;
	global yscale;
	global fn;
	global beta;
	global gamma;
	global N;
	global starttime;
	global endtime;
	regime = 0;
	starttime = 0;
	endtime = 0;
	beta = 1.19 - b
	x0 = [ 0.999999; 0.000001; 0 ];
	t = (1:N);
	x = lsode(@f, x0, t);

	fprintf(fn, "\\def\\lockdown%s{\n", name);
	fprintf(fn, "\\fill[color=gray!30] (%.4f,0) rectangle (%.4f,%.4f);\n", xscale * starttime, xscale * endtime, yscale * 1);
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
	fprintf(fn, "\\node at (3,5.3) [above] {$\\beta = %.3f$};\n", beta);
	fprintf(fn, "\\node at (9,5.3) [above] {$\\gamma = %.2f$};\n", gamma);
	fprintf(fn, "}\n");

	retval = 0;
endfunction

kurve(0.20, "aa");
kurve(0.21, "ab");
kurve(0.22, "ac");
kurve(0.23, "ad");
kurve(0.24, "ae");
kurve(0.25, "af");
kurve(0.26, "ag");
kurve(0.27, "ah");
kurve(0.28, "ai");
kurve(0.29, "aj");

kurve(0.30, "ba");
kurve(0.31, "bb");
kurve(0.32, "bc");
kurve(0.33, "bd");
kurve(0.34, "be");
kurve(0.35, "bf");
kurve(0.36, "bg");
kurve(0.37, "bh");
kurve(0.38, "bi");
kurve(0.39, "bj");

kurve(0.40, "ca");
kurve(0.41, "cb");
kurve(0.42, "cc");
kurve(0.43, "cd");
kurve(0.44, "ce");
kurve(0.45, "cf");
kurve(0.46, "cg");
kurve(0.47, "ch");
kurve(0.48, "ci");
kurve(0.49, "cj");

kurve(0.50, "da");
kurve(0.51, "db");
kurve(0.52, "dc");
kurve(0.53, "dd");
kurve(0.54, "de");
kurve(0.55, "df");
kurve(0.56, "dg");
kurve(0.57, "dh");
kurve(0.58, "di");
kurve(0.59, "dj");

kurve(0.60, "ea");
kurve(0.61, "eb");
kurve(0.62, "ec");
kurve(0.63, "ed");
kurve(0.64, "ee");
kurve(0.65, "ef");
kurve(0.66, "eg");
kurve(0.67, "eh");
kurve(0.68, "ei");
kurve(0.69, "ej");

kurve(0.70, "fa");
kurve(0.71, "fb");
kurve(0.72, "fc");
kurve(0.73, "fd");
kurve(0.74, "fe");
kurve(0.75, "ff");
kurve(0.76, "fg");
kurve(0.77, "fh");
kurve(0.78, "fi");
kurve(0.79, "fj");

kurve(0.80, "ga");
kurve(0.81, "gb");
kurve(0.82, "gc");
kurve(0.83, "gd");
kurve(0.84, "ge");
kurve(0.841, "AA");
kurve(0.842, "AB");
kurve(0.843, "AC");
kurve(0.844, "AD");
kurve(0.845, "AE");
kurve(0.846, "AF");
kurve(0.847, "AG");
kurve(0.848, "AH");
kurve(0.849, "AI");
kurve(0.85, "gf");
kurve(0.86, "gg");
kurve(0.87, "gh");
kurve(0.88, "gi");
kurve(0.89, "gj");

kurve(0.90, "ha");
kurve(0.91, "hb");
kurve(0.92, "hc");
kurve(0.93, "hd");
kurve(0.94, "he");
kurve(0.95, "hf");
kurve(0.96, "hg");
kurve(0.97, "hh");
kurve(0.98, "hi");
kurve(0.99, "hj");

fclose(fn);




