#
# Makefile -- build 3d images
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	ansatz.jpg

ansatz.png:	ansatz.pov
	povray +A0.1 -W1920 -H1080 -Oansatz.png ansatz.pov

ansatz.jpg:	ansatz.png Makefile
	convert -extract 1700x1080+110+0 ansatz.png \
		-density 300 -units PixelsPerInch ansatz.jpg
