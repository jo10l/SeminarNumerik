#
# Makefile
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	kahan kahan-optimized

kahan:	kahan.cpp
	g++ -o kahan -Wall -g kahan.cpp

kahan-optimized: kahan.cpp Makefile
	g++ -o kahan-optimized -Wall -g -O4 kahan.cpp
