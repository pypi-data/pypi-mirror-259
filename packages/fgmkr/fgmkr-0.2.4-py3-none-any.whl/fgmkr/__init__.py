from matplotlib import pyplot as plt
def fgmk(n,x,y,xlabel,ylabel, titlestr, figtext = None, glabel = None, grid = None,dim=None):
    plt.figure(n)
    plt.plot(x,y, label = glabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if(grid == True):
        plt.grid(which='both')
    plt.title(titlestr)
    plt.text(0.5, -0.18, r'$\bf{Figure\ }$' + str(n) + r': '+ str(figtext), transform=plt.gca().transAxes,
            horizontalalignment='center', verticalalignment='center', fontsize=10)
    if dim != None:
        plt.figsize = dim
    if glabel != None:
        plt.legend()

    # plt.figure(1)
    # plt.figure()
    # fgmk(1, t_vals, dP_num(t_vals), 'time (s)', 'Power (W)', 'Power vs Time', glabel="f(x) = x^2 + 3x + 2", grid=1)