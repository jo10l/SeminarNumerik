#
# Makefile -- dgl
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	dgl-handout.pdf Seminar-06-dgl.pdf

thumbnail:	thumbnail.jpg

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-06-dgl.pdf:	Seminar-06-dgl.tex $(SOURCES)
	pdflatex Seminar-06-dgl.tex

dgl-handout.pdf:	dgl-handout.tex $(SOURCES)
	pdflatex dgl-handout.tex

thumbnail.pdf:	Seminar-06-dgl.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-06-dgl.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

