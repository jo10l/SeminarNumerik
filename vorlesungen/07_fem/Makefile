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

thumbnail:	thumbnail.jpg

thumbnail.pdf:	Seminar-07-fem.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-07-fem.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

