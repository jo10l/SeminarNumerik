#
# Makefile
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	3001fehler.pdf 3001plot.pdf 3003kreis.pdf 3003fehler.pdf \
	abweichungen.pdf radiusfehler.pdf kreisapprox

3001fehler.pdf:	3001fehler.tex 3001path.tex
	pdflatex 3001fehler.tex

3001plot.pdf:	3001plot.tex 3001graph.tex
	pdflatex 3001plot.tex

3001path.tex 3001graph.tex:	3001.m
	octave 3001.m

3003kreis.pdf:	3003kreis.tex
	pdflatex 3003kreis.tex

3003fehler.pdf:	3003fehler.tex
	pdflatex 3003fehler.tex

kreisapprox:	kreisapprox.cpp
	g++ -o kreisapprox -Wall -g -O2 kreisapprox.cpp

FEHLER = fehler.tex unterschied.tex differenz.tex

$(FEHLER):	kreisapprox
	./kreisapprox --points=200

radiusfehler.pdf:	radiusfehler.tex $(FEHLER)
	pdflatex radiusfehler.tex

abweichungen.pdf:	abweichungen.tex $(FEHLER)
	pdflatex abweichungen.tex

