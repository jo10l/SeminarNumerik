#
# Makefile -- extract smaller image versions
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	plot_l_small.png plot_m_small.png plot_diff_l_m_small.png

SIZE=9000x5260+1000+600 

plot_l_small.png:	plot_l.png Makefile
	convert -extract $(SIZE) plot_l.png -scale 25% \
		plot_l_small.png

plot_m_small.png:	plot_m.png Makefile
	convert -extract $(SIZE) plot_m.png -scale 25% \
		plot_m_small.png

plot_diff_l_m_small.png:	plot_diff_l_m.png Makefile
	convert -extract $(SIZE) plot_diff_l_m.png -scale 25% \
		plot_diff_l_m_small.png

