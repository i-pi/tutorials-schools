import numpy as np

def autoCorr(infile,nbead,columns,mlag,nequi,dt,verbosity,ncol):

    data = np.genfromtxt(infile,skip_header = ncol+nequi,usecols = columns)
    if (len(columns)>1): data = np.sum(data,axis=-1)

    autocorr = np.zeros((mlag),float)
    autoerror = np.zeros((mlag),float)
    block = np.zeros((mlag), float)
    blockerror = np.zeros((mlag), float)
    times = np.arange(mlag)

    # Calculates the mean, variance and stadard deviation 
    mean = np.mean(data)
    var = np.mean(data**2)-mean**2
    std = np.sqrt(var) if(abs(var)>1.0e-15) else  0.

    # Calculates the normalized autocorrelation function
    for tt in range(mlag):
        autocorr[tt] = np.dot(data[:len(data)-tt]-mean,data[tt:len(data)]-mean) / (len(data)-tt)
    autocorr /= autocorr[0]

    # Estimating the autocorrelation time (integral of the autocorrelation function)
    tau = sum(autocorr) - autocorr[0]*0.5*dt
    tau2 = sum(autocorr**2) - autocorr[0]*0.5*dt
    # Calculating the standard error in the mean value
    error = std/np.sqrt(len(data)*dt*0.5/tau)

    # printing the information 
    if(verbosity>0):    
        title = str(nbead)+' bead' if nbead<2 else str(nbead)+' beads'
        print('==================================', title, '=============================================')
        print(' mean = %8.4e  |  variance: = %8.4e  |  st.dev. = %8.4e'%(mean,var,std))
        print('<tau> = %8.4e  |    <tau^2> = %8.4e  |  error = %8.4e'%(tau,tau2,error))
    
    # Calculating the block correlation function
    block[0]=0.
    block[1]=autocorr[0]*0.5
    vtimesm = autocorr[1]
    for m in range(2,mlag):
        block[m]=block[m-1]+vtimesm*(1./(m-1)-1./(m))
        vtimesm+=autocorr[m]*m
    block *= 2*dt

    # here we compute the errors on ACF, assuming that the AC is a gaussian
    # distributed random variable. see Zwanzig and Ailawadi¸ PR 182 (1969)
    # **********************************************************************

    tau2 *= 2./(len(data)*dt)
    tau2 = np.sqrt(tau2) if tau2>0 else 0.
    
    for i in range(mlag):
        autoerror[i]=tau2*(1-autocorr[i]);
    
    # Calculating the block error
    #    //the errors on blocking averages can be computed in a similar way 
    #    //!BEWARE THIS FORMULA NEED CHECK!!!!!!!!!!!!!!!!

    for i in range(mlag):
        blockerror[i]=tau2*abs(block[i]-i*dt/2.)

    if(verbosity>1):
        # printing the information 
        print('        time               acf             Dacf            block              Dblock   ')
        print('---------------------------------------------------------------------------------------')
        for i in range(mlag):
            print('%15.8f   %15.8f   %15.8f   %15.8f   %15.8f'%(times[i], autocorr[i], autoerror[i], block[i], blockerror[i]))
    if(verbosity>0): print('=======================================================================================\n')
    return mean, error
