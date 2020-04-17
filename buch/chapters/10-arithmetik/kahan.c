double  s = 0;
double  c = 0;
for (int i = 1; i <= n; i++) {
        double  y = a(i);
        y = y - c;
        double  t = s + y;
        c = (t - s) - y;
        s = t;
}
