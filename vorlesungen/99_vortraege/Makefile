#
# Makefile -- vortraege
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	vortraege-handout.pdf Seminar-99-vortraege.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-99-vortraege.pdf:	Seminar-99-vortraege.tex $(SOURCES)
	pdflatex Seminar-99-vortraege.tex

vortraege-handout.pdf:	vortraege-handout.tex $(SOURCES)
	pdflatex vortraege-handout.tex

thumbnail:	thumbnail.jpg

thumbnail.pdf:	Seminar-99-vortraege.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-99-vortraege.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

gauss.pdf:	Seminar-99-vortraege.pdf
	pdfjam --outfile gauss.pdf --papersize '{16cm,9cm}' \
		Seminar-99-vortraege.pdf 13
gauss.jpg:	gauss.pdf
	convert -density 300 gauss.pdf \
                -resize 1920x1080 -units PixelsPerInch gauss.jpg
