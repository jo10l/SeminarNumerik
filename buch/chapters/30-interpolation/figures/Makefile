#
# Makefile -- figures für Kapitel interpolation
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	h.pdf rolle.pdf nullstellen.pdf sin.pdf l.pdf norm.pdf

%.pdf:	%.tex
	pdflatex $<

normpaths.tex:	normal.m
	octave normal.m

norm.pdf:	norm.tex normpaths.tex
	pdflatex norm.tex
