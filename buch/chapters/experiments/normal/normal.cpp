/*
 * normal.cpp
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cstdlib>
#include <cstdio>
#include <cmath>

template<typename T>
class normal {
	T	_p;
public:
	normal(T p) : _p(p) { }
	T	iteration(T x) {
		return x - (sqrt(M_PI)/(2*sqrt(2))) * exp(2 * x*x) * (0.5 + erfl(sqrt(2)*x) - _p);
	}
	T	newton(T x0) {
		int	k = 0;
		T	x = x0;
		do {
			long double	X = x;
			printf("%2d & %24.20Lf \\\\\n", k, X);
			x = iteration(x);
		} while (++k < 40);
		return x;
	}
};

int	main(int argc, char *argv[]) {

	normal<long double>	n(0.9);
	long double	x = n.newton(0);

	return EXIT_SUCCESS;
}
