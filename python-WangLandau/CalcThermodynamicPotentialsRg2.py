import numpy as np
import sys

if len(sys.argv) != 2:
    print("USAGE: CalcThermodynamicPotentials E_HGLnDOS_RG2.dat")
    sys.exit()
    
FH = np.loadtxt(sys.argv[1])

maximumFH = np.max(FH[:,1])

FH[:,1] = FH[:,1]-maximumFH


T = np.linspace(0.01, 10.0, 5000)

# find maximum for extrem exponentials
maximumExpArray= np.empty(len(T))

for i in range(len(T)):
    maximumExpArray[i]=np.max(FH[:,1]-FH[:,0]/T[i])



U = np.empty(len(T))
F = np.empty(len(T))
S = np.empty(len(T))
CV = np.empty(len(T))
RG2 = np.empty(len(T))
RG2Fluctuation = np.empty(len(T))

for i in range(len(T)):
    U[i]=np.sum(FH[:,0]*np.exp(FH[:,1]-FH[:,0]/T[i]-maximumExpArray[i]))/np.sum(np.exp(FH[:,1]-FH[:,0]/T[i]-maximumExpArray[i]))
    F[i]=-T[i]*(maximumExpArray[i]+np.log(np.sum(np.exp(FH[:,1]-FH[:,0]/T[i]-maximumExpArray[i]))))
    S[i]=(U[i]-F[i])/T[i]
    CV[i]=((np.sum(FH[:,0]*FH[:,0]*np.exp(FH[:,1]-FH[:,0]/T[i]-maximumExpArray[i]))/np.sum(np.exp(FH[:,1]-FH[:,0]/T[i]-maximumExpArray[i]))) - U[i]*U[i])/(T[i]*T[i])
    RG2[i]=np.sum(FH[:,2]*np.exp(FH[:,1]-FH[:,0]/T[i]-maximumExpArray[i]))/np.sum(np.exp(FH[:,1]-FH[:,0]/T[i]-maximumExpArray[i]))
    RG2Fluctuation[i]=((np.sum(FH[:,2]*FH[:,0]*np.exp(FH[:,1]-FH[:,0]/T[i]-maximumExpArray[i]))/np.sum(np.exp(FH[:,1]-FH[:,0]/T[i]-maximumExpArray[i]))) - RG2[i]*U[i])/(T[i]*T[i])

UT=np.array([T,U]).T
FT=np.array([T,F]).T
ST=np.array([T,S]).T
CVT=np.array([T,CV]).T
RG2T=np.array([T,RG2]).T
RG2FluctuationT=np.array([T,RG2Fluctuation]).T

# save output avoiding NaN or Inf
UTClean=UT[np.isfinite(UT).all(axis=1)]
STClean=ST[np.isfinite(ST).all(axis=1)]
FTClean=FT[np.isfinite(FT).all(axis=1)]
CVTClean=CVT[np.isfinite(CVT).all(axis=1)]
RG2TClean=RG2T[np.isfinite(RG2T).all(axis=1)]
RG2FluctuationTClean=RG2FluctuationT[np.isfinite(RG2FluctuationT).all(axis=1)]

np.savetxt(sys.argv[1]+"_U_T.dat", UTClean, header=" T <U>")
np.savetxt(sys.argv[1]+"_F_T.dat", FTClean, header=" T <F>" )
np.savetxt(sys.argv[1]+"_S_T.dat", STClean, header=" T <S>" )
np.savetxt(sys.argv[1]+"_CV_T.dat", CVTClean, header=" T <CV>" )
np.savetxt(sys.argv[1]+"_RG2_T.dat", RG2TClean, header=" T <Rg2>" )
np.savetxt(sys.argv[1]+"_RG2_T_Fluctuation.dat", RG2FluctuationTClean, header=" T d<Rg2>/dT" )

# shift S(T->0)=0, this also shifts F(T->0)=U(T->0)
minS0=STClean[0,1]
STCleanShifted = np.array([STClean[:,0], STClean[:,1]-minS0]).T
FTCleanShifted = np.array([FTClean[:,0], FTClean[:,1]+FTClean[:,0]*minS0]).T

np.savetxt(sys.argv[1]+"_F_T_shifted.dat", FTCleanShifted )
np.savetxt(sys.argv[1]+"_S_T_shifted.dat", STCleanShifted )



