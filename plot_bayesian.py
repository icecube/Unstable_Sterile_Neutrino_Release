import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

info = np.genfromtxt('BayesFactor.txt')

g2s = [0.0, 1.570796, 3.141593, 4.712389, 6.283185,
         7.853982, 9.424778, 10.995574, 12.566371]
         
scan = {}
for g2 in g2s:   
    scan[g2] = info[info[:,2] == g2]
    
x_edges = np.array([0.00944061, 0.01188502, 0.01496236, 0.01883649, 0.02371374,
       0.02985383, 0.03758374, 0.04731513, 0.05956621, 0.07498942,
       0.09440609, 0.11885022, 0.14962357, 0.18836491, 0.23713737,
       0.29853826, 0.3758374 , 0.47315126, 0.59566214, 0.74989421,
       0.94406088])
y_edges = np.array([9.44060876e-03, 1.18850223e-02, 1.49623566e-02, 1.88364909e-02,
       2.37137371e-02, 2.98538262e-02, 3.75837404e-02, 4.73151259e-02,
       5.95662144e-02, 7.49894209e-02, 9.44060876e-02, 1.18850223e-01,
       1.49623566e-01, 1.88364909e-01, 2.37137371e-01, 2.98538262e-01,
       3.75837404e-01, 4.73151259e-01, 5.95662144e-01, 7.49894209e-01,
       9.44060876e-01, 1.18850223e+00, 1.49623566e+00, 1.88364909e+00,
       2.37137371e+00, 2.98538262e+00, 3.75837404e+00, 4.73151259e+00,
       5.95662144e+00, 7.49894209e+00, 9.44060876e+00, 1.18850223e+01,
       1.49623566e+01, 1.88364909e+01, 2.37137371e+01, 2.98538262e+01,
       3.75837404e+01, 4.73151259e+01])

X_edges, Y_edges = np.meshgrid(x_edges, y_edges)

fig, axes = plt.subplots(nrows = 3, ncols = 3, figsize = (7.5,6.67))
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
mpl.rcParams['xtick.major.size'] = 2.5
mpl.rcParams['ytick.major.size'] = 2.5
mpl.rcParams['xtick.minor.size'] = 2.5
mpl.rcParams['ytick.minor.size'] = 2.5

for g2, ax in zip(g2s, axes.flat):   
    X = scan[g2][:,1].reshape(20,37).T
    Y = scan[g2][:,0].reshape(20,37).T    
    Z = scan[g2][:,3].reshape(20,37).T
    
    pcol = ax.pcolor(X_edges, Y_edges, Z, 
                     vmin = -2, vmax = 2,
                    rasterized = True,
                    linewidth=0,
                    cmap = 'PiYG_r')
    pcol.set_edgecolor('face')
    
    ax.semilogx()
    ax.semilogy()
    ax.set_xlim(.01,1.)
    ax.set_title(r'$g^2 =\ $'+str(round(g2/np.pi,1))+r' $\pi$')
    ax.set_yticks([.01,0.1,1.,10])

    for ax in axes[:,0]:
        ax.set_ylabel(r'$\Delta m^2_{41}\:(\rm{eV}^2$)')

    for ax in axes[-1,:]:
        ax.set_xlabel(r'$\sin^2 2\theta_{24}$')
        
cbar = fig.colorbar(pcol, ax = axes.ravel().tolist(),
                   extend='max')
cbar.set_label(r'$\log_{10}$(Bayes  Factor)')

plt.show()