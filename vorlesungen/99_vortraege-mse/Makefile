#
# Makefile -- vortraege-mse
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	vortraege-mse-handout.pdf Seminar-99-vortraege-mse.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-99-vortraege-mse.pdf:	Seminar-99-vortraege-mse.tex $(SOURCES)
	pdflatex Seminar-99-vortraege-mse.tex

vortraege-mse-handout.pdf:	vortraege-mse-handout.tex $(SOURCES)
	pdflatex vortraege-mse-handout.tex

thumbnail:	thumbnail.jpg

thumbnail.pdf:	Seminar-99-vortraege-mse.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-99-vortraege-mse.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

