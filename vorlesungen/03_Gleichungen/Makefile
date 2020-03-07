#
# Makefile -- Gleichungen
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	Gleichungen-handout.pdf Seminar-03-Gleichungen.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-03-Gleichungen.pdf:	Seminar-03-Gleichungen.tex $(SOURCES)
	pdflatex Seminar-03-Gleichungen.tex

Gleichungen-handout.pdf:	Gleichungen-handout.tex $(SOURCES)
	pdflatex Gleichungen-handout.tex

