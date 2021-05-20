import scipy.integrate
from sys import argv
from numpy import exp, pi, arange, sum, array,sinh,cosh, interp

def g(lamb, omega, beta):
    hbar=1.0
    if omega==0.0:
       fac=(beta-lamb)*lamb*hbar**2/(2.*pi)
    else:
       fac=beta*hbar/(2.*pi*omega*sinh(beta*hbar*omega/2.))*(cosh(beta*hbar*omega/2.)-cosh(beta*hbar*omega/2. - lamb*hbar*omega))
    return fac

def f(lamb, omega, beta):
    hbar=1.0
    if omega==0.0:
       fac=1./(pi)
    else:
       fac=beta*hbar*omega*cosh(beta*hbar*omega/2.-lamb*hbar*omega)/(2.*pi*sinh(beta*hbar*omega/2.))
    return fac

def t(lamb, omega, beta):
    hbar=1.0
    if omega==0.0:
       fac=0.0
    else:
       fac=beta*hbar*(omega**3)*cosh(beta*hbar*omega/2.-lamb*hbar*omega)/(4.*pi*sinh(beta*hbar*omega/2.))
    return fac

def integrate(dx, func, fact):
    numarray=[i*j for i,j in zip(func,fact)]
    integ=dx*0.5*sum(array([(numarray[i]+numarray[i+1]) for i in range(len(numarray)-1)]))
    return integ 


inp=open(argv[1]) # PRIOR
temperature=float(argv[2]) # T in kelvin
beta=1./(temperature*3.1668152e-06) # convert beta to atomic units so hbar is 1
nbeads=int(argv[3])
omfac=4.5563353e-06 #invcm to atomic frequency
facatomic=0.024188843/(2.*pi) # factor to account for fs and atomic time mix in fourier transforms, as well as fourier transform conventions (2 pis)
dl=beta/nbeads
lamb=arange(0, (beta)+dl, dl)


whole=[line.split()[:] for line in inp]

inp.close()

freq=[float(i[0])*omfac for i in whole if float(i[0])<4500.0] 

fftfull=[float(i[1])/facatomic for i in whole]
fftfull=fftfull[:len(freq)]

# clean small numbers
fft=[i if i>max(fftfull)/10000. else 0.0 for i in fftfull]

#fft=fftfull

dx=freq[1]

# displacement
#for l in lamb:
#   gf=array([g(l, i, beta) for i in freq])
#   filetemp=open('f_displ_'+str(l), 'w')
#   trash=[filetemp.write('%f %f\n' %(i,j)) for i,j in zip(freq, gf)]
#   filetemp.close()
   # integrate
#   number2=integrate(freq[1], fft[1:], gf)
#   numarray=[i*j for i,j in zip(fft,gf)]
#   number=scipy.integrate.simps(numarray, x=freq)
#   print l, number

#print ' ' 

# cvv
for l in lamb:
   fplus=array([f(l, i, beta) for i in freq])
#   filetemp=open('f_vv_'+str(l), 'w')
#   trash=[filetemp.write('%f %f\n' %(i,j)) for i,j in zip(freq, fplus)]
#   filetemp.close()
   # integrate
   numarray=[i*j for i,j in zip(fft,fplus)]
   number=scipy.integrate.simps(numarray, x=freq)
   number=integrate(freq[1], fft[1:], fplus)
   print(l/beta, number)

print(' ')

## force
#for l in lamb:
#   gffplus=array([t(l, i, beta) for i in freq])
##   filetemp=open('f_ff_'+str(l), 'w')
##   trash=[filetemp.write('%f %f\n' %(i,j)) for i,j in zip(freq, gffplus)]
##   filetemp.close()
#   number=integrate(freq[1], fft, gffplus)
#   print l, number
#
#
