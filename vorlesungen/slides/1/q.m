#
# q.m
#
# (c) 2020 Prof Dr Andreas Müller
#

function retval = f(x)
	retval = 0.5 * (x + 2/x);
endfunction

x=2;
for i = (0:10)
	printf("%2d & %20.16f \\\\\n", i, x);
	x = f(x);
endfor
