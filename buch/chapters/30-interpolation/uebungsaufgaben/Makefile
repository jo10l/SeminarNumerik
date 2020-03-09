#
# Makefile
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	3001fehler.pdf 3001plot.pdf

3001fehler.pdf:	3001fehler.tex 3001path.tex
	pdflatex 3001fehler.tex

3001plot.pdf:	3001plot.tex 3001graph.tex
	pdflatex 3001plot.tex

3001path.tex 3001graph.tex:	3001.m
	octave 3001.m


