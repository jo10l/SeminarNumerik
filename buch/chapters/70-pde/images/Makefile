#
# Makefile -- build images for pde chapter
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
images = derivatives.pdf diffex.pdf diff2.pdf laplace.pdf poisson.pdf \
	neumann.pdf kont.pdf 2dpart.pdf gebiet.pdf offen.pdf euler.pdf \
	rueckwaerts.pdf cngrid.pdf explizitd.pdf explizitspektrum.pdf \
	implizitspektrum.pdf cnspektrum.pdf \
	explizitneumann.pdf implizitneumann.pdf cnneumann.pdf \
	explizit.jpg implizit.jpg \
	ringgebiet.pdf

all:	$(images)

derivatives.pdf:	derivatives.tex
	pdflatex derivatives.tex

diffex.pdf:	diffex.tex
	pdflatex diffex.tex

diff2.pdf:	diff2.tex
	pdflatex diff2.tex

laplace.pdf:	laplace.tex
	pdflatex laplace.tex

poisson.pdf:	poisson.tex
	pdflatex poisson.tex

neumann.pdf:	neumann.tex
	pdflatex neumann.tex

kont.pdf:	kont.tex
	pdflatex kont.tex

2dpart.pdf:	2dpart.tex
	pdflatex 2dpart.tex

gebiet.pdf:	gebiet.tex
	pdflatex gebiet.tex

offen.pdf:	offen.tex
	pdflatex offen.tex

euler.pdf:	euler.tex
	pdflatex euler.tex

rueckwaerts.pdf:	rueckwaerts.tex
	pdflatex rueckwaerts.tex

cngrid.pdf:	cngrid.tex
	pdflatex cngrid.tex

explizit.inc:   explizit.m
	octave --silent explizit.m

explizit.png:   explizit.pov explizit.inc common.inc
	povray +A0.1 -W1920 -H1080 -Oexplizit.png explizit.pov

explizit.jpg:   explizit.png
	convert explizit.png -density 300 -units PixelsPerInch explizit.jpg

implizit.inc:	implizit.m
	octave --silent implizit.m

implizit.png:	implizit.pov implizit.inc common.inc
	povray +A0.1 -W1920 -H1080 -Oimplizit.png implizit.pov

implizit.jpg:	implizit.png
	convert implizit.png -density 300 -units PixelsPerInch implizit.jpg

cranknicholson.inc:     cranknicholson.m
	octave --silent cranknicholson.m

cranknicholson.png:     cranknicholson.pov cranknicholson.inc common.inc
	povray +A0.1 -W1920 -H1080 -Ocranknicholson.png cranknicholson.pov

cranknicholson.jpg:     cranknicholson.png
	convert cranknicholson.png -density 300 -units PixelsPerInch cranknicholson.jpg


combined.png:   combined.pov common.inc explizit.inc implizit.inc cranknicholson.inc
	povray +A0.1 -W1920 -H1080 -Ocombined.png combined.pov

combined.jpg:   combined.png
	convert combined.png -density 300 -units PixelsPerInch combined.jpg

explizitd.pdf:	explizitd.tex explizitd.inc
	pdflatex explizitd.tex

explizitd.inc explizitspektrum.inc:	explizitd.m
	octave --quiet explizitd.m

explizitspektrum.pdf:	explizitspektrum.tex explizitspektrum.inc
	pdflatex explizitspektrum.tex

implizitd.inc implizitspektrum.inc:	implizitd.m
	octave --quiet implizitd.m

implizitspektrum.pdf:	implizitspektrum.tex implizitspektrum.inc
	pdflatex implizitspektrum.tex

cnspektrum.inc:	cranknicholsond.m
	octave --quiet cranknicholsond.m

cnspektrum.pdf:	cnspektrum.tex cnspektrum.inc
	pdflatex cnspektrum.tex

explizitneumann.inc:	explizitn.m
	octave --quiet explizitn.m

explizitneumann.pdf:	explizitneumann.tex explizitneumann.inc
	pdflatex explizitneumann.tex

implizitneumann.inc:	implizitn.m
	octave --quiet implizitn.m

implizitneumann.pdf:	implizitneumann.tex implizitneumann.inc
	pdflatex implizitneumann.tex

cnneumann.inc:	cranknicholsonn.m
	octave --quiet cranknicholsonn.m

cnneumann.pdf:	cnneumann.tex cnneumann.inc
	pdflatex cnneumann.tex

ringgebiet.pdf:	ringgebiet.tex
	pdflatex ringgebiet.tex
