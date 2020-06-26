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

chapter3 =								\
	../slides/3/problem.tex						\
	../slides/3/linear.tex						\
	../slides/3/polygon.tex						\
	../slides/3/lagrange.tex					\
	../slides/3/gleichungen.tex					\
	../slides/3/nullstellenschachtelung.tex				\
	../slides/3/fehlerformel.tex					\
	../slides/3/runge.tex						\
	../slides/3/lissajous.tex					\
	../slides/3/tschebyscheff.tex					\
	../slides/3/tschebyscheffpoly.tex				\
	../slides/3/hermite.tex						\
	../slides/3/baryzentrisch.tex					\
	../slides/3/spline/fe.tex					\
	../slides/3/spline/forderungen.tex				\
	../slides/3/spline/variationsproblem.tex			\
	../slides/3/spline/eulerlagrange.tex				\
	../slides/3/spline/mechanik.tex					\
	../slides/3/spline/minimal.tex					\
	../slides/3/spline/hermite.tex					\
	../slides/3/spline/zweiteabl.tex				\
	../slides/3/spline/bedingungen.tex				\
	../slides/3/spline/gleichungssystem.tex				\
	../slides/3/chapter.tex	

chapter4 =								\
	../slides/4/plan.tex						\
	../slides/4/integral.tex					\
	../slides/4/riemann.tex						\
	../slides/4/korn.tex						\
	../slides/4/approximation.tex					\
	../slides/4/numerik.tex						\
	../slides/4/mittelpunkt.tex					\
	../slides/4/trapez.tex						\
	../slides/4/rekursion.tex					\
	../slides/4/fehler.tex						\
	../slides/4/romberg.tex						\
	../slides/4/rombergbeispiel.tex					\
	../slides/4/chapter.tex

chapter5 =								\
	../slides/5/richtungsfeld.tex					\
	../slides/5/reduktion.tex					\
	../slides/5/reduktionbeispiel.tex				\
	../slides/5/picard.tex						\
	../slides/5/anfangrand.tex					\
	../slides/5/euler.tex						\
	../slides/5/fehler.tex						\
	../slides/5/verbesserung.tex					\
	../slides/5/rungekutta.tex					\
	../slides/5/rkfehler.tex					\
	../slides/5/mehrschritt.tex					\
	../slides/5/sir.tex						\
	../slides/5/faktoren.tex					\
	../slides/5/sirsim.tex						\
	../slides/5/sirpath.tex						\
	../slides/5/sirbetasim.tex					\
	../slides/5/sirbetapath.tex					\
	../slides/5/i0slide.tex						\
	../slides/5/i0.tex						\
	../slides/5/sirI0path.tex					\
	../slides/5/sirI0sim.tex					\
	../slides/5/kapazitaet.tex					\
	../slides/5/ableitung.tex					\
	../slides/5/parameter.tex					\
	../slides/5/randwertproblem.tex					\
	../slides/5/schiessmethode.tex					\
	../slides/5/ballwurf.tex					\
	../slides/5/chapter.tex

chapter6 =								\
	../slides/6/linalg.tex						\
	../slides/6/kondition.tex					\
	../slides/6/konditionbeispiel.tex					\
	../slides/6/splitting.tex					\
	../slides/6/gaussseidel/iteration.tex				\
	../slides/6/gaussseidel/matrix.tex				\
	../slides/6/gaussseidel/spektralradius.tex			\
	../slides/6/gaussseidel/lambda.tex				\
	../slides/6/gaussseidel/beispiel.tex				\
	../slides/6/gaussseidel/gs.tex					\
	../slides/6/gaussseidel/beispiel2.tex				\
	../slides/6/gaussseidel/gs2.tex					\
	../slides/6/gaussseidel/konvergenz.tex				\
	../slides/6/gaussseidel/beispielkonv.tex			\
	../slides/6/powermethod.tex					\
	../slides/6/jacobi/eigenwerte.tex				\
	../slides/6/jacobi/drehung.tex					\
	../slides/6/jacobi/iteration.tex				\
	../slides/6/jacobi/konvergenz.tex				\
	../slides/6/jacobi/jm.tex					\
	../slides/6/fem/introbeispiel.tex				\
	../slides/6/fem/integralprinzip.tex				\
	../slides/6/chapter.tex

chapter7 =								\
	../slides/7/chapter.tex

chapter8 =								\
	../slides/8/pde.tex						\
	../slides/8/beispiele.tex					\
	../slides/8/diskretisierung.tex					\
	../slides/8/poisson.tex						\
	../slides/8/explizit.tex					\
	../slides/8/fdm.tex						\
	../slides/8/implizit.tex					\
	../slides/8/vergleich.tex					\
	../slides/8/waerme.tex						\
	../slides/8/courant.tex						\
	../slides/8/fvm.tex						\
	../slides/8/chapter.tex

slides = 								\
	$(chapter0) $(chapter1) $(chapter2) $(chapter3) $(chapter4) \
	$(chapter5) $(chapter6) $(chapter7) $(chapter8)
