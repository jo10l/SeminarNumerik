#
# Makefile 
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all: testgmp testmpfr

testmpfr:	testmpfr.c
	gcc -o testmpfr -g -Wall -O2 -I /usr/lib/arm-linux-gnueabihf \
		testmpfr.c -lmpfr -lm

testgmp:	testgmp.c
	gcc -o testgmp -g -Wall -O2 testgmp.c -lgmp -lm

