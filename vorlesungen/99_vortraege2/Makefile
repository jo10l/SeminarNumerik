#
# Makefile -- vortraege2
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	vortraege2-handout.pdf Seminar-99-vortraege2.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-99-vortraege2.pdf:	Seminar-99-vortraege2.tex $(SOURCES)
	pdflatex Seminar-99-vortraege2.tex

vortraege2-handout.pdf:	vortraege2-handout.tex $(SOURCES)
	pdflatex vortraege2-handout.tex

thumbnail:	thumbnail.jpg

thumbnail.pdf:	Seminar-99-vortraege2.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-99-vortraege2.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

