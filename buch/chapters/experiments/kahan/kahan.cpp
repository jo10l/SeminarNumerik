/*
 * kahan.cpp -- Kahan Summation für die harmonische Reihe
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <iomanip>

template<typename T>
class harmonisch {
public:
	T	summe(int n) {
		T	s = 0;
		T	c = 0;
		for (int i = 1; i <= n; i++) {
			T	y = 1./i;
			y = y - c;
			T	t = s + y;
			c = (t - s) - y;
			s = t;
			//std::cout << s << ", " << c << std::endl;
		}
		return s;
	}

	T	reverse(int n) {
		T	s = 0;
		for (int i = n; i > 0; i--) {
			s += 1./i;
		}
		return s;
	}

	T	forward(int n) {
		T	s = 0;
		for (int i = 1; i <= n; i++) {
			s += 1./i;
		}
		return s;
	}
};

int	main(int argc, char *argv[]) {
	int	N = 100000000;

	harmonisch<float>	h;
	float	s = h.summe(N);
	float	r = h.reverse(N);
	float	f = h.forward(N);
	std::cout << std::endl;
	std::cout << "Kahan:   " << std::setw(20) << std::setprecision(15) << s;
	std::cout << std::endl;
	std::cout << "Reverse: " << std::setw(20) << std::setprecision(15) << r;
	std::cout << std::endl;
	std::cout << "Forward: " << std::setw(20) << std::setprecision(15) << f;
	std::cout << std::endl;

	harmonisch<long double>	hd;
	long double	S = hd.summe(N);
	long double	R = hd.reverse(N);
	long double	F = hd.forward(N);
	std::cout << std::endl;
	std::cout << "Kahan:   " << std::setw(26) << std::setprecision(20) << S;
	std::cout << std::endl;
	std::cout << "Reverse: " << std::setw(26) << std::setprecision(20) << R;
	std::cout << std::endl;
	std::cout << "Forward: " << std::setw(26) << std::setprecision(20) << F;
	std::cout << std::endl;

	return EXIT_SUCCESS;
}



