#
# Makefile -- pde
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	pde-handout.pdf Seminar-08-pde.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-08-pde.pdf:	Seminar-08-pde.tex $(SOURCES)
	pdflatex Seminar-08-pde.tex

pde-handout.pdf:	pde-handout.tex $(SOURCES)
	pdflatex pde-handout.tex

thumbnail:	thumbnail.jpg

thumbnail.pdf:	Seminar-08-pde.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-08-pde.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

courant:	courant.jpg

courant.pdf:	Seminar-08-pde.pdf
	pdfjam --outfile courant.pdf --papersize '{16cm,9cm}' \
		Seminar-08-pde.pdf 41
courant.jpg:	courant.pdf
	convert -density 300 courant.pdf \
                -resize 1920x1080 -units PixelsPerInch courant.jpg

explizit:	explizit.jpg

explizit.pdf:	Seminar-08-pde.pdf
	pdfjam --outfile explizit.pdf --papersize '{16cm,9cm}' \
		Seminar-08-pde.pdf 28
explizit.jpg:	explizit.pdf
	convert -density 300 explizit.pdf \
                -resize 1920x1080 -units PixelsPerInch explizit.jpg

