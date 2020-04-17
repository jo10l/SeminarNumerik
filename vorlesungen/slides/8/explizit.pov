//
// explizit.pov
//
// (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
//
#version 3.7;
#include "colors.inc"
#include "common.inc"

mesh {
#include "explizit.inc"

	pigment {
		color rgb<1.0,0.0,0.2>
	}
	finish {
		specular 0.9
		metallic
	}
}
