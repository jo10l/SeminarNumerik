/*
 * testmpfr.c
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <mpfr.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double	mpfrexp(double x) {
	mpfr_t	X, P, S;
	mpfr_init(X);
	mpfr_init(P);
	mpfr_init(S);

	mpfr_set_d(X, x, MPFR_RNDN);
	mpfr_set_d(P, 1., MPFR_RNDN);
	mpfr_set_d(S, 1., MPFR_RNDN);

	mpfr_t	R, Q;
	mpfr_init(R);
	mpfr_init(Q);

	for (int i = 1; i < 1000; i++) {
		mpfr_mul(Q, P, X, MPFR_RNDN);
		mpfr_div_ui(R, Q, i, MPFR_RNDN);
		mpfr_set(P, R, MPFR_RNDN);
		mpfr_add(Q, S, R, MPFR_RNDN);
		mpfr_set(S, Q, MPFR_RNDN);
	}
	
	double	result = mpfr_get_d(S, MPFR_RNDN);

	mpfr_clear(X);
	mpfr_clear(P);
	mpfr_clear(S);
	mpfr_clear(R);
	mpfr_clear(Q);

	return result;
}

void	experiment(int bits) {
	mpfr_set_default_prec(bits);
	double	x = -100;
	double	y = mpfrexp(x);
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

