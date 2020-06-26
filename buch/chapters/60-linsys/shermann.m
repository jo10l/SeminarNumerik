#
# shermann.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#

A = [
 -2,  1,  0,  0,  0;
  1, -2,  1,  0,  0;
  0,  1, -2,  1,  0;
  0,  0,  1, -2,  1;
  0,  0,  0,  1, -2
];

A1 = inverse(A)

e1 = [ 1; 0; 0; 0; 0 ];
e5 = [ 0; 0; 0; 0; 1 ];

E51 = e5*e1'

u = -e5
v = e1

B = A - u*v'

c = v' * A1 * u

B1 = A1 + (1/(1-c)) * (A1 * u * v' * A1)

B * B1
