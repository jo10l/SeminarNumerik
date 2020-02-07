%
% common.tex -- gemeinsame Definition für die Illustrationen Mittelpunkt-
%               und Trapezregel
%
% (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
%

\def\a{1}
\def\b{11}

\def\tickszeichnen{
	\draw (\a,-0.1)--(\a,0.1); \node at (\a,-0.1) [below] {$\mathstrut a$};
	\draw (\b,-0.1)--(\b,0.1); \node at (\b,-0.1) [below] {$\mathstrut b$};
}

\def\A{0.03}
\def\B{3}

\def\kurve{
	\draw[line width=1.2pt] plot[domain=-0.1:12.1,samples=100]
		({\x},{\A*(\x-1)*(\x-7)*(\x-11)+\B});
}

\def\achsen{
	\draw[->] (-0.1,0)--(12.3,0) coordinate[label={$x$}];
	\draw[->] (0,-0.1)--(0,6.3) coordinate[label={right:$y$}];
}

\def\funktion{
	\node at (11.8,{\A*(11.8-1)*(11.8-7)*(11.8-11)+\B}) [above left] {$y=f(x)$};
}
