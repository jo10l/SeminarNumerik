def dgl(t, y):
    '''The differential equation to solve.'''
    r_x = y[0]
    r_y = y[1]
    v_x = y[2]
    v_y = y[3]
    p0 = v_x
    p1 = v_y
    p2 = -k/m * np.sqrt(v_x**2 + v_y**2) * v_x
    p3 = -k/m * np.sqrt(v_x**2 + v_y**2) * v_y - g
    return [p0, p1, p2, p3]

def runge_kutta(t):
    '''Runs Runge Kutta to find position and speed at time t.'''
    rk = sp.solve_ivp(fun=dgl, t_span = (0,t), 
    y0 = [r0x, r0y, v0x, v0y], method='RK45', vectorized = True)
    assert rk.status == 0
    time_at_end     = rk.t[-1]
    position_at_end = rk.y[0:2, -1]
    speed_at_end    = rk.y[2:4, -1]
    return time_at_end, position_at_end, speed_at_end