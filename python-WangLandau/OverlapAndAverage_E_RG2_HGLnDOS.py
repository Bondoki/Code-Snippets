import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fmin
import sys

if len(sys.argv) != 4:
    print("USAGE: OverlapAndAverage_E_RG2_HGLnDOS window1.dat window2.dat output.dat")
    sys.exit()
    
#print(sys.argv)
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])
 
E_RG2_HGLnDOS_1=np.loadtxt(sys.argv[1])
E_RG2_HGLnDOS_2=np.loadtxt(sys.argv[2])

# overlap in x between E_RG2_HGLnDOS_1 and E_RG2_HGLnDOS_2 for E_RG2_HGLnDOS_1
cE_RG2_HGLnDOS_1_2=np.in1d(E_RG2_HGLnDOS_1[:,0], E_RG2_HGLnDOS_2[:,0])
cE_RG2_HGLnDOS_2_1=np.in1d(E_RG2_HGLnDOS_2[:,0], E_RG2_HGLnDOS_1[:,0])

# plot data and overlap in x
#plt.plot(E_RG2_HGLnDOS_1[:,0],E_RG2_HGLnDOS_1[:,1])
#plt.plot(E_RG2_HGLnDOS_2[:,0],E_RG2_HGLnDOS_2[:,1])
#plt.plot(E_RG2_HGLnDOS_1[cE_RG2_HGLnDOS_1_2,0],E_RG2_HGLnDOS_1[cE_RG2_HGLnDOS_1_2,1])
#plt.plot(E_RG2_HGLnDOS_2[cE_RG2_HGLnDOS_2_1,0],E_RG2_HGLnDOS_2[cE_RG2_HGLnDOS_2_1,1])
#plt.show()




# plot shifted data

#plt.plot(E_RG2_HGLnDOS_1[:,0],E_RG2_HGLnDOS_1[:,1])
#plt.plot(E_RG2_HGLnDOS_2[:,0],E_RG2_HGLnDOS_2[:,1])

#plt.show()

# concatenate all data and averaging
#mean = np.array( [ E_RG2_HGLnDOS_1[cE_RG2_HGLnDOS_1_2,0], np.mean( np.array([ E_RG2_HGLnDOS_1[cE_RG2_HGLnDOS_1_2,1], E_RG2_HGLnDOS_2[cE_RG2_HGLnDOS_2_1,1]+offset ]), axis=0 ), np.mean( np.array([ E_RG2_HGLnDOS_1[cE_RG2_HGLnDOS_1_2,2], E_RG2_HGLnDOS_2[cE_RG2_HGLnDOS_2_1,2] ]), axis=0 ) ]).transpose()
mean = np.array( [ E_RG2_HGLnDOS_1[cE_RG2_HGLnDOS_1_2,0], np.mean( np.array([ E_RG2_HGLnDOS_1[cE_RG2_HGLnDOS_1_2,1], E_RG2_HGLnDOS_2[cE_RG2_HGLnDOS_2_1,1] ]), axis=0 ), np.mean( np.array([ E_RG2_HGLnDOS_1[cE_RG2_HGLnDOS_1_2,2], E_RG2_HGLnDOS_2[cE_RG2_HGLnDOS_2_1,2] ]), axis=0 ) ]).transpose()

#E_RG2_HGLnDOS_2Shifted = np.array([E_RG2_HGLnDOS_2[:,0], E_RG2_HGLnDOS_2[:,1], E_RG2_HGLnDOS_2[:,2]]).T

concatenate=np.concatenate((E_RG2_HGLnDOS_2[np.invert(cE_RG2_HGLnDOS_2_1),:3], mean, E_RG2_HGLnDOS_1[np.invert(cE_RG2_HGLnDOS_1_2),:3]))


np.savetxt(sys.argv[3], concatenate, header=" E, <Rg2>, LnDOS")
#plt.plot(concatenate[:,0],concatenate[:,1])
#plt.show()





