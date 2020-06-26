syms U_t U_x dx dt U

eqn = (U-U_t)/dt + U*(U-U_x)/dx == 0
solution = (solve(eqn, U))
latex(solution)
latex(eqn)

%%
syms U_t U_x dx dt U

eqn = (U-U_t)/dt + U_t*(U-U_x)/dx == 0
solution = (solve(eqn, U))
latex(solution)
latex(eqn)

%% crank nicolson

syms U_t U_x dx dt U

eqn = (U-U_t)/dt + U*(U-U_x)/dx == 0
solution = (solve(eqn, U))
b = latex(solution)
latex(eqn)

%% implicit
syms dx dt

ut = sym('u_t',[1 3])
u1t = sym('u_t1',[1 3])

%eqns.append((ut[0]-u1t[0])/dt+u1t[0]*(ut[1]-ut[0])/dx)
%for i in range(1,99,1):
 %   eqns.append((ut[i]-u1t[i])/dt+u1t[i]*(ut[i+1]-ut[i-1])/(2*dx))
%eqns.append((ut[-1]-u1t[-1])/dt+u1t[-1]*(ut[-1]-ut[-2])/dx)

eqns = [];
eqns= [eqns, (ut(1)-u1t(1))/dt+ut(1)*(ut(2)-ut(1))/dx];
for i=2:2
    eqns= [eqns,(ut(i)-u1t(i))/dt+ut(i)*(ut(i+1)-ut(i-1))/(2*dx)];
end
eqns= [eqns, (ut(3)-u1t(3))/dt+ut(3)*(ut(3)-ut(2))/dx];

assume(ut,'real')
a = vpasolve(eqns, ut)
latex(a.u_t1)
latex(a.u_t2)
latex(a.u_t3)

%%

syms U_t U_x1 U_x2  dx dt U_x

eqn = (U_x-U_t)/dt + U_x*(U_x1-U_x2)/(2*dx) == 0
solution = (solve(eqn, U_x))
latex(simplify(solution))
latex(eqn)

%%

syms U_{i}^{n} U_{i}^{n-1} dx dt U_{i-1}^{n-1}

eqn = (U_{i}^{n}- U_{i}^{n-1})/dt + U_{i}^{n}*(U_{i}^{n-1}-U_{i-1}^{n-1})/dx == 0
solution = (solve(eqn, U_{i}^{n}))
latex(solution)
latex(eqn)

