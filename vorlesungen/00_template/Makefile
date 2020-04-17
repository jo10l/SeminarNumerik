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

thumbnail:	thumbnail.jpg

thumbnail.pdf:	Seminar-yyy-xxx.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-yyy-xxx.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

