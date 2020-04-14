#
# Makefile -- sircapa
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	sircapa-handout.pdf Seminar-99-sircapa.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-99-sircapa.pdf:	Seminar-99-sircapa.tex $(SOURCES)
	pdflatex Seminar-99-sircapa.tex

sircapa-handout.pdf:	sircapa-handout.tex $(SOURCES)
	pdflatex sircapa-handout.tex

thumbnail:	thumbnail.jpg

thumbnail.pdf:	Seminar-99-sircapa.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-99-sircapa.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

