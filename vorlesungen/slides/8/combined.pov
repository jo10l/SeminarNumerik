//
// cranknicholson.pov
//
// (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
//
#version 3.7;
#include "colors.inc"
#include "common.inc"

mesh {
#include "cranknicholson.inc"

	pigment {
		color rgb<0.2,0.6,1.0>
	}
	finish {
		specular 0.9
		metallic
	}
}

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

mesh {
#include "implizit.inc"

	pigment {
		color rgb<0.4,0.8,0.2>
	}
	finish {
		specular 0.9
		metallic
	}
}
