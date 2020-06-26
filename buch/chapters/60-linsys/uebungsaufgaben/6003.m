#
# 6003.m
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#


do
spektralradiusJacobi = 1;
spektralradiusGaussSeidel = 1;

do 
	A = round(rand(3,3) * 25 - 12 * ones(3,3));
	if (A(1,1) == 0) 
		A(1,1) = 1;
	end
	if (A(2,2) == 0) 
		A(2,2) = 1;
	end
	if (A(3,3) == 0) 
		A(3,3) = 1;
	end
	d = abs(det(A));
until (d == 1);

A
B = inverse(A)

r = [ 0, 1, 1; 0, 0, 1; 0, 0, 0];
l = [ 0, 0, 0; 1, 0, 0; 1, 1, 0];
d = [ 1, 0, 0; 0, 1, 0; 0, 0, 1];

L = l.*A
R = r.*A
D = d.*A

try 
	F = inverse(L+D)*R
	spektralradiusGaussSeidel = max(abs(eig(F)))
	F = inverse(D)*(L+R)
	spektralradiusJacobi = max(abs(eig(F)))
catch
end_try_catch

until ((spektralradiusJacobi > 1.01) && (spektralradiusGaussSeidel < 0.99));

