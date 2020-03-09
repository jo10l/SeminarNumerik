#
# Makefile -- figures für Kapitel interpolation
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	h.pdf rolle.pdf nullstellen.pdf sin.pdf l.pdf norm.pdf tscheb.pdf \
	basis.pdf tschebasis.pdf polygon.pdf vergleich.pdf

%.pdf:	%.tex
	pdflatex $<

normpaths.tex:	normal.m
	octave normal.m

norm.pdf:	norm.tex normpaths.tex
	pdflatex norm.tex

tpaths.tex:	tschebyscheff.m
	octave tschebyscheff.m

tscheb.pdf:	tscheb.tex tpaths.tex
	pdflatex tscheb.tex

basis.pdf:	basis.tex basispaths.tex
	pdflatex basis.tex
basispaths.tex:	basis.m
	octave basis.m

tschebasis.pdf:	tschebasis.tex tschebasispaths.tex
	pdflatex tschebasis.tex
tschebasispaths.tex:	tschebasis.m
	octave tschebasis.m

polygon.pdf:	polygon.tex
	pdflatex polygon.tex

vergleich.pdf:	vergleich.tex
	pdflatex vergleich.tex

