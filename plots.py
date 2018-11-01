import numpy as np
import matplotlib.pyplot as plt

def D(N, d, omega, phi, phip):
    c=340.
    D = (1./N) * np.ones_like(phi)
    for n in range(1,N):
        D = D + (1./N) * np.exp( (1j)*n*d*(omega/c)*(np.sin(phi) - np.sin(phip)) )
    return D

phi = np.arange(-np.pi,np.pi,0.01)


# INCREASING OMEGA -> MORE LOBES
phip = 0
omegas = 2*np.pi*np.array([1000, 2000, 4000, 8000])
d = 0.1
N = 3

Ds = []
for omega in omegas:
    #newD = np.log(np.absolute(D(N, d, omega, phi, phip)))
    #Ds.append( np.absolute(np.amin(newD)) + newD )
    #Ds.append( 10*np.log10(np.absolute(D(N, d, omega, phi, phip))/.01) )
    newD = np.absolute(D(N, d, omega, phi, phip))
    smallest = np.amin(newD)
    Ds.append(np.log(newD/smallest))

fig1, ax1 = plt.subplots(1,4,subplot_kw=dict(projection='polar'))
ax1[0].plot(phi,Ds[0])
ax1[1].plot(phi,Ds[1])
ax1[2].plot(phi,Ds[2])
ax1[3].plot(phi,Ds[3])
plt.setp([a.get_yticklabels() for a in ax1], visible=False)
#plt.setp([a.set_thetagrids(range(0,360,90),frac=1.2) for a in ax1])
plt.setp([a.set_xticklabels([]) for a in ax1])
fig1.subplots_adjust(wspace=0.75)

# different pointing angles for different omegas
phips = np.pi*np.array([0, 1./6, 1./4, 5./6])
omega = 2*np.pi*2000
Ds = []
for phip in phips:
    #newD = np.log(np.absolute(D(N, d, omega, phi, phip)))
    #Ds.append( np.absolute(np.amin(newD)) + newD )
    #Ds.append( 10*np.log10(np.absolute(D(N, d, omega, phi, phip))/.01) )
    newD = np.absolute(D(N, d, omega, phi, phip))
    smallest = np.amin(newD)
    Ds.append(np.log(newD/smallest))

fig2, ax2 = plt.subplots(1,4,subplot_kw=dict(projection='polar'))
ax2[0].plot(phi,Ds[0])
ax2[1].plot(phi,Ds[1])
ax2[2].plot(phi,Ds[2])
ax2[3].plot(phi,Ds[3])
plt.setp([a.get_yticklabels() for a in ax2], visible=False)
#plt.setp([a.set_thetagrids(range(0,360,90),frac=1.2) for a in ax2])
plt.setp([a.set_xticklabels([]) for a in ax2])
fig2.subplots_adjust(wspace=0.75)

phips = np.pi*np.array([0, 1./6, 1./4, 5./6])
omega = 2*np.pi*4000
Ds = []
for phip in phips:
    #newD = np.log(np.absolute(D(N, d, omega, phi, phip)))
    #Ds.append( np.absolute(np.amin(newD)) + newD )
    #Ds.append( 10*np.log10(np.absolute(D(N, d, omega, phi, phip))/.01) )
    newD = np.absolute(D(N, d, omega, phi, phip))
    smallest = np.amin(newD)
    Ds.append(np.log(newD/smallest))

fig3, ax3 = plt.subplots(1,4,subplot_kw=dict(projection='polar'))
ax3[0].plot(phi,Ds[0])
ax3[1].plot(phi,Ds[1])
ax3[2].plot(phi,Ds[2])
ax3[3].plot(phi,Ds[3])
plt.setp([a.get_yticklabels() for a in ax3], visible=False)
#plt.setp([a.set_thetagrids(range(0,360,90),frac=1.2) for a in ax3])
plt.setp([a.set_xticklabels([]) for a in ax3])
fig3.subplots_adjust(wspace=0.75)

phips = np.pi*np.array([0, 1./6, 1./4, 5./6])
omega = 2*np.pi*1700
Ds = []
for phip in phips:
    #newD = np.log(np.absolute(D(N, d, omega, phi, phip)))
    #Ds.append( np.absolute(np.amin(newD)) + newD )
    #Ds.append( 10*np.log10(np.absolute(D(N, d, omega, phi, phip))/.01) )
    newD = np.absolute(D(N, d, omega, phi, phip))
    smallest = np.amin(newD)
    Ds.append(np.log(newD/smallest))

fig4, ax4 = plt.subplots(1,4,subplot_kw=dict(projection='polar'))
ax4[0].plot(phi,Ds[0])
ax4[1].plot(phi,Ds[1])
ax4[2].plot(phi,Ds[2])
ax4[3].plot(phi,Ds[3])
plt.setp([a.get_yticklabels() for a in ax4], visible=False)
#plt.setp([a.set_thetagrids(range(0,360,90),frac=1.2) for a in ax4])
plt.setp([a.set_xticklabels([]) for a in ax4])
fig4.subplots_adjust(wspace=0.75)


phips = np.pi*np.array([0, 1./6, 1./4, 5./6])
omega = 2*np.pi*1000
Ds = []
for phip in phips:
    #newD = np.log(np.absolute(D(N, d, omega, phi, phip)))
    #Ds.append( np.absolute(np.amin(newD)) + newD )
    #Ds.append( 10*np.log10(np.absolute(D(N, d, omega, phi, phip))/.01) )
    newD = np.absolute(D(N, d, omega, phi, phip))
    smallest = np.amin(newD)
    Ds.append(np.log(newD/smallest))

fig5, ax5 = plt.subplots(1,4,subplot_kw=dict(projection='polar'))
ax5[0].plot(phi,Ds[0])
ax5[1].plot(phi,Ds[1])
ax5[2].plot(phi,Ds[2])
ax5[3].plot(phi,Ds[3])
plt.setp([a.get_yticklabels() for a in ax5], visible=False)
#plt.setp([a.set_thetagrids(range(0,360,90),frac=1.2) for a in ax4])
plt.setp([a.set_xticklabels([]) for a in ax5])
fig5.subplots_adjust(wspace=0.75)


plt.show()
