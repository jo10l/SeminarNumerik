#
# Makefile -- vortraege3
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	vortraege3-handout.pdf Seminar-99-vortraege3.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-99-vortraege3.pdf:	Seminar-99-vortraege3.tex $(SOURCES)
	pdflatex Seminar-99-vortraege3.tex

vortraege3-handout.pdf:	vortraege3-handout.tex $(SOURCES)
	pdflatex vortraege3-handout.tex

thumbnail:	thumbnail.jpg

thumbnail.pdf:	Seminar-99-vortraege3.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-99-vortraege3.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

