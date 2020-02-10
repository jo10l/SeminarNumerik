/*
 * sqrt.cpp
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <ios>
#include <iomanip>
#include <limits>

const int	N = 2;

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

template<typename T>
std::string	float2binary(T x) {
	char *xp = (char *)&x;
	std::string	s;
	int	bytes = sizeof(T);
	for (int i = bytes; i >= 0; i--) {
		s.append(char2binary(xp[i]));
	}
	return s;
}


template<typename T, typename S>
void	show() {
	T	x0 = sqrtl(2);
	T	x = x0;
	S	s = *(S*)(&x);
	s -= N;
	x = *(T*)(&s);
	T	startwerte[11];
	printf("  ");
	for (int i = 0; i <= 2*N; i++) {
		startwerte[i] = *(T*)(&s);
		std::string	e = float2binary(startwerte[i]);
		e = e.substr(e.size() - 5);
		printf("& \\texttt{%s} ", e.c_str());
		s++;
	}
	printf("\\\\\n  ");
	for (int i =  0; i <= 2*N; i++) {
		printf("& %10.6f ", startwerte[i]);
	}
	printf("\\\\\n  ");
	for (int i =  0; i <= 2*N; i++) {
		printf("& %10.6g ", startwerte[i] - x0);
	}
	printf("\\\\\n");
	T	folge[11];
	for (int i = 0; i <= 2*N; i++) { folge[i] = startwerte[i]; }
	int	counter = 0;
	while (++counter <= 20) {
		printf("%2d", counter);
		for (int i = 0; i <= 2*N; i++) {
			T	y = folge[i];
			y = y * y * y / 2.;
			folge[i] = y;
			if ((0.1 <= y) && (y < 100)) {
				printf("& %10.6f ", y);
			} else if (y < 0.1) {
				if (0 == y) {
					printf("&  0.000000  ");
				} else {
					printf("&%12.6e", y);
				}
			} else {
				if (y == std::numeric_limits<T>::infinity()) {
					printf("&  \\infty    ");
				} else {
					printf("&%12.6e", y);
				}
			}
		}
		printf("\\\\\n");
	}
}


int	main(int argc, char *argv[]) {
	show<float,int>();
	return EXIT_SUCCESS;
}
