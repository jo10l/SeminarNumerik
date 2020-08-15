/*
 * kreisapprox.cpp -- Approximation eines Kreises mittels einer Bézier-Kurve
 *
 * (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
 */
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <iostream>
#include <fstream>
#include <getopt.h>

class point {
	double	_x;
	double	_y;
public:
	double	x() const { return _x; }
	double	y() const { return _y; }
	point() : _x(0), _y(0) { }
	point(double x, double y) : _x(x), _y(y) { }
	point	operator+(const point& other) const {
		return point(_x + other.x(), _y + other.y());
	}
	point	operator-(const point& other) const {
		return point(_x - other.x(), _y - other.y());
	}
	point	operator*(double t) const {
		return point(_x * t, _y * t);
	}
	double	abs() const { return hypot(_x, _y); }
	double	distance(const point& other) const {
		return hypot(_x - other.x(), _y - other.y());
	}
	point	emphasize(double s) const;
};

std::ostream&	operator<<(std::ostream& out, const point& p) {
	char	buffer[100];
	snprintf(buffer, sizeof(buffer), "({%.5f*#1},{%.5f*#2})", p.x(), p.y());
	return out << std::string(buffer);
}

point	operator*(double t, const point& p) {
	return p * t;
}

point	point::emphasize(double s) const {
	return (1 + s * (abs() - 1)) * (*this);
}

class bezier : public std::vector<point> {
	point	p(double t, int k, int l) const {
		if (k == 0) {
			return operator[](l);
		}
		point	r = ((1-t) * p(t, k-1, l)) + (t * p(t, k-1, l+1));
		return r;
	}
public:
	point	operator()(double t) {
		return p(t, size() - 1, 0);
	}
};

class kreisapprox : public bezier {
public:
	kreisapprox(double a) {
		push_back(point(1,0));
		push_back(point(1,a));
		push_back(point(a,1));
		push_back(point(0,1));
	}
};

class kreis {
public:
	point	operator()(double t) {
		double	phi = M_PI * t / 2;
		return point(cos(phi), sin(phi));
	}
};

static struct option	longopts[] = {
{ "a",		required_argument,	NULL,	'a' },
{ "points",	required_argument,	NULL,	'n' },
{ "scale",	required_argument,	NULL,	's' },
{ "prefix",	required_argument,	NULL,	'p' },
{ NULL,		0,			NULL,	 0  }
};

class	filename {
	std::string	_prefix;
public:
	const std::string&	prefix() const { return _prefix; }
	void	prefix(const std::string& p) { _prefix = p; }
	filename(const std::string& prefix) : _prefix(prefix) { }
	filename() { }
	std::string	operator()(const std::string& f) const {
		return _prefix + f + std::string(".tex");
	}
};

int	main(int argc, char *argv[]) {
	// parameters
	double	a = 4 * (sqrt(2)-1) / 3;
	int	N = 100;
	double	scale = 1000;
	filename	f;

	int	c;
	int	longindex;
	while (EOF != (c = getopt_long(argc, argv, "a:n:s:p:",
		longopts, &longindex)))
		switch (c) {
		case 'a':
			a = std::stod(optarg);
			break;
		case 'n':
			N = std::stoi(optarg);
			break;
		case 's':
			scale = std::stoi(optarg);
			break;
		case 'p':
			f.prefix(optarg);
			break;
		}

	kreisapprox	b(a);
	kreis	k;

	double	h = 1. / N;
	
	{
		std::ofstream	out(f("kurve"));
		out << "\\def\\kurvepfad#1#2{" << std::endl;
		out << "\\fill[color=red!20] " << point(0,1);
		out << "    arc (90:0:{#1}) -- " << point(1,0);
		for (int i = 1; i <= N; i++) {
			out << std::endl << "-- " << b(i * h).emphasize(0.5 * scale);
		}
		out << std::endl;
		out << "--cycle;" << std::endl;
		out << "\\draw[line width=1.4pt,color=red] " << b(0);
		for (int i = 1; i <= N; i++) {
			out << std::endl << "-- " << b(i * h).emphasize(0.5 * scale);
		}
		out << ";" << std::endl;
		out << "}" << std::endl;
	}
	{
		std::ofstream	out(f("fehler"));
		out << "\\def\\fehlerpfad#1#2{" << std::endl;
		out << "\\draw[line width=1.4pt,color=red] " << point();
		for (int i = 1; i <= N; i++) {
			double	t = i * h;
			out << std::endl << "-- ";
			out << point(t, scale * (b(t).abs() - 1));
		}
		out << ";" << std::endl;
		out << "}" << std::endl;
	}
	{
		std::ofstream	unterschied(f("unterschied"));
		std::ofstream	differenz(f("differenz"));
		unterschied << "\\def\\unterschiedpfad#1#2{" << std::endl;
		unterschied << "\\draw[line width=1.4pt,color=red] " << point();
		differenz << "\\def\\differenzpfad#1#2{" << std::endl;
		differenz << "\\draw[->,line width=1.4pt,color=red] " << point();
		for (int i = 0; i <= N; i++) {
			double	t = i * h;
			point	p = b(t) - k(t);
			unterschied << std::endl << "-- ";
			unterschied << point(t, scale * p.abs());
			differenz << std::endl << "-- " << scale * p;
		}
		unterschied << ";" << std::endl;
		differenz << ";" << std::endl;
		for (int i = 0 ; i <= N; i += (N / 10)) {
			double	t = i * h;
			point	p = b(t) - k(t);
			unterschied << "\\punkta{";
			unterschied << point(t, scale * p.abs());
			unterschied << "}{";
			unterschied << (i / (N / 10)) << "}";
			unterschied << std::endl;
			if ((i > 0) && (i < N)) {
				differenz << "\\punktb{";
				differenz << scale * p;
				differenz << "}{";
				differenz << (i / (N / 10)) << "}";
				differenz << std::endl;
			}
		}
		unterschied << "}" << std::endl;
		differenz << "}" << std::endl;
	}

	return EXIT_SUCCESS;
}
