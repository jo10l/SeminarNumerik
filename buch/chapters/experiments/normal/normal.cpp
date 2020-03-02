/*
 * normal.cpp
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>

template<typename T>
class normal {
	T	_p;
public:
	normal(T p) : _p(p) { }
	T	Phi(T x) const {
		return 0.5 * (1 + erf(x / sqrt(2)));
	}
	T	f(T x) const {
		return Phi(x) - _p;
	}
	T	fprime(T x) const {
		return exp(-x*x/2) / sqrt(2*M_PI);
	}
};

template<typename T>
class newton : public normal<T> {
public:
	newton(T p) : normal<T>(p) { }
	T	iteration(T x) const {
		return x - normal<T>::f(x) / this->fprime(x);
	}
	T	find(T x0) const {
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

template<typename T>
class sekante : public normal<T> {
public:
	sekante(T p) : normal<T>(p) { }
	std::pair<T, T>	iteration(const std::pair<T, T>& x) const {
		T	a = x.first;
		T	b = x.second;
		T	fa = this->f(a);
		T	fb = this->f(b);
		T	xneu = (a*fb - b*fa)/(fb-fa);
		return std::make_pair(x.second, xneu);
	}
	T	find() const {
		std::pair<long double, long double>	x
			= std::make_pair((long double)0, (long double)1);
		int	k = 0;
		do {
			printf("%d & %24.20Lf & %24.20Lf \\\\\n",
				k, x.first, x.second);
			x = iteration(x);
		} while (++k <= 40);
		return x.second;
	}
};

int	main(int argc, char *argv[]) {
	long double	p = 0.95;
	normal<long double>	norm(p);
	std::cout << norm.Phi(1.664);
	std::cout << 0.5*(1+erf(-10*sqrt(2))) << std::endl;


	newton<long double>	n(p);
	long double	x = n.find(0);

	sekante<long double>	s(p);
	x = s.find();

	return EXIT_SUCCESS;
}
