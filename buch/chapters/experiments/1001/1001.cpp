/*
 * 1001.cpp
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswi
 */
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <limits>
#include <iostream>

template<typename T>
class grenzwert {
public:
	T	f(T x) {
		return (1 - cos(x)) / x;
	}

	T	g(T x) {
		return 2 * sin(x/2) * sin(x/2) / x;
	}

	T	limit(T x, int digits) {
		std::cout << std::numeric_limits<T>::epsilon() << std::endl;
		std::cout << sqrt(2*std::numeric_limits<T>::epsilon())
			<< std::endl;
		std::cout << f(1e-10) << std::endl;
		T	l;
		int	counter = 0;
		while ((x > 0) && (++counter < 30)) {
			l = f(x);
			long double	X = x;
			long double	L = l;
			long double	LL = 2 * sin(x/2) * sin(x/2) / x;
			printf("%d & %*.*Lf & %*.*Lf & %*.*Lf\\\\\n", counter,
				digits + 4, digits, X,
				digits + 4, digits, L,
				digits + 4, digits, LL);
			x = x / 2;
		}
		return l;
	}

	void	plot(T xmax, int npoints, float s) {
		FILE	*file = fopen("path.tex", "w");

		fprintf(file, "\\def\\pfad{\n");
		fprintf(file, "\\draw[color=red,line width=1.4pt]\n");
		fprintf(file, "\t(0,0)");
		for (int i = 1; i <= npoints; i++) {
			T	x = i * xmax / npoints;
			double	y = f(x);
			fprintf(file, "\n\t--(%.4f,%.4f)", s * x, s * y);
		}
		fprintf(file, ";\n}\n");

		fprintf(file, "\\def\\korrekt{\n");
		fprintf(file, "\\draw[color=blue,line width=1.4pt]\n");
		fprintf(file, "\t(0,0)");
		for (int i = 1; i <= npoints; i++) {
			T	x = i * xmax / npoints;
			double	y = g(x);
			fprintf(file, "\n\t--(%.4f,%.4f)", s * x, s * y);
		}
		fprintf(file, ";\n}\n");

		fclose(file);
	}
	
};

int	main(int argc, char *argv[]) {

	{
		grenzwert<float>	g;
		g.limit(1,10);
		g.plot(0.001, 500, (float)12000);
	}
	{
		grenzwert<double>	g;
		g.limit(1,16);
	}
	{
		grenzwert<long double>	g;
		g.limit(1,20);
	}

	return EXIT_SUCCESS;
}
