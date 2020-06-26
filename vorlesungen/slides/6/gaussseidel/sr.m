#
# sr.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
n = 100;

global	polar = 0;

function writel(fn, lambda, name)
	global polar;
	fprintf(fn, "\\def\\%s{\n", name);
	spectralradius = max(abs(lambda));
	fprintf(fn, "\\spektralradius{%.4f}\n", spectralradius);
	if (polar == 0)
		fprintf(fn, "\\rectangulargrid\n");
#		fprintf(fn, "\\foreach \\y in {-3,-2.7,...,3.1}{\n");
#		fprintf(fn, "\\draw[color=darkgreen,line width=0.5pt] (-3.1,\\y)--(3.1,\\y);\n");
#		fprintf(fn, "\\draw[color=orange,line width=0.5pt] (\\y,-3.1)--(\\y,3.1);\n");
#		fprintf(fn, "}\n");
	else
		fprintf(fn, "\\polargrid\n");
#		fprintf(fn, "\\foreach \\r in {-3,-2.7,...,3.1}{\n");
#		fprintf(fn, "\\draw[color=orange,line width=0.5pt] (-3,0) circle[radius={3*exp(\\r/3)*exp(-1)}];\n");
#		fprintf(fn, "\\draw[color=darkgreen,line width=0.5pt] ({-3+3.1*exp(-2)*cos(60*\\r/3.14159)},{3.1*exp(-2)*sin(60*\\r/3.14159)}) -- ({-3+3.1*cos(60*\\r/3.14159)},{3.1*sin(60*\\r/3.14159)});\n");
#		fprintf(fn, "}\n");
	end
	n = size(lambda);
	for i = (1:n)
		fprintf(fn, "\\punkt{%.4f}{%.4f}\n", real(lambda(i)), imag(lambda(i)));
	end
	fprintf(fn, "}\n");
end

fn = fopen("lambda.tex", "w");


#A = rand(n,n) - n * eye(n);
A = rand(n, n);
A = A / max(abs(eig(A)));
eig(A)

phi = 2 * pi * rand(n/2, 1);
r = sqrt(rand(n/2, 1));
lambda = zeros(n, 1);
lambda((1:n/2),1) = r .* cos(phi) + i * r .* sin(phi)
lambda(n/2 + (1:n/2),1) = r .* cos(phi) - i * r .* sin(phi)

T = rand(n, n);
A = T * diag(lambda) * inverse(T);

writel(fn, lambda, "matrixA");

polar = 1;

#D = diag(diag(A))
#L = tril(A, -1)
#R = triu(A, 1)
#C = inverse(D+L)*R;

tau = 2;
C = (1/tau)*A - eye(n);

C = exp(-1) * expm(A) - eye(n);

lambda = eig(C);

writel(fn, lambda, "richardson");

fclose(fn);
