import numpy as np

def trapecio(f,a,b,N):
    h   = (b-a)/N
    xi  = np.linspace(a,b,N+1)
    fi  = f(xi)
    s   = 0.0
    for i in range(1,N):
        s = s + fi[i]
    s = (h/2)*(fi[0] + fi[N]) + h*s
    return s
    
    def romberg(f,a,b,nmax,epsilon = 1e-6):
# nmax  ... orden maximo del métod de Romberg (dimensión de la matríz)
    A         = np.zeros((nmax,nmax),float)
    convergencia = 0
    for i in range(0,nmax):
        N      = 2**i
        A[i,0] = trapecio(f,a,b,N)
        for k in range(0,i):
            n        = k + 2
            A[i,k+1] = 1.0/(4**(n-1)-1)*(4**(n-1)*A[i,k] - A[i-1,k])
        if (i > 0):
            if (abs(A[i,k+1] - A[i,k]) < epsilon):
               convergencia = 1
               break  
    ans = (A[i,k+1],N)
    return print('El valor de la integral es: %f con una N = %i'%ans) 
