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

sky_sphere {
        pigment {
                color rgb<1,1,1>
        }
}

#declare step = 0.175;
#declare xstep = step;
#declare ystep = step;

#declare ixmin = -5;
#declare ixmax =  5;
#declare iymin = -5;
#declare iymax =  5;

#declare r = 0.003;

#if (0)
union {
#declare ix = ixmin;
#while (ix <= ixmax)
	#declare A = <ix * xstep, 0, iymin * ystep>;
	#declare B = <ix * xstep, 0, iymax * ystep>;
	cylinder { A, B, r }
	sphere { A, r }
	sphere { B, r }
	#declare ix = ix + 1;
#end
#declare iy = iymin;
#while (iy <= iymax)
	#declare A = <ixmin * xstep, 0, iy * ystep>;
	#declare B = <ixmax * xstep, 0, iy * ystep>;
	cylinder { A, B, r }
	sphere { A, r }
	sphere { B, r }
	#declare iy = iy + 1;
#end
	pigment {
		color White
	}
	finish {
		specular 0.9
		metallic
	}
}
#end

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

//#declare f = function(X, Y) { exp(-(SQR(X) + SQR(Y)) / (2 * SQR(0.5))) }
#declare f = function(X, Y) { 1-(SQR(X) + SQR(Y)) }

#macro flaeche(iX, iY)
	<iX * xstep, f(iX * xstep, iY * ystep), iY * ystep >
#end

#macro ebene(iX, iY)
	<iX * xstep, 0, iY * ystep >
#end

#declare pointoutside = function(X, Y) { select((SQR(X*xstep) + SQR(Y*ystep)) - 1, 0, 1) }

mesh {

	#declare ix = ixmin;
	#while (ix < ixmax)
		#declare iy = iymin;
		#while (iy < iymax)
			#declare A = flaeche(ix    , iy    );
			#declare B = flaeche(ix + 1, iy    );
			#declare C = flaeche(ix    , iy + 1);
			#declare D = flaeche(ix + 1, iy + 1);
			#declare c = pointoutside(ix, iy) + pointoutside(ix+1, iy) + pointoutside(ix, iy+1);
			#if (c)
			#else
				triangle { A, B, C }
			#end
			#declare c = pointoutside(ix+1, iy) + pointoutside(ix+1, iy+1)+ pointoutside(ix, iy+1);
			#if (c)
			#else
				triangle { B, D, C }
			#end
			#declare iy = iy + 1;
		#end
		#declare ix = ix + 1;
	#end

	pigment {
		color rgb<0.4, 0.6, 0.8>
	}
	finish {
		specular 0.9
		metallic
	}

}

#declare r2 = 0.003;

union {
	#declare ix = ixmin;
	#while (ix < ixmax)
		#declare iy = iymin;
		#while (iy < iymax)
			#declare A = flaeche(ix    , iy    );
			#declare B = flaeche(ix + 1, iy    );
			#declare C = flaeche(ix    , iy + 1);
			#declare D = flaeche(ix + 1, iy + 1);
			#declare c = pointoutside(ix, iy) + pointoutside(ix+1, iy) + pointoutside(ix, iy+1);
			#if (c)
			#else
				sphere { A, r2 }
				sphere { B, r2 }
				sphere { C, r2 }
				cylinder { A, B, r2 }
				cylinder { B, C, r2 }
				cylinder { C, A, r2 }
			#end
			#declare c = pointoutside(ix+1, iy) + pointoutside(ix+1, iy+1)+ pointoutside(ix, iy+1);
			#if (c)
			#else
				sphere { B, r2 }
				sphere { C, r2 }
				sphere { D, r2 }
				cylinder { B, D, r2 }
				cylinder { D, C, r2 }
				cylinder { C, B, r2 }
			#end
			#declare iy = iy + 1;
		#end
		#declare ix = ix + 1;
	#end

	pigment {
		color Yellow
	}
	finish {
		specular 0.9
		metallic
	}

}



union {
	#declare ix = ixmin;
	#while (ix < ixmax)
		#declare iy = iymin;
		#while (iy < iymax)
			#declare A = ebene(ix    , iy    );
			#declare B = ebene(ix + 1, iy    );
			#declare C = ebene(ix    , iy + 1);
			#declare D = ebene(ix + 1, iy + 1);
			#declare c = pointoutside(ix, iy) + pointoutside(ix+1, iy) + pointoutside(ix, iy+1);
			#if (c)
			#else
				sphere { A, r }
				sphere { B, r }
				sphere { C, r }
				cylinder { A, B, r }
				cylinder { B, C, r }
				cylinder { C, A, r }
			#end
			#declare c = pointoutside(ix+1, iy) + pointoutside(ix+1, iy+1)+ pointoutside(ix, iy+1);
			#if (c)
			#else
				sphere { B, r }
				sphere { C, r }
				sphere { D, r }
				cylinder { B, D, r }
				cylinder { D, C, r }
				cylinder { C, B, r }
			#end
			#declare iy = iy + 1;
		#end
		#declare ix = ix + 1;
	#end

	pigment {
		color White
	}
	finish {
		specular 0.9
		metallic
	}

}
