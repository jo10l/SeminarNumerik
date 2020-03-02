#
# Makefile.inc -- additional depencencies
#
# (c) 20920 Prof Dr Andreas Müller, Hochschule Rapperswil
#
chapter0 =								\
	../slides/0/intro.tex						\
	../slides/0/resourcen.tex					\
	../slides/0/latextipps.tex					\
	../slides/0/themen.tex						\
	../slides/0/chapter.tex

chapter1 =								\
	../slides/1/float.tex						\
	../slides/1/ieee754.tex						\
	../slides/1/ausloeschung.tex					\
	../slides/1/verschmierung.tex					\
	../slides/1/assoziativ.tex					\
	../slides/1/iteration.tex					\
	../slides/1/fixpunktiteration.tex				\
	../slides/1/analyse.tex						\
	../slides/1/linear.tex						\
	../slides/1/quadratisch.tex					\
	../slides/1/instabil.tex					\
	../slides/1/chapter.tex

chapter2 =								\
	../slides/2/intervallhalbierung.tex				\
	../slides/2/sekanten.tex					\
	../slides/2/sekantenfehler.tex					\
	../slides/2/sekantenbeispiel.tex				\
	../slides/2/gleichungen.tex					\
	../slides/2/newton.tex						\
	../slides/2/newtonschnell.tex					\
	../slides/2/erfolgsfaktoren.tex					\
	../slides/2/chapter.tex

slides = 								\
	$(chapter0) $(chapter1) $(chapter2)
