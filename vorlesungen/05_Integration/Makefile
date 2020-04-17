#
# Makefile -- Integration
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	Integration-handout.pdf Seminar-05-Integration.pdf

thumbnail:	thumbnail.jpg

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

Seminar-05-Integration.pdf:	Seminar-05-Integration.tex $(SOURCES)
	pdflatex Seminar-05-Integration.tex

Integration-handout.pdf:	Integration-handout.tex $(SOURCES)
	pdflatex Integration-handout.tex

thumbnail.pdf:	Seminar-05-Integration.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		Seminar-05-Integration.pdf
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

