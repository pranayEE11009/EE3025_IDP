import numpy as np
import matplotlib.pyplot as plt

N=6
x=np.array([1,2,3,4,2,1])

#defining h[n]
h=np.zeros(N)
h[0]=1
h[1]=(-1/2)*h[0]
h[2]=1-(1/2)*h[1]
for i in range(3,N):
    h[i]=(-1/2)*h[i-1]

#DFT function using matrix multiplication
def DFT(N):
    n,k=np.meshgrid(np.arange(N),np.arange(N))
    #here, n and k are NxN matrices where each point from these matrices
    #gives the x and y coordinates respectively of the intersections of a grid
    #spaned over the x and y axis with range 0 to N on each side.
    
    W=np.exp(-1j*2*np.pi*n*k/N)
    return W


X=DFT(N)@x    #DFT of x
H=DFT(N)@h    #DFT of h

#plotting
n=np.linspace(0,N-1,N)

plt.stem(n,x,use_line_collection='True')
plt.title('x[n]'); plt.xlabel('n'); plt.ylabel('magnitude')
plt.show()
plt.stem(n,h,use_line_collection='True')
plt.title('h[n]'); plt.xlabel('n'); plt.ylabel('magnitude')
plt.show()

plt.stem(n,abs(X),use_line_collection='True')
plt.title('$\mid X[k]\mid $') ; plt.xlabel('k') ; plt.ylabel('amplitude')
plt.grid()
plt.show()
plt.stem(n,np.angle(X,deg=True),use_line_collection='True')
plt.title(r'$ \angle{X[k]}$'); plt.xlabel('k'); plt.ylabel('phase in degrees')
plt.grid()
plt.show()

plt.stem(n,abs(H),use_line_collection='True')
plt.title('$\mid H[k] \mid $'); plt.xlabel('k'); plt.ylabel('amplitude')
plt.grid()
plt.show()
plt.stem(n,np.angle(H,deg=True),use_line_collection='True')
plt.title(r'$\angle{H[k]}$'); plt.xlabel('k'); plt.ylabel('phase in degrees')
plt.grid()
plt.show()
