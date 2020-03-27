#
# Makefile -- fem
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	fem-handout.pdf Seminar-07-fem.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-07-fem.pdf:	Seminar-07-fem.tex $(SOURCES)
	pdflatex Seminar-07-fem.tex

fem-handout.pdf:	fem-handout.tex $(SOURCES)
	pdflatex fem-handout.tex

