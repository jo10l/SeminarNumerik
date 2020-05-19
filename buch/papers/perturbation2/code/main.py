import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)

def correct_direction(x, x0):
    factor = (np.sum(x * x0, axis=0, keepdims=True) >= 0) * 2 - 1
    x[:,:] = x * factor

def test(A, B):

    K0 = A
    
    f = plt.figure()

    lam0, x0 = np.linalg.eig(K0)

    plot_eigv(lam0, x0, '-bo')
    print("K0 accurate")
    print(lam0)
    print(x0)
    print()

    dK = (B-A)
    lamn, xn = perturbate(K0, dK, lam0, x0)

    # correct_direction(xn, x0)
    plot_eigv(lamn, xn, 'rx')
    print("K0 + dK perturbated")
    print(lamn)
    print(xn)
    print()

    lam, x = np.linalg.eig(B)

    # correct_direction(x, x0)
    plot_eigv(lam, x, '-g+')
    print("K0 + dK accurate")
    print(lam)
    print(x)
    print()

    return x0, x, xn, lam0, lam, lamn

def plot_eigv(lam, x, color):
    z = np.zeros((len(lam), 2))
    for i in range(len(lam)):
        z[:,1] = x[:,i] # lam[i] * x[:,i]
        plt.plot(z[0], z[1], color)

# def plot_eigv2(lam, x, color):
#     for i in range(len(lam)):
#         v = lam[i] * x[:,i]
#         plt.arrow(0, 0, v[0], v[1])

def perturbate(K0, dK, lam0, x0):

    x0 = x0.copy()

    #look for degenerated eigenvalues
    degens = []
    for i in range(len(lam0)):
        degen = np.where(lam0[i] == lam0[i:])[0]
        if len(degen) > 1:
            degens.append(degen)

    # solve small eigenvalue problem for degenerated eigenvalues and insert new eigenvectors
    for degen in degens:
        mat = x0[:, degen].T @ dK @ x0[:, degen]
        lam, x = np.linalg.eig(mat)
        x0[:, degen] = x0[:, degen] @ x

    # apply appperturbation algorithm
    lam = np.zeros_like(lam0)
    x = np.zeros_like(x0)

    for i in range(len(K0)):
        x0i = x0[:, [i]]
        lam0i = lam0[i]

        lam[i] = lam0i + (x0i.T @ (dK) @ x0i)

        x[:, [i]] = x0i # + imag(d * gamma) * x0i
        for j in range(len(K0)):
            if not np.isclose(lam0[j], lam0[i]):
            # if i != j:
                x0j = x0[:, [j]]
                lam0j = lam0[j]
                x[:, [i]] += ((x0j.T @ dK @ x0i) / (lam0i - lam0j)) * x0j

        x[:, [i]] = x[:, [i]] / np.linalg.norm(x[:, [i]])

    return lam, x



def example3d():

    
    A = np.array([[2,0,0],[0,2,0],[0,0,1]], dtype=np.float64)
    B = np.array([[2,0.3,0.4],[0.4,3,0.3],[0.4,0.3,1]], dtype=np.float64)

    # A = np.array([[0.8,0,0],[0,1,0],[0,0,1.2]], dtype=np.float64)
    # B = np.array([[0.9,0.1,0.3],[0.2,1.1,0.3],[0.3,0.3,1.2]], dtype=np.float64)

    # A = np.array([[1,2,3],[2,3,4],[5,6,7]], dtype=np.float64)
    # B = np.array([[1,2.3,3.4],[2.4,3,4.3],[5.4,6.3,7]], dtype=np.float64)

    x0, x_correct, x_perb, lam0, lam_correct, lam_perb = test(A, B)

    import jscomposer

    jc = jscomposer.JsonComposer()

    jc.add_transform(np.eye(3), "bbbbbb")

    jc.add_transform(A, "666666")
    jc.add_transform(B, "000099")
    jc.add_transform(B-A, "00ff00")

    # jc.add_basis(x0, "666666")
    # jc.add_basis(x_perb, "ff0000")
    # jc.add_basis(x_correct, "000099")

    jc.add_eig_basis(x0, lam0, "666666")
    jc.add_eig_basis(x_perb, lam_perb, "ff0000")
    jc.add_eig_basis(x_correct, lam_correct, "000099")

    jc.save()

    pass


def example2d_2():

    A = np.array([[1,2],[3,4]], dtype=np.float64)
    B = np.array([[1.1,2.3],[3.1,4.2]], dtype=np.float64)

    A = np.array([[1,0],[0,1]], dtype=np.float64)
    B = np.array([[-1, 0.5],[0.5, 1]], dtype=np.float64)

    A = np.array([[1,0.1],[0.2,1.5]], dtype=np.float64)
    B = np.array([[0.95, 0.5],[0.15, 1.55]], dtype=np.float64)

    x0, x_correct, x_perb, lam0, lam_correct, lam_perb = test(A, B)

    plt.axis('equal')
    plt.show()

    import jscomposer

    def to33(x):
        y = np.zeros((3, 3))
        y[:2, :2] = x
        return y

    def to3(x):
        y = np.zeros((3,))
        y[:2] = x
        return y

    jc = jscomposer.JsonComposer()

    jc.add_transform(np.eye(3), "bbbbbb")

    jc.add_transform(to33(A), "666666")
    jc.add_transform(to33(B), "000099")
    jc.add_transform(to33(B-A), "00ff00")

    # jc.add_basis(x0, "666666")
    # jc.add_basis(x_perb, "ff0000")
    # jc.add_basis(x_correct, "000099")

    jc.add_eig_basis(to33(x0), to3(lam0), "666666")
    jc.add_eig_basis(to33(x_perb), to3(lam_perb), "ff0000")
    jc.add_eig_basis(to33(x_correct), to3(lam_correct), "000099")

    jc.save()

    pass

if __name__ == "__main__":

    example2d_2()
    # example3d()

