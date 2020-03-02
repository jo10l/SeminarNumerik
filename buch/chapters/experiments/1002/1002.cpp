/*
 * 1002.cpp -- iteration to compute log(1+x_0)
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <iomanip>

template<typename T>
class iteration {
public:
	T	f(T x) {
		return sqrt(1 + x) - 1;
	}

	T	g(T x) {
		T	a = atan(sqrt(x));
		return sqrt(x) * tan(a / 2);
	}

	void	run(T x0, int N, int digits) {
		T	x = x0;
		T	y = x0;
		T	p = 1;
		for (int i = 0; i < N; i++) {
			long double	X = x;
			long double	Y = y;
			printf("%2d & %*.*Lf & %*.*Lf \\\\\n", i,
				digits + 4, digits, p * X,
				digits + 4, digits, p * Y);
			x = f(x);
			y = g(y);
			p *= 2;
		}
		printf("\\infty & %*.*f & %*.*f \\\\\n",
			digits + 4, digits, (double)log(1 + x0),
			digits + 4, digits, (double)log(1 + x0));
	}
};

int	main(int argc, char *argv[]) {

	iteration<double>	i;
	i.run(0.5, 50, 10);

	return EXIT_SUCCESS;
}
