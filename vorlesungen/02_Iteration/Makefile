#
# Makefile -- Iteration
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	Iteration-handout.pdf Seminar-02-Iteration.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-02-Iteration.pdf:	Seminar-02-Iteration.tex $(SOURCES)
	pdflatex Seminar-02-Iteration.tex

Iteration-handout.pdf:	Iteration-handout.tex $(SOURCES)
	pdflatex Iteration-handout.tex

