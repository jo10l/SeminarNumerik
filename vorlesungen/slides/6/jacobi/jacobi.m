#
# jacobi.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
N = 6;
B = rand(N,N);
[Q, R, P] = qr(B);
d = -1 + 2 * rand(1,N);
d = d + sign(d);
A = diag(d);
for k = (1:1)
	A = Q' * A * Q;
end
A

function retval = drehmatrix(A)
	theta = (A(2,2) - A(1,1)) / (2 * A(1,2));
	ta = theta + sqrt(theta^2 + 1);
	c = 1/sqrt(1+ta^2);
	s = ta*c;
	retval = [c, -s; s, c];
end

function retval = einzelschritt(A, i, j)
	d = drehmatrix([A(i,i),A(i,j);A(j,i), A(j,j)]);
	D = eye(size(A));
	D(i,i) = d(1,1);
	D(i,j) = d(1,2);
	D(j,i) = d(2,1);
	D(j,j) = d(2,2);
	retval = D' * A * D;
end

function showmatrix(fn, A, i, j, counter)
	n = size(A);
	fprintf(fn, "\\only<%d>{\n", counter);
	if (i > 0)
		fprintf(fn, "\\fill[color=gray!20] (%.2f,%.2f) rectangle (%.2f,%.2f);\n", i-0.5, -j-0.5, i+0.5, -j+0.5);
		fprintf(fn, "\\fill[color=gray!20] (%.2f,%.2f) rectangle (%.2f,%.2f);\n", j-0.5, -i-0.5, j+0.5, -i+0.5);
	end
	fprintf(fn, "\\gitter\n");
	for i = (1:n)
		for j = (1:n)
			try 
				r = 0.1 * (log10(abs(A(i,j))) - 1) + 1;
				if (r < 0)
					r = 0;
				else
					A(i, j)
					r
				end
				fprintf(fn, "\\fill[color=red!40] (%d,%d) circle[radius=%.4f];\n", i, -j, r/2);
			catch
			end_try_catch
		end
	end
	fprintf(fn, "}\n");
end

fn = fopen("jm.tex", "w");

counter=1
fprintf(fn, "\\only<%d>{\\node at (0.5,-0.15) [right] {Ausgangsmatrix:};}\n", counter);
showmatrix(fn, A, -1, -1, counter);
counter++;

for k = (1:12)
	fprintf(fn, "\\only<%d-%d>{\\node at (0.5,-0.15) [right] {Durchgang %d:};}\n", counter, counter + N * (N - 1)/2 - 1, k);
	for i = (2:N)
		for j = (1:i-1)
			A = einzelschritt(A, i, j);
			showmatrix(fn, A, i, j, counter);
			counter++;
		end
	end
end

A

fclose(fn);
