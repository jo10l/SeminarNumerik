/*
 * horner.cpp
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cstdlib>
#include <iostream>
#include <ios>
#include <iomanip>

template<typename T>
class polynomial {
	int	_degree;
	T	*_array;
public:
	polynomial(int degree) : _degree(degree) {
		_array = new T[degree + 1];
		for (int i = 0; i <= _degree; i++) {
			_array[i] = 0;
		}
		_array[0] = 1;
	}
	~polynomial() {
		delete _array;
	}
	T&	operator[](int i) {
		return _array[i];
	}
	std::pair<T, T>	f(T x) {
		T	fvalue;
		T	p[_degree+2];
		p[0] = 0;
		for (int i = 0; i <= _degree; i++) {
			p[i+1] = _array[i] + x * p[i];
		}
		for (int i = 0; i <= _degree; i++) {
			std::cout << p[i] << ",";
		}
		fvalue = p[_degree+1];;
		std::cout << "f=" << fvalue;
		T	q = 0;
		for (int i = 0; i <= _degree; i++) {
			q = p[i] + x * q;
		}
		std::cout << ",f'=" << q << std::endl;
		return std::make_pair(fvalue, q);
	}
	T	step(T x) {
		std::pair<T, T>	y = f(x);
		return x - (y.first / y.second);
	}
};

int	main(int argc, char *argv[]) {
	polynomial<float>	pol(3);
	pol[1] = 9;
	pol[2] = 9;
	pol[3] = 8;
	float	x = -10;
	for (int i = 0; i < 20; i++) {
		std::cout << i << "," << std::setprecision(10) << x << std::endl;
		x = pol.step(x);
	}
	return EXIT_SUCCESS;
}
