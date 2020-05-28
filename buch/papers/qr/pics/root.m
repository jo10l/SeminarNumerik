## Copyright (C) 2020 User
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} root (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: User <User@DESKTOP-O8I1BVL>
## Created: 2020-04-27

function F = root(x)
#F(1)=sin(x(1))*sin(x(3))-cos(x(1))*cos(x(3))*sin(x(2))-2.8/sqrt(2.8^2+2^2+2^2);
#F(2)=-cos(x(3))*sin(x(1))*sin(x(2))-cos(x(1))*sin(x(3))-2/sqrt(2.8^2+2^2+2^2);
#F(3)=cos(x(2))*cos(x(3))-2/sqrt(2.8^2+2^2+2^2);
F(1)=cos(x(1))*sin(x(2))-1/sqrt(3);
F(2)=sin(x(1))*sin(x(2))-1/sqrt(3);
F(3)=cos(x(2))-1/sqrt(3);
endfunction
