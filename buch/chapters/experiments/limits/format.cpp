/*
 * format.cpp
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <ios>
#include <iomanip>

template<typename T>
void	show(T x) {
	std::cout << std::setprecision(20) << std::setw(20) << std::fixed;
	std::cout << x << std::endl;
	std::cout << (5 * x) << std::endl;
}

int	main(int argc, char *argv[]) {
	show<float>(0.2);
	show<double>(0.2);
	show<long double>(0.2);
	show<float>(0.5);
	show<double>(0.5);
	show<long double>(0.5);
	return EXIT_SUCCESS;
}
