#
# Makefile
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	verschmierung.pdf iteration.pdf \
	normal.pdf negativ.pdf quadratisch.pdf divergent.pdf negdiv.pdf \
	m1qp.pdf m1qn.pdf m1kp.pdf m1kn.pdf \
	mnqp.pdf mnqn.pdf mnkp.pdf mnkn.pdf

verschmierung.pdf:	verschmierung.tex exppaths.tex
	pdflatex verschmierung.tex

iteration.pdf:	iteration.tex
	pdflatex iteration.tex

normal.pdf:	normal.tex zeichnung.tex

negativ.pdf:	negativ.tex zeichnung.tex

quadratisch.pdf:	quadratisch.tex zeichnung.tex

divergent.pdf:	divergent.tex zeichnung.tex

negdiv.pdf:	negdiv.tex zeichnung.tex

m1qp.pdf:	m1qp.tex zeichnung.tex

m1qn.pdf:	m1qn.tex zeichnung.tex

m1kp.pdf:	m1kp.tex zeichnung.tex

m1qn.pdf:	m1qn.tex zeichnung.tex

mnqp.pdf:	mnqp.tex zeichnung.tex

mnqn.pdf:	mnqn.tex zeichnung.tex

mnkp.pdf:	mnkp.tex zeichnung.tex

mnqn.pdf:	mnqn.tex zeichnung.tex

%.pdf:	%.tex
	pdflatex $<
