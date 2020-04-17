#
# Makefile -- Interpolation
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	Interpolation-handout.pdf Seminar-04-Interpolation.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-04-Interpolation.pdf:	Seminar-04-Interpolation.tex $(SOURCES)
	pdflatex Seminar-04-Interpolation.tex

Interpolation-handout.pdf:	Interpolation-handout.tex $(SOURCES)
	pdflatex Interpolation-handout.tex

