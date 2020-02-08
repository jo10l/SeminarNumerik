#
# Makefile
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	limits format

limits:	limits.cpp
	g++ -o limits -Wall limits.cpp

format:	format.cpp
	g++ -o format -Wall format.cpp

test:	limits
	./limits
