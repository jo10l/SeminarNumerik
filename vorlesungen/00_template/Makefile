#
# Makefile -- xxx
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	xxx-handout.pdf Seminar-yyy-xxx.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-yyy-xxx.pdf:	Seminar-yyy-xxx.tex $(SOURCES)
	pdflatex Seminar-yyy-xxx.tex

xxx-handout.pdf:	xxx-handout.tex $(SOURCES)
	pdflatex xxx-handout.tex

