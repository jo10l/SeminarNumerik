#
# Makefile -- linalg
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	linalg-handout.pdf Seminar-09-linalg.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-09-linalg.pdf:	Seminar-09-linalg.tex $(SOURCES)
	pdflatex Seminar-09-linalg.tex

linalg-handout.pdf:	linalg-handout.tex $(SOURCES)
	pdflatex linalg-handout.tex

thumbnail:	thumbnail.jpg

thumbnail.pdf:	Seminar-09-linalg.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-09-linalg.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

konvergenz.pdf:	Seminar-09-linalg.pdf
	pdfjam --outfile konvergenz.pdf --papersize '{16cm,9cm}' \
		Seminar-09-linalg.pdf 85
konvergenz.jpg:	konvergenz.pdf
	convert -density 300 konvergenz.pdf \
                -resize 1920x1080 -units PixelsPerInch konvergenz.jpg

