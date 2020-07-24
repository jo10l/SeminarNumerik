/*
 * cm.cpp
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapeprswil
 */
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <limits>
#include <iostream>
#include <iomanip>

const double	limit = 3;

template<typename T>
class computational_mode {
	int	n;
	int	i;
	T	h;
	T	state[2];
public:
	computational_mode(int _n);
	T	next();
	T	next(int n);
	T	x() const { return h * i; }
	void	draw(std::ostream& out, const std::string& name, int steps);
};

template<typename T>
void	computational_mode<T>::draw(std::ostream& out, const std::string& name,
		int steps) {
	out << "\\def\\" << name << "{" << std::endl;
	out << "({0*\\sx},{1*\\sy}) ";
	T	y = 0;
	do {
		y = next(steps);
		out << std::endl;
		out << std::setprecision(6) << std::fixed;
		out << "-- ({" << x() << "*\\sx},{" << abs(y) << "*\\sy})";
	} while (abs(y) < limit);
	out << std::endl;
	out << "}" << std::endl;
}

template<typename T>
computational_mode<T>::computational_mode(int _n) : n(_n) {
	h = 1 / (T)n;
	state[0] = 1 / (-h/2  + sqrt(1+h*h/4));
	state[1] = 1;
	i = 0;
}

template<typename T>
T	computational_mode<T>::next() {
	T	x = state[0] - 2 * h * state[1];
	state[0] = state[1];
	state[1] = x;
	i++;
	return x;
}

template<typename T>
T	computational_mode<T>::next(int n) {
	T	y;
	while (n-- > 0) {
		y = next();
	}
	return y;
}

int	main(int argc, char *argv[]) {
	{
		computational_mode<float>	cm(100);
		cm.draw(std::cout, "floathundred", 1);
	}
	{
		computational_mode<float>	cm(1000);
		cm.draw(std::cout, "floatthousand", 10);
	}
	{
		computational_mode<float>	cm(10000);
		cm.draw(std::cout, "floattenthousand", 100);
	}
	{
		computational_mode<float>	cm(100000);
		cm.draw(std::cout, "floathundredthousand", 1000);
	}

	{
		computational_mode<double>	cm(100);
		cm.draw(std::cout, "doublehundred", 1);
	}
	{
		computational_mode<double>	cm(1000);
		cm.draw(std::cout, "doublethousand", 10);
	}
	{
		computational_mode<double>	cm(10000);
		cm.draw(std::cout, "doubletenthousand", 100);
	}
	{
		computational_mode<double>	cm(100000);
		cm.draw(std::cout, "doublehundredthousand", 1000);
	}

	{
		computational_mode<long double>	cm(100);
		cm.draw(std::cout, "longdoublehundred", 1);
	}
	{
		computational_mode<long double>	cm(1000);
		cm.draw(std::cout, "longdoublethousand", 10);
	}
	{
		computational_mode<long double>	cm(10000);
		cm.draw(std::cout, "longdoubletenthousand", 100);
	}
	{
		computational_mode<long double>	cm(100000);
		cm.draw(std::cout, "longdoublehundredthousand", 1000);
	}

	return EXIT_SUCCESS;
}
