/*
 * limits.cpp -- Grenzen der Datentypen
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cstdlib>
#include <limits>
#include <iostream>
#include <ios>
#include <iomanip>

template<typename T>
void	show() {
	std::cout << "Typ:                " << typeid(T).name() << std::endl;
	std::cout << "IEEE-754:           ";
	std::cout << ((std::numeric_limits<T>::is_iec559) ? "yes" : "no");
	std::cout << std::endl;
	std::cout << "maximum:            ";
	std::cout << std::numeric_limits<T>::max();
	std::cout << std::endl;
	std::cout << "minimum:            ";
	std::cout << std::numeric_limits<T>::min();
	std::cout << std::endl;
	std::cout << "epsilon:            ";
	std::cout << std::numeric_limits<T>::epsilon();
	std::cout << std::endl;
	std::cout << "round_error:        ";
	std::cout << std::numeric_limits<T>::round_error();
	std::cout << std::endl;
	std::cout << "grösster Exponent:  ";
	std::cout << std::numeric_limits<T>::max_exponent << std::endl;
	std::cout << "kleinster Exponent: ";
	std::cout << std::numeric_limits<T>::min_exponent << std::endl;
	std::cout << "has_denorm:         ";
	std::cout << ((std::numeric_limits<T>::has_denorm) ? "yes" : "no");
	std::cout << std::endl;
	std::cout << "denorm_min:         ";
	std::cout << std::numeric_limits<T>::denorm_min() << std::endl;
	std::cout << std::endl;
}

int 	main(int argc, char *argv[]) {
	show<float>();
	show<double>();
	show<long double>();
	return EXIT_SUCCESS;
}
