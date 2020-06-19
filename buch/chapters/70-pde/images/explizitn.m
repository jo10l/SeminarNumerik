#
# explizitn.m -- Neumann Randbedingungen
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
N = 18;

function retval = Atilde(c, N)
	A = eye(N);
	A = c*shift(A,-1) + (1-2*c)*A + c*shift(A,1);
	A = A(2:N-1,2:N-1);
	A(1,1) = 1-c;
	A(N-2,N-2) = 1-c;
	retval = A;
end

function spektralradius = sr(c, N)
	A = Atilde(c, N);
	e = eig(A);
	spektralradius = max(abs(e));
end

format long

fn = fopen("explizitn.inc", "w");

fprintf(fn, "\\draw[color=red,line width=1.4pt] (0,%.3f*\\sy)", sr(0,N));
for c = 0.01 * (1:200)
	fprintf(fn, "\n--({%.3f*\\sx},{%.3f*\\sy})", c, sr(c, N));
end
fprintf(fn, ";\n");
fclose(fn);

#
# Bewegung der Eigenwerte
#
fn = fopen("explizitneumann.inc", "w");
for c = 0.01 * (1:200)
	fprintf(fn, "%% c = %f \n", c);
	e = eig(Atilde(c, N));
	for i = (1:N-2)
		fprintf(fn, "\\fill[color=red] ({%.3f*\\sx},{%.3f*\\sy}) circle[radius=\\r];\n",
			e(i,1), c);
	end
end

fclose(fn);
