/*
 * sekante.cpp
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <ios>
#include <iomanip>
#include <limits>
#include <cmath>

int	w = 8;
bool	left = false;

template<typename T>
class intervallhalbierung {
	T	_a;
public:
	intervallhalbierung(T a) : _a(a) { }

	T	f(T x) const {
		long double	xx = x;
		return sinl(xx) - _a;	
	}

	std::pair<T, T>	operator()(const std::pair<T, T>& I) const {
		T	ma = f(I.second);
		T	mb = -f(I.first);
		T	m = (ma * I.first + mb * I.second) / (ma + mb);
		T	y = f(m);
		if (y < 0) {
			left = true;
			return std::make_pair(m, I.second);
		}
		left = false;
		return std::make_pair(I.first, m);
	}

	T	solve(T a, T b, T epsilon) const {
		int	k = 0;
		printf(" %2d & %*.*Lf & %*.*Lf & %*.*Lf\\\\\n", k++,
			w+2, w, (long double)a,
			w+2, w, (long double)b,
			w+2, w, (long double)(b - a));
		std::pair<T, T>	I = std::make_pair(a, b);
		int	counter = 0;
		do {
			I = (*this)(I);
			long double	a = I.first;
			long double	b = I.second;
			printf(" %2d & %s \\underline{}%*.*Lf & %s \\underline{}%*.*Lf & %*.*Lf\\\\\n", k++,
				(left) ? "\\color{red}" : "           ",
				w+2, w, a,
				(!left) ? "\\color{red}" : "           ",
				w+2, w, b,
				w+2, w, b - a);
		} while (((I.second - I.first) > epsilon) && (counter++ < 100));
		return I.first;
	}
};

int	main(int argc, char *argv[]) {

	std::cout << "float" << std::endl;

	{
		intervallhalbierung<float>	i(0.5);
		std::cout << std::setprecision(10);
		i.solve(0., 1.5, std::numeric_limits<float>::epsilon());
		std::cout << asinf(0.5) << std::endl;
	}

	std::cout << std::endl << "double" << std::endl;
	w = 17;
	
	{
		intervallhalbierung<double>	i(0.5);
		std::cout << std::setprecision(18);
		i.solve(0., 1.5, std::numeric_limits<double>::epsilon());
		std::cout << asin(0.5) << std::endl;
	}
	
	std::cout << std::endl << "long double" << std::endl;
	w = 20;
	
	{
		intervallhalbierung<long double>	i(0.5);
		std::cout << std::setprecision(22);
		i.solve(0., 1.5, std::numeric_limits<long double>::epsilon());
		std::cout << asinl(0.5) << std::endl;
	}
	
	return EXIT_SUCCESS;
}
