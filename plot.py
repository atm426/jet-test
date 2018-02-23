#===========================
# load checkpoints and plot
#===========================

import numpy as np
import matplotlib.pyplot as plt
import h5py
import glob

list = glob.glob("/Users/austin/research/jet-test/checkpoints/checkpoint_*.h5")

def main():

    i = 0
    for file in list:
        f = h5py.File(file)
        t = time(f)

        Nr = f['Grid/Nr'][0][0]
        rho = f['Data/Cells'][0:Nr, 0]
        P = f['Data/Cells'][0:Nr, 1]

        plt.title(str(i))
        plt.plot(rho, 'b-', label = str(round(t,4)))
        plt.plot(P, 'r-')
        plt.legend(numpoints=1, frameon=False, loc='best')
        plt.savefig("/Users/austin/research/jet-test/images/image_"+str(i).zfill(4)+".png")
        plt.close('all')
        print i
        i+=1

def time(file):

    t = file['Grid/T'][0]

    return t
