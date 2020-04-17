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

videos:	i0video simvideo simbetavideo

i0video:	Seminar-99-sircapa.pdf
	pdfjam --outfile i0video.pdf --papersize '{16cm,9cm}' \
		Seminar-99-sircapa.pdf 187-205
	rm -rf i0video; mkdir i0video
	convert -density 600 -units PixelsPerInch i0video.pdf \
		-resize 1920x1080 -depth 8 -alpha off -density 72 \
		i0video/i%03d.png

simvideo:	Seminar-99-sircapa.pdf
	pdfjam --outfile simvideo.pdf --papersize '{16cm,9cm}' \
		Seminar-99-sircapa.pdf 5-84
	rm -rf simvideo; mkdir simvideo
	convert -density 600 -units PixelsPerInch simvideo.pdf \
		-resize 1920x1080 -depth 8 -alpha off -density 72 \
		simvideo/i%03d.png

simbetavideo:	Seminar-99-sircapa.pdf
	pdfjam --outfile simbetavideo.pdf --papersize '{16cm,9cm}' \
		Seminar-99-sircapa.pdf 93-181
	rm -rf simbetavideo; mkdir simbetavideo
	convert -density 600 -units PixelsPerInch simbetavideo.pdf \
		-resize 1920x1080 -depth 8 -alpha off -density 72 \
		simbetavideo/i%03d.png




