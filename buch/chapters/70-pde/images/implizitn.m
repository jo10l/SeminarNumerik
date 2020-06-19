#
# implizitn.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
N = 18;

function retval = Btilde(c, N)
	B = eye(N);
	B = -c * shift(B,-1) + (1+2*c) * B -c * shift(B,1);
	B = B(2:N-1,2:N-1);
	B(1,1) = 1+c;
	B(N-2,N-2) = 1+c;
	retval = B;
end

function spektralradius = sr(c, N)
	B = inverse(Btilde(c, N));
	e = eig(B);
	spektralradius = max(abs(e));
end

fn = fopen("implizitneumann.inc", "w");

for c = 0.01 * (1:200)
	fprintf(fn, "%% c = %f \n", c);
	e = eig(inverse(Btilde(c, N)));
	for i = (1:N-2)
		fprintf(fn, "\\fill[color=red] ({%.3f*\\sx},{%.3f*\\sy}) circle[radius=\\r];\n",
			e(i,1), c);
	end
end

fclose(fn);
