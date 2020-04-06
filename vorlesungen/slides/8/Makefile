#
# Makefile
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
images:	explizit.jpg implizit.jpg cranknicholson.jpg combined.jpg

explizit.inc:	explizit.m
	octave --silent explizit.m

explizit.png:	explizit.pov explizit.inc common.inc
	povray +A0.1 -W1920 -H1080 -Oexplizit.png explizit.pov

explizit.jpg:	explizit.png
	convert explizit.png -density 300 -units PixelsPerInch explizit.jpg



implizit.inc:	implizit.m
	octave --silent implizit.m

implizit.png:	implizit.pov implizit.inc common.inc
	povray +A0.1 -W1920 -H1080 -Oimplizit.png implizit.pov

implizit.jpg:	implizit.png
	convert implizit.png -density 300 -units PixelsPerInch implizit.jpg



cranknicholson.inc:	cranknicholson.m
	octave --silent cranknicholson.m

cranknicholson.png:	cranknicholson.pov cranknicholson.inc common.inc
	povray +A0.1 -W1920 -H1080 -Ocranknicholson.png cranknicholson.pov

cranknicholson.jpg:	cranknicholson.png
	convert cranknicholson.png -density 300 -units PixelsPerInch cranknicholson.jpg


combined.png:	combined.pov common.inc explizit.inc implizit.inc cranknicholson.inc
	povray +A0.1 -W1920 -H1080 -Ocombined.png combined.pov

combined.jpg:	combined.png
	convert combined.png -density 300 -units PixelsPerInch combined.jpg

