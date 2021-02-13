import numpy as np
import matplotlib.pyplot as plt

N=200 
x=np.array([1,2,3,4,2,1])

#DFT of x[n]
X = np.zeros(N) + 1j*np.zeros(N)
for k in range(N):
    for n in range(6):
            X[k]+=x[n]*np.exp(-1j*2*np.pi*k*n/N)

#defining h[n]
h=np.zeros(12)
h[0]=1
h[1]=(-1/2)*h[0]
h[2]=1-(1/2)*h[1]
for i in range(3,12):
    h[i]=(-1/2)*h[i-1]

#DFT of h[n]
H=np.zeros(N) + 1j*np.zeros(N)
for k in range(N):
    for n in range(N):
        if n<12:
            H[k]+=h[n]*np.exp(-1j*2*np.pi*k*n/N)
        else:
            H[k]+=0


#plotting
n=np.linspace(0,N-1,N)

plt.stem(np.linspace(0,5,6),x,use_line_collection='True')
plt.title('x[n]'); plt.xlabel('n'); plt.ylabel('magnitude')
plt.show()
plt.stem(np.linspace(0,11,12),h,use_line_collection='True')
plt.title('h[n]'); plt.xlabel('n'); plt.ylabel('magnitude')
plt.show()

plt.plot(n,abs(X))
plt.title('$\mid X[k]\mid $') ; plt.xlabel('k') ; plt.ylabel('amplitude')
plt.grid()
plt.show()
plt.plot(n,np.angle(X,deg=True))
plt.title(r'$ \angle{X[k]}$'); plt.xlabel('k'); plt.ylabel('phase in degrees')
plt.grid()
plt.show()

plt.plot(n,abs(H))
plt.title('$\mid H[k] \mid $'); plt.xlabel('k'); plt.ylabel('amplitude')
plt.grid()
plt.show()
plt.plot(n,np.angle(H,deg=True))
plt.title(r'$\angle{H[k]}$'); plt.xlabel('k'); plt.ylabel('phase in degrees')
plt.grid()
plt.show()
