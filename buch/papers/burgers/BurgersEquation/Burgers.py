#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:16:54 2020

@author: nunigan
"""

import sympy
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import copy
from matplotlib import animation
# import dill
# from mayavi import mlab


class Burgers:
    def __init__(self, x_dim=100, t_dim=100, dx=0.1, dt=0.1):
        # Grid
        self.x = np.linspace(0, x_dim, int(x_dim/dx))
        self.t = np.linspace(0, t_dim, int(t_dim/dt))
        self.T, self.X = np.meshgrid(self.t, self.x)

        # Wave with initial Condition
        self.U1 = np.zeros((int(x_dim/dx), int(t_dim/dt)))
        print(np.shape(self.U1))
        self.U1[:, 0] = np.exp(-1*(self.x-x_dim/2)**2)
        # self.U1[:int(x_dim//(3*dx)), 0] = 0
        # self.U1[int(x_dim//(3*dx)):int(2*x_dim//(3*dx)), 0] = 1
        # self.U1[int(2*x_dim//(3*dx)):, 0] = 0

        # parameter
        self.dt = dt
        self.dx = dx
        self.x_dim = x_dim
        self.t_dim = t_dim
        self.M = int(x_dim/dx)
        self.N = int(t_dim/dt)

    def quadratic(self):
        U_quadratic1 = copy.deepcopy(self.U1)
        U_quadratic2 = copy.deepcopy(self.U1)

        for t in np.linspace(1, self.N-1, self.N-1, dtype=int):
            for x in np.linspace(1, self.M - 1, self.M - 1, dtype=int):
                d_U1_x1 = U_quadratic1[x-1, t]
                d_U1_t1 = U_quadratic1[x, t-1]
                # d_U1_x2 = U_quadratic2[x-1, t]
                # d_U1_t2 = U_quadratic2[x, t-1]
                U_quadratic1[x, t] = (d_U1_x1*self.dt - self.dx + (d_U1_x1**2*self.dt**2 - 2*d_U1_x1*self.dt*self.dx + 4*d_U1_t1*self.dt*self.dx + self.dx**2)**(1/2))/(2*self.dt)
                # U_quadratic2[x, t] = -(self.dx - d_U1_x2*self.dt + (d_U1_x2**2*self.dt**2 - 2*d_U1_x2*self.dt*self.dx + 4*d_U1_t2*self.dt*self.dx + self.dx**2)**(1/2))/(2*self.dt)

        return U_quadratic1

    def linear_convection(self, c=1):
        linear_con = copy.deepcopy(self.U1)
        linear_con[:,0] = np.append(np.append(np.zeros(int(len(self.x)/3)), np.ones(int(len(self.x)/3))), np.zeros(int(len(self.x)/3)))
        for t in np.linspace(1, self.N-1, self.N-1, dtype=int):
            for x in np.linspace(1, self.M-1, self.M-1, dtype=int):
                linear_con[x, t] = linear_con[x, t-1] - c*self.dt/self.dx*(linear_con[x, t-1] - linear_con[x-1, t-1])
        return linear_con

                
                
    def linear1(self):
        linear1 = copy.deepcopy(self.U1)
        for t in np.linspace(1, self.N-1, self.N-1, dtype=int):
            for x in np.linspace(1, self.M-1, self.M-1, dtype=int):
                xi = (linear1[x, t-1]-linear1[x-1, t-1])/self.dx
                d_U1_t = linear1[x, t-1]
                linear1[x, t] = d_U1_t/(1+self.dt*xi)
        return linear1

    def linear2(self):
        linear2 = copy.deepcopy(self.U1)
        for t in np.linspace(1, self.N-1, self.N-1, dtype=int):
            for x in np.linspace(1, self.M-1, self.M-1, dtype=int):
                xi = linear2[x, t-1]*(linear2[x, t-1]-linear2[x-1, t-1])/self.dx
                d_U1_t = linear2[x, t-1]
                linear2[x, t] = -self.dt*xi+d_U1_t
        return linear2

    def linear3(self, alpha):
        linear3 = copy.deepcopy(self.U1)
        for t in np.linspace(1, self.N-1, self.N-1, dtype=int):
            for x in np.linspace(1, self.M-2, self.M-2, dtype=int):
                linear3[x, t-1] += alpha*(linear3[x+1, t-1]+linear3[x-1, t-1]-2*linear3[x, t-1])
            for x in np.linspace(1, self.M-2, self.M-2, dtype=int):
                xi = linear3[x, t-1]*(linear3[x+1, t-1]-linear3[x-1, t-1])/(2*self.dx)
                linear3[x, t] = -self.dt*xi+linear3[x, t-1]
        return linear3

    def linear4(self, alpha):
        linear4 = copy.deepcopy(self.U1)
        for t in np.linspace(1, self.N-1, self.N-1, dtype=int):
            for x in np.linspace(1, self.M-2, self.M-2, dtype=int):
                xi = (linear4[x+1, t-1]-linear4[x-1, t-1])/(2*self.dx)
                d_U1_t = linear4[x, t-1]
                linear4[x, t] = d_U1_t/(1+self.dt*xi) + alpha*(linear4[x+1, t-1]+linear4[x-1, t-1]-2*linear4[x, t-1])
        return linear4

    def linear5(self):
        linear5 = copy.deepcopy(self.U1)
        for t in np.linspace(1, self.N-1, self.N-1, dtype=int):
            for x in np.linspace(1, self.M-2, self.M-2, dtype=int):
                linear5[x, t] =linear5[x, t-1]*(self.dx+linear5[x-1, t]*self.dt)/(self.dx+linear5[x, t-1]*self.dt)
        return linear5

    def implicit_solver(self):
        ut = sympy.symbols('u_{t}0:'+str(self.M))
        implicit = copy.deepcopy(self.U1)

        dt = sympy.symbols('delta_t')
        dx = sympy.symbols('delta_x')
        u1t = sympy.symbols('u_{t-1}0:5')

        for t in np.linspace(1, self.N-1, self.N-1, dtype=int):
            eqns = []
            eqns.append((ut[0]-implicit[0, t-1])/self.dt+implicit[0, t-1]*(ut[1]-ut[0])/self.dx)
            for i in np.linspace(1, self.M-2, self.M-2, dtype=int):
                eqns.append((ut[i]-implicit[i, t-1])/self.dt+implicit[i, t-1]*(ut[i+1]-ut[i-1])/(2*self.dx))
            eqns.append((ut[-1]-implicit[-1, t-1])/self.dt+implicit[-1, t-1]*(ut[-1]-ut[-2])/self.dx)

            # print(sympy.printing.latex(eqns))

            sols = sympy.solve(eqns, ut)
            # print(list(sols.items()))
            # print(sympy.printing.latex(sols))

            implicit[:, t] = np.array(list(sols.values()))
        return implicit

    def implicit_as_lin1(self):
        implicit = copy.deepcopy(self.U1)
        mask = np.append(np.array([-1, 1]), np.zeros(len(self.x)-2))
        A = np.zeros((len(self.x), len(self.x)))
        for i in range(len(self.x)-1):
            A[i+1, :] = np.roll(mask, i)

        for t in np.linspace(1, self.N-1, self.N-1, dtype=int):
            implicit[:, t] = implicit[:, t-1] - self.dt/self.dx*implicit[:, t-1]*(A@implicit[:, t-1])
        return implicit

    def implicit_as_leap_frog_forwards(self):
        implicit = copy.deepcopy(self.U1)

        mask = np.append(np.array([-1, 0, 1]), np.zeros(len(self.x)-3))
        A = np.zeros((len(self.x), len(self.x)))
        for i in range(len(self.x)-2):
            A[i+1, :] = np.roll(mask, i)
        # A[-1,:] = np.append(np.zeros(len(self.x)-2), np.array([-1, 1]))
        A[-1, :] = np.zeros(len(self.x))


        for t in np.linspace(1, self.N-1, self.N-1, dtype=int):
            implicit[:, t] = implicit[:, t-1] - self.dt/(2*self.dx)*implicit[:, t-1]*(A@implicit[:, t-1])
        return implicit

    def implicit_as_leap_frog_backwards(self):
        implicit = copy.deepcopy(self.U1)

        for t in range(self.N-1):
            dx = self.dx
            dt = self.dt
            x = np.zeros(self.M)

            d = 2*dx*implicit[:, t]
            d[0] = dx*implicit[0, t]
            d[-1] = dx*implicit[-1, t]

            a = -dt*implicit[1:, t]
            c = dt*implicit[:-1, t]

            b = np.full(self.M, 2*dx, dtype='Float64')
            b[0] = dx - dt*implicit[0, t]
            b[-1] = dx + dt*implicit[-1, t]

            c[0] = c[0]/b[0]
            d[0] = d[0]/b[0]
            for i in range(1, self.M-1):
                c[i] = c[i]/(b[i]-a[i]*c[i-1])
                d[i] = (d[i]-a[i]*d[i-1])/(b[i]-a[i]*c[i-1])

            x[-1] = d[-1]

            for i in range(self.M-2, -1, -1):
                x[i] = d[i]-c[i]*x[i+1]

            implicit[:, t+1] = x

        return implicit

    def implicit_as_leap_frog_backwards_analytical(self):
        implicit = copy.deepcopy(self.U1)

        f = dill.load(open("myfile", "rb"))

        for t in range(self.N-1):
            res = []
            for i in range(self.M):
                res.append(f[i](self.dt, self.dx, implicit[:, t]))
                # res.append(f[i](implicit[:, t]))
            implicit[:, t+1] = res

        return implicit

    def plot(self, data, save=False, title=''):
        SMALL_SIZE = 5
        MEDIUM_SIZE = 8
        BIGGER_SIZE = 12

        plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
        plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
        plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
        plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

        x = self.X.flatten()
        y = self.T.flatten()
        z = data.flatten()

        fig = plt.figure()
        axs = fig.gca(projection='3d')
        axs.set_xlabel('x (m)')
        axs.set_ylabel('t (s)')
        axs.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        axs.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        axs.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        axs.set_zticks([])
        axs.w_zaxis.line.set_lw(0.)
        axs.xaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
        axs.yaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
        axs.zaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
        axs.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0, antialiased=False, alpha=.99)
        fig.subplots_adjust(top = 1, bottom=0, left=-.1, right=1.1)
        axs.view_init(30, -60)



        # for i, angle in enumerate(range(0,360,1)):
        #     axs.view_init(30, angle)
        #     file = 'images/' + title +'{}.png'.format(i)
        #     fig.savefig(file, dpi=100)

        if save is True:
           fig.subplots_adjust(top = 1, bottom=0, left=-.1, right=1.1)
           axs.view_init(30, -60)
           fig.savefig('images/' +title+'_front.pdf')
           axs.view_init(89, -90)
           fig.subplots_adjust(top = 1.3, bottom=-.3, left=-.3, right=1.2)
           fig.savefig('images/' +title+'_top.pdf')

    def plot_animate_rot_3D(self, data, title=''):

        SMALL_SIZE = 5
        MEDIUM_SIZE = 8
        BIGGER_SIZE = 12

        plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
        plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
        plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
        plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

        x = self.X.flatten()
        y = self.T.flatten()
        z = data.flatten()

        fig = plt.figure()
        axs = fig.gca(projection='3d')
        axs.set_xlabel('x (m)')
        axs.set_ylabel('t (s)')
        axs.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        axs.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        axs.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        axs.set_zticks([])
        axs.w_zaxis.line.set_lw(0.)
        axs.xaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
        axs.yaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
        axs.zaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)

        def init():
            axs.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0, antialiased=False)
            return fig,

        def animate(i):
            axs.view_init(elev=30., azim=i-90)
            return fig,

        animate(0)
        plt.savefig('images/' +title + '_thumb.pdf')

        # Animate
        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                        frames=360, interval=10, blit=True)
        # Save
        anim.save('images/' +title+'.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

    def plot_animate_1D(self, datas, legend, title='t.mp4'):

        SMALL_SIZE = 5
        MEDIUM_SIZE = 8
        BIGGER_SIZE = 16

        plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
        plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
        plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
        plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
        plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

        fig = plt.figure(figsize=(16,9))
        ax = plt.axes(xlim=(min(self.x), max(self.x)), ylim=(0,1.1))
        plt.xlabel('space (m)')
        plt.ylabel('Amplitude (m)')
        plt.grid(True)
        lines = []
        textstr = 'time = {} s'.format(0)
        props = dict(boxstyle='round', facecolor='white', alpha=0.5)
        tex = ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=20,verticalalignment='top', bbox=props)

        for i in range(len(datas)):
            line, = ax.plot([],[], lw=4, label=legend[i])
            lines.append(line)
        plt.legend()


        def init():
            for lnum, line in enumerate(lines):
                line.set_data(self.x, datas[lnum][:,0])
            return lines

        def animate(i):
            for lnum, line in enumerate(lines):
                line.set_data(self.x, datas[lnum][:,i])  # update the data.
                tex.set_text('time = {} s'.format(i))
            return lines

        for j, i in enumerate(np.linspace(0,len(self.t)-1,20)):
            animate(int(i))
            plt.tight_layout()
            plt.savefig('images/' + title + str(j)+'.pdf')


        # plt.tight_layout()
        # anim = animation.FuncAnimation(fig, animate, init_func=init,
                                        # frames=len(self.t), interval=1, blit=True)
        # Save
        # anim.save('images/' + title + '1D.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

def plot_multiple():
    fig = plt.figure(figsize=(25, 13))
    cnt = 0
    for i in range(4):
        for j in range(4):
            x_dim = 10
            t_dim = 10
            dx = .3
            dt = 0.23+cnt

            b = Burgers(x_dim, t_dim, dx, dt)
            data = b.linear5()
            # data = b.linear1()

            axs = plt.subplot2grid((4, 4), (i, j), projection='3d')

            axs.tick_params(
                            labelbottom=False,
                            labelleft=False,
                            bottom=False,
                            left=False
                            )
            x = np.linspace(0, x_dim, int(x_dim/dx))
            t = np.linspace(0, t_dim, int(t_dim/dt))
            T, X = np.meshgrid(t, x)
            x = X.flatten()
            y = T.flatten()
            z = data.flatten()

            axs.set_xlabel('x (m)')
            axs.set_ylabel('t (s)')
            axs.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
            axs.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
            axs.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
            axs.set_zticks([])
            axs.w_zaxis.line.set_lw(0.)
            axs.xaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
            axs.yaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
            axs.zaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
            axs.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0, antialiased=False, alpha=.99)
            axs.view_init(30, -60)
            # axs.set_title(r'$\Delta x$ = {:.2}, $\Delta t$ = {:.2}'.format(dx, dt), fontsize=12)
            # axs.subplots_adjust(top = 1, bottom=0, left=-.4, right=1.1)
            # textstr = '$\Delta x$ = {:.2} \n$\Delta t$ = {:.2} \n$c$={:.2}'.format(dx, dt, dt/dx)
            textstr = '$c$={:.3}'.format(dt/dx)
            props = dict(boxstyle='round', facecolor='white', alpha=0.8)
            axs.text(x=10, y=1, z=max(z), s=textstr, fontsize=15, verticalalignment='top', bbox=props)
            cnt += .01

    plt.tight_layout()
    plt.show()
    # fig.savefig('images/multi_unstable.jpg', dpi=100)
    fig.savefig('images/multi_stable.pdf')


# test%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if __name__ == '__main__':

    b1 = Burgers(x_dim=10, t_dim=10, dx=.1, dt=.1)
    # plot_multiple()
    # lin_cov = b1.linear_convection(c=1)
    Uq1 = b1.quadratic()
    Ul1 = b1.linear1()
    Ul2 = b1.linear2()
    # Ul3 = b1.linear3(alpha=0)
    # Ul4 = b1.linear4(alpha=0)
    Ul5 = b1.linear5()
    # Ucn = b1.crank_nicolson()
    # implicit = b1.implicit_solver()

    # implicit = b1.implicit_as_lin1()B
    implicit = b1.implicit_as_leap_frog_backwards()
    # implicit = b1.implicit_as_leap_frog_forwards()
    # implicit= b1.implicit_as_leap_frog_backwards_analytical()

    # b1.plot_animate_rot_3D(Uq1, title='nlc_3d')
    b1.plot_animate_1D([Uq1, Ul5, implicit], ['Quadratic','Linear', 'Leap-Frog'], 'imp')
    # b1.plot(data=Uq1, save=False, title='Nonlinear_Convection')
    # b1.plot(data=lin_cov, save=False, title='Linear Convection')
    # b1.plot(data=Ul1, save=False, title='linear1')
    # b1.plot(data=Ul2, save=False, title='linear2')
    # b1.plot(data=Ul3, save=True, title='Leap_Frog')
    # b1.plot(data=Ul4, save=False, title='linear4')
    # b1.plot(data=Ul5, save=False, title='linear5')
    # b1.plot(implicit, save=True, title='Implicit')
