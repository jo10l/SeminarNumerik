#
# Makefile -- dgl
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	dgl-handout.pdf Seminar-06-dgl.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-06-dgl.pdf:	Seminar-06-dgl.tex $(SOURCES)
	pdflatex Seminar-06-dgl.tex

dgl-handout.pdf:	dgl-handout.tex $(SOURCES)
	pdflatex dgl-handout.tex

