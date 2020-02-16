#
# Makefile -- Intro
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	Intro-handout.pdf Seminar-01-Intro.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-01-Intro.pdf:	Seminar-01-Intro.tex $(SOURCES)
	pdflatex Seminar-01-Intro.tex

Intro-handout.pdf:	Intro-handout.tex $(SOURCES)
	pdflatex Intro-handout.tex

