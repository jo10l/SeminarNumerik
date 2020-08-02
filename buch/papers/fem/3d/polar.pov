//
// ansatz.pov
//
// (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
//
#include "colors.inc"

global_settings {
	assumed_gamma 1
}

#declare imagescale = 0.034;
#declare winkel = pi * (190 / 180);
#declare dist = 0.45;

camera {
        location <-30, 10, 20>
        look_at <0, 0.36, 0>
        right 16/9 * x * imagescale
        up y * imagescale
}

light_source {
        <-10, 10, 50> color White
        area_light <0.1,0,0> <0,0,0.1>, 10, 10
        adaptive 1
        jitter
}

light_source {
	< -4, 0.5, 0> color White
}

sky_sphere {
        pigment {
                color rgb<1,1,1>
        }
}

#declare Phistep = pi / 10;
#declare Rstep = 0.2;

#declare iPhimin = 0;
#declare iPhimax = 20;
#declare iRmin = 0;
#declare iRmax = 5;

#declare r = 0.003;

cylinder {
	<0, -r, 0>, <0, 0, 0>, 1
	pigment {
		color rgb<1, 0.2, 0.8>
	}
	finish {
		specular 0.9
		metallic
	}
}

#declare SQR = function(s) { s * s }

#declare func = function(s) { 1-SQR(s) }

#declare Phi = function(iPhi, iR) { Phistep * (iPhi + 0.5 * iR) }

#macro flaeche(iPhi, iR)
	<Rstep*iR*cos(Phi(iPhi,iR)), func(iR*Rstep), Rstep*iR*sin(Phi(iPhi,iR))>
#end

#macro ebene(iPhi, iR)
	< Rstep*iR*cos(Phi(iPhi, iR)), 0, Rstep*iR*sin(Phi(iPhi, iR)) >
#end

#declare sc = 0.999;

intersection {
	mesh {
		#declare iPhi = iPhimin;
		#while (iPhi < iPhimax)
			#declare A = ebene(iPhi, 0);
			#declare B = ebene(iPhi+1, 0);
			#declare C = sc * A;
			#declare D = sc * B;
			triangle { A, B, D }
			triangle { A, D, C }
			#declare iR = iRmin;
			#while (iR < iRmax)
				#declare A = flaeche(iPhi    , iR    );
				#declare B = flaeche(iPhi + 1, iR    );
				#declare C = flaeche(iPhi    , iR + 1);
				#declare D = flaeche(iPhi + 1, iR + 1);
				triangle { A, B, C }
				triangle { B, D, C }
				triangle { sc * A, sc * B, sc * C }
				triangle { sc * B, sc * D, sc * C }
				#declare iR = iR + 1;
			#end
			#declare iPhi = iPhi + 1;
		#end
		inside_vector <-0.001, 1, 0>
	}
	plane {  <cos(winkel), 0, sin(winkel)>, dist }

	pigment {
		color rgb<0.4, 0.6, 0.8>
	}
	finish {
		specular 0.9
		metallic
	}

}

#declare r2 = 0.003;

intersection {
	union {
		sphere { flaeche(0, 0), r2 }
		#declare iPhi = iPhimin;
		#while (iPhi < iPhimax)
			#declare A = flaeche(iPhi, 0);
			#declare B = flaeche(iPhi, 1);
			cylinder { A, B, r2 }
			#declare iR = 1;
			#while (iR < iRmax)
				#declare A = flaeche(iPhi    , iR    );
				#declare B = flaeche(iPhi + 1, iR    );
				#declare C = flaeche(iPhi    , iR + 1);
				#declare D = flaeche(iPhi + 1, iR + 1);
				sphere { A, r2 }
				sphere { B, r2 }
				sphere { C, r2 }
				cylinder { A, B, r2 }
				cylinder { B, C, r2 }
				cylinder { C, A, r2 }
				sphere { B, r2 }
				sphere { C, r2 }
				sphere { D, r2 }
				cylinder { B, D, r2 }
				cylinder { D, C, r2 }
				cylinder { C, B, r2 }
				#declare iR = iR + 1;
			#end
			#declare iPhi = iPhi + 1;
		#end
	}
	plane {  <cos(winkel), 0, sin(winkel)>, dist }

	pigment {
		color Yellow
	}
	finish {
		specular 0.9
		metallic
	}

}



union {
	sphere { ebene(0, 0), r2 }
	#declare iPhi = iPhimin;
	#while (iPhi < iPhimax)
		#declare A = ebene(iPhi, 0);
		#declare B = ebene(iPhi, 1);
		cylinder { A, B, r2 }
		#declare iR = 1;
		#while (iR < iRmax)
			#declare A = ebene(iPhi    , iR    );
			#declare B = ebene(iPhi + 1, iR    );
			#declare C = ebene(iPhi    , iR + 1);
			#declare D = ebene(iPhi + 1, iR + 1);
				sphere { A, r }
				sphere { B, r }
				sphere { C, r }
				cylinder { A, B, r }
				cylinder { B, C, r }
				cylinder { C, A, r }
				sphere { B, r }
				sphere { C, r }
				sphere { D, r }
				cylinder { B, D, r }
				cylinder { D, C, r }
				cylinder { C, B, r }
			#declare iR = iR + 1;
		#end
		#declare iPhi = iPhi + 1;
	#end

	pigment {
		color White
	}
	finish {
		specular 0.9
		metallic
	}

}
