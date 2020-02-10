/*
 * ausloeschung.cpp
 *
 * (c) 2020 Prof Dr Andreas Müllerm Hochschule Rapperswil
 */
#include <cstdlib>
#include <iostream>
#include <ios>
#include <iomanip>
#include <cmath>

std::string	char2binary(char x) {
	std::string	s;
	unsigned char	m = 0x80;
	char	c[2];
	c[1] = '\0';
	while (m) {
		c[0] = (m & x) ? '1' : '0';
		s.append(c);
		m >>= 1;
	}
	return s;
}

std::string	float2binary(float x) {
	char *xp = (char *)&x;
	std::string	s;
	for (int i = 3; i >= 0; i--) {
		s.append(char2binary(xp[i]));
	}
	return s;
}

int	main(int argc, char *argv[]) {

	float	a = M_PI;
	float	b = sqrt(10);
	float	d = b - a;

	std::cout << std::scientific << std::setprecision(30);
	std::cout << "a=" << a << std::endl;
	std::cout << "b=" << b << std::endl;
	std::cout << "d=" << d << std::endl;

	std::cout << "a=" << float2binary(a) << std::endl;
	std::cout << "b=" << float2binary(b) << std::endl;
	std::cout << "d=" << float2binary(d) << std::endl;

	return EXIT_SUCCESS;
}
