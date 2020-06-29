/*
 * testgmp.c -- GMP Beispiel
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <gmp.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double	gmpexp(double x) {
	mpf_t	X, P, S;
	mpf_init(X);
	mpf_init(P);
	mpf_init(S);

	mpf_set_d(X, x);
	mpf_set_d(P, 1.);
	mpf_set_d(S, 1.);

	mpf_t	R, Q;
	mpf_init(R);
	mpf_init(Q);

	for (int i = 1; i < 1000; i++) {
		mpf_mul(Q, P, X);
		mpf_div_ui(R, Q, i);
		mpf_set(P, R);
		mpf_add(Q, S, R);
		mpf_set(S, Q);
	}
	
	double	result = mpf_get_d(S);

	mpf_clear(X);
	mpf_clear(P);
	mpf_clear(S);
	mpf_clear(R);
	mpf_clear(Q);

	return result;
}

void	experiment(int bits) {
	mpf_set_default_prec(bits);
	double	x = -100;
	double	y = gmpexp(x);
	double	z = exp(x);

	printf("bits:         %d\n", bits);
	printf("GMP:          %.20g\n", y);
	printf("Prozessor:    %.20g\n", z);
	printf("Fehler:       %.20g\n\n", y - z);
}

int	main(int argc, char *argv[]) {
	int	bits = 32;
	while (bits <= 512) {
		experiment(bits);
		bits <<= 1;
	}
	
	return EXIT_SUCCESS;
}

