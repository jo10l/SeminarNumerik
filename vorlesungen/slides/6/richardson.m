#
# richardson.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
n = 10;

function r = spectralradius(A)
	r = max(abs(eig(A)));
end

A = rand(n, n) + 2 * rand(1,1) * eye(n)
m = 1000;
M = 0;
for t = (-100:0.1:100)
	try 
		B = t * eye(n);
		C = A - B;
		s = spectralradius((1/t)*C);
		if (s > M)
			M = s;
			tM = t;
		end
		if (s < m)
			m = s;
			tm = s;
		end
		#printf("%4.1f  %10.4f\n", t, s);
	catch
	end_try_catch
end

printf("minimum:  %10.4f @ %4.1f\n", m, tm);
printf("maximum:  %10.4f @ %4.1f\n", M, tM);
	

