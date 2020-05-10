//
// common.inc
//
// (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
//

global_settings {
        assumed_gamma 1
}

#declare rechterwinkelradius = 0.5;
#declare rechterwinkelthickness = 0.01;
#macro rechterwinkel(o, v1, v2, c)
intersection {
        sphere { o, rechterwinkelradius }
        #declare rnormale = vnormalize(vcross(v1, v2));
        plane { rnormale, vdot(o, rnormale) + rechterwinkelthickness * rechterwinkelradius / 0.5 }
        plane { -rnormale, -vdot(o, rnormale) + rechterwinkelthickness * rechterwinkelradius / 0.5 }
        plane { -v1, -vdot(o, v1) }
        plane { -v2, -vdot(o, v2) }
        pigment {
                color c
        }
}
sphere { o + 0.45 * (vnormalize(v1) +vnormalize(v2)) * rechterwinkelradius,
        0.05 * rechterwinkelradius / 0.5
        pigment {
                color c
        }
}
#end

//
// draw an arrow from <from> to <to> with thickness <arrowthickness> with
// color <c>
//
#macro arrow(from, to, arrowthickness, c)
        #declare arrowdirection = vnormalize(to - from);
        #declare arrowlength = vlength(to - from);
        union {
                sphere {
                        from, 1.1 * arrowthickness
                }
                cylinder {
                        from,
                        from + (arrowlength - 5 * arrowthickness) * arrowdirection,
                        arrowthickness
                }
                cone {
                        from + (arrowlength - 5 * arrowthickness) * arrowdirection,
                        2 * arrowthickness,
                        to,
                        0
                }
                pigment {
                        color c
                }
                finish {
                        specular 0.9
                        metallic
                }
        }
#end

#declare imagescale = 0.134;

arrow(<-0.5,0,0>, <10.5,0,0>, 0.05, White)
arrow(<0,0,-0.5>, <0,0,5.5>, 0.05, White)
arrow(<0,-0.5,0>, <0,3.3,0>, 0.05, White)

camera {
        location <-30, 10, 20>
        look_at <5, 0.78, 1.8>
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

