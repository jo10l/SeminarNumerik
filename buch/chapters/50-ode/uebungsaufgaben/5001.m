#
# 5001.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
N = 20
for k = (1:N)
	h = 2^(-k);
	q = (2+h)/(2-h);
	printf("%2d & \\underline{ %20.16f\\\\\n", k, q^(2^k))
end
