/*
 * nullstellen.cpp
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
	int	_n;
public:
	intervallhalbierung(T a, int n) : _a(a), _n(n) { }

	T	f(T x) const {
		T	result = 1;
		T	p = x;
		int	k = _n;
		while (k) {
			if (k & 0x1) {
				result *= p;
			}
			p *= p;
			k >>= 1;
		}
		return result - _a;
	}

	std::pair<T, T>	operator()(const std::pair<T, T>& I) const {
		T	m = 0.5 * (I.first + I.second);
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
		} while ((I.second - I.first) > epsilon);
		return I.first;
	}
};

int	main(int argc, char *argv[]) {

	std::cout << "float" << std::endl;

	{
		intervallhalbierung<float>	i(10., 100);
		std::cout << std::setprecision(10);
		i.solve(0., 2., std::numeric_limits<float>::epsilon());
		std::cout << powf(10., 0.01) << std::endl;
	}

	std::cout << std::endl << "double" << std::endl;
	w = 17;
	
	{
		intervallhalbierung<double>	i(10., 100);
		std::cout << std::setprecision(18);
		i.solve(0., 2., std::numeric_limits<double>::epsilon());
		std::cout << powl(10., 0.01) << std::endl;
	}
	
	std::cout << std::endl << "long double" << std::endl;
	w = 20;
	
	{
		intervallhalbierung<long double>	i(10., 100);
		std::cout << std::setprecision(22);
		i.solve(0., 2., std::numeric_limits<long double>::epsilon());
		std::cout << powl(10., 0.01) << std::endl;
	}
	
	return EXIT_SUCCESS;
}
