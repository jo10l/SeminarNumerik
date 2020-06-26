#
# Makefile
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	computationalmode.pdf

cm:	cm.cpp
	g++ -o cm -Wall -g cm.cpp

cm.tex:	cm
	./cm > cm.tex

computationalmode.pdf:	computationalmode.tex cm.tex
	pdflatex computationalmode.tex


