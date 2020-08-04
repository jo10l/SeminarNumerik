rng(2)
n=6;
a=randn(n);
a=a+a'
a=hess(a);
[Evec,Eval]=eig(a);
Eval;
%%
htr= .5*(a(n-1,n-1) + a(n,n));                          
dscr= sqrt((.5*(a(n-1,n-1)-a(n,n)))^2 + a(n,n-1)^2);    
if htr < 0, dscr= -dscr; end                            
root1 = htr + dscr;                                     
if root1 == 0                                         
	root2 = 0;
else                                                    
	det= a(n-1,n-1)*a(n,n) -a(n,n-1)^2;                 
	root2= det/root1;
end
if abs(a(n,n)-root1) < abs(a(n,n)-root2)
	shift= root1;
else
	shift= root2;
end
cs= a(1,1) -shift; sn=a(2,1);
r= norm([cs sn]);
cs= cs/r; sn=sn/r;              
q0= [ cs -sn; sn cs];           
a(:,1:2) = a(:,1:2) * q0;
a(1:2,:) = q0'*a(1:2,:);
for ii = 1:n-2
	%Chase the bulge from position (ii+2, ii)
	cs=a(ii+1,ii);sn=a(ii+2,ii);
	r=norm([cs sn]);
	cs= cs/r; sn= sn/r;
	a(ii+1,ii) = r;
	a(ii+2,ii)=0;
	qi= [cs -sn; sn cs];
	
	%Gives the rotator to chase the bulge
	a(ii+1:ii+2,ii+1:n) =qi'*a(ii+1:ii+2,ii+1:n);
	a(:,ii+1:ii+2) = a(:,ii+1:ii+2)*qi;
end
format short e
subdiag = diag(a,-1);
format long
bottom_entry = a(n,n);