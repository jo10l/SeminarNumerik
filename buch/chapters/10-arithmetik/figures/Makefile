#
# Makefile
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	verschmierung.pdf

verschmierung.pdf:	verschmierung.tex exppaths.tex
	pdflatex verschmierung.tex

exppaths.tex: ../../experiments/verschmierung/exppaths.tex
	cp ../../experiments/verschmierung/exppaths.tex .
