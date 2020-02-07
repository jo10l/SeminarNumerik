a = 0;
b = 1;
h = b-a;

function y = f(x) 
    y = sqrt(1 - x*x);
endfunction

function summe = M(h, a, b, f)
    x = a + h/2;
    s = 0;
    while (x < b)
        s = s + f(x);
        x = x + h;
    end
    summe = h * s;
endfunction

T = h * ( (1/2) * f(a) + (1/2) * f(b) )

for k = (2:20)
    T = (1/2) * T + (1/2) * M(h, a, b, @f);
    h = h/2;
endfor

