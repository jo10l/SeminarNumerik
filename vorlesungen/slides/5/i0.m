#
# i0.m -- 
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
global beta;
global betamax;
global forcebeta;
global gamma;
global Ithreshold;

gamma = 0.2;
beta = 0.29;
betamax = 0.8;
forcebeta = 0;
Ithreshold = 0.10;

function yprime = f(y, t)
	global beta;
	global gamma;
	S = y(1,1);
	I = y(2,1);
	yprime = [
		-beta * I * S;
		 beta * I * S - gamma * I
	];
endfunction

lsode_options("maximum step size", 0.1)

function retval = duration(b)
	global beta;
	global betamax;
	global gamma;
	global Ithreshold;
	global forcebeta;
	beta = b;
	x0 = [ 0.999999, 0.000001 ];
	# find the minimum time when I gives 
	t = (1:200);
	x = lsode(@f, x0, t);
	t0 = min(t(x(:,2) > Ithreshold));
	
	for i = (1:4)
		t = [0, t0];
		x = lsode(@f, x0, t);
		xprime = f([x(2,1);x(2,2)], t0);
		deltat = (x(2,2) - Ithreshold) / xprime(2,1);
		t0 = t0 - deltat;
	end
	S0 = x(2,1);
	I0 = Ithreshold;
	if (forcebeta > 0)
		retval = (S0 - gamma / betamax) / (gamma * I0);
	else
		retval = (S0 - gamma / beta) / (gamma * I0);
	end
end

betascale = 10;
tscale = 0.2;
betamin = 0.1
betatop = 0.99
N = 200;
deltab = (betatop - betamin) / N;

fn = fopen("i0.tex", "w");

for i = (10:20)
#	Ithreshold = 0.01 * i
	gamma = 0.025 * i
	notfirst = 0;
	fprintf(fn, "\\def\\i%s{\n", char(64 + i));
	fprintf(fn, "    \\draw[color=red,line width=1.5pt] \n");
	for b = betamin + (0:N)*deltab
		b
		try
			d = duration(b)
			if (notfirst > 0)
				fprintf(fn, "\n\t-- ");
			else
				notfirst = 1;
			end
			fprintf(fn, "(%.4f,%.4f)", betascale * b, tscale * d);
		catch
		end_try_catch
	end
	fprintf(fn, ";\n}\n");

end

gamma = 0.2
for i = (10:20)
	Ithreshold = 0.01 * i
	notfirst = 0;
	fprintf(fn, "\\def\\j%s{\n", char(64 + i));
	fprintf(fn, "    \\draw[color=blue,line width=1.5pt] \n");
	for b = betamin + (0:N)*deltab
		b
		try
			d = duration(b)
			if (notfirst > 0)
				fprintf(fn, "\n\t-- ");
			else
				notfirst = 1;
			end
			fprintf(fn, "(%.4f,%.4f)", betascale * b, tscale * d);
		catch
		end_try_catch
	end
	fprintf(fn, ";\n}\n");

end

fclose(fn);


