import numpy as np

c = 343.
omega = 2*np.pi*6000
d = 0.1
a = omega * d / c

print "a = ", a

f = lambda n: 2*(3*n - 1)*np.pi / (3.*a)
g = lambda n: 2*(3*n + 1)*np.pi / (3.*a)

print "m \t f \t g \t arcsin(f) \t arcsin(g)"
for m in range(-3,4):
    if np.abs(f(m)) <= 1 and np.abs(g(m)) <=1:
        print "%d \t %.2f \t %.2f \t %.2f \t %.2f" % (m,f(m),g(m),np.arcsin(f(m))*180./np.pi,np.arcsin(g(m))*180./np.pi)
