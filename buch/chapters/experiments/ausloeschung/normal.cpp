/*
 * normal.cpp
 *
 * (c) 2020 Prof Dr Andreas Mueller, Hochschule Rapperswil
 */
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <ios>
#include <iomanip>

template<typename T>
void	normalexperiment(double a, double b) {
	T	p2 = erfl(sqrtl(2) * b);
	T	p1 = erfl(sqrtl(2) * a);
	T	p = p2 - p1;
	std::cout << std::fixed << std::setprecision(2);
	std::cout << "P(" << a << " <= X <= " << b << ") = ";
	std::cout << std::setprecision(6) << std::scientific;
	std::cout << p << std::endl;
	std::cout << std::endl;
}

template<typename T>
void	normalexperimentc(double a, double b) {
	T	p2 = erfcl(sqrtl(2) * b);
	T	p1 = erfcl(sqrtl(2) * a);
	T	p = p1 - p2;
	std::cout << std::fixed << std::setprecision(2);
	std::cout << "P(" << a << " <= X <= " << b << ") = ";
	std::cout << std::setprecision(15) << std::scientific;
	std::cout << p << std::endl;
	std::cout << std::endl;
}

int	main(int argc, char *argv[]) {
	double	a = 4.18;
	double	b = a + 1;
	normalexperiment<float>(a, b);
	normalexperiment<double>(a, b);
	normalexperiment<long double>(a, b);

	normalexperimentc<float>(a, b);
	normalexperimentc<double>(a, b);
	normalexperimentc<long double>(a, b);

	return EXIT_SUCCESS;
}
