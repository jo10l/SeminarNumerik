/*
 * assoziativ.c -- finde Zahlen, für die das Assiziativgesetzt nicht gilt
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cstdio>
#include <cmath>
#include <typeinfo>
#include <iostream>
#include <ios>
#include <iomanip>

template<typename T>
void	nonassociative() {
	T	a = 1.;
	std::cout << "Typ: " << typeid(a).name() << std::endl;
	T	b = 1.;
	int	counter = 0;
	while (++counter < 500) {
		b = b / 2.;
		T	x = a + (b + b);
		T	y = (a + b) + b;
		if (x != y) {
			int	p = std::numeric_limits<T>::digits10 + 3;
			int	w = p + 6;
			std::cout << std::scientific;
			std::cout << "Unterschied:    ";
			std::cout << std::setw(w) << std::setprecision(p);
			std::cout << (x - y) << std::endl;
			std::cout << std::fixed;
			std::cout << "a           =   " << a << std::endl;
			std::cout << "b           =   " << b << std::endl;
			std::cout << "a + (b + b) =   " << x << std::endl;
			std::cout << "(a + b) + b =   " << y << std::endl;
			std::cout << "binary digits:  ";
			std::cout << std::numeric_limits<T>::digits;
			std::cout << std::endl;
			std::cout << "decimal digits: ";
			std::cout << std::numeric_limits<T>::digits10;
			std::cout << std::endl;
			std::cout << std::setw(w) << std::setprecision(p) << "epsilon     =   ";
			std::cout << std::scientific << std::numeric_limits<T>::epsilon();
			std::cout << std::endl;
		}
	}
	std::cout << std::endl;
}

int	main(int argc, char *argv[]) {
	nonassociative<float>();
	nonassociative<double>();
	nonassociative<long double>();
	return EXIT_SUCCESS;
}
