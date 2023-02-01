import numpy as np # Support for large, multi-dimensional arrays and matrices

# Perform convolution, x[n]*h[n]:-
def convolution(x, h):
    
    # String padding refers to adding, usually, non-informative characters to a string to one or both ends of it. This is most often done for output formatting and alignment purposes, but it can have useful practical applications. numpy.pad() function is used to pad the numpy arrays.

    size = (len(x) + len(h)) - 1 # Compute the size of system response
    x = np.pad(x,(0,size - len(x)),'constant')
    h = np.pad(h,(0,size - len(h)),'constant')
    y = np.zeros(size, dtype = float) # Returns a new array of given shape and type, with zeros.
    
    for i in range (size):
        for j in range (size):
            if i >= j:
                y[i] = float(y[i] + (float(x[i-j])*float(h[j])))
                
    return y # System Response y[n]

# Down-sample the given signal by a factor of "m":-
def down_sample(signal, m):
    down_sampler = []
    # Copy the element value from original signal to down sampler array with the increment value set to "m":
    for i in range(0, len(signal), m):
        down_sampler.append(signal[i])
    return down_sampler

# Up-sample the given signal by a factor of "l":-
def up_sample(signal, l):       
    up_sampler = []
    for i in range(len(signal)):
        up_sampler.append(signal[i]) # Copy the element value from original signal to up sampler array
        if i != len(signal):
            for k in range(l-1): 
                up_sampler.append(0) # Insert "l-1" zeros between the elements of the array
        else:
            break
    return up_sampler

# Driver Code: main(); Execution starts here.

x = [6, 7, 8, 9, 10]
h1= [1/np.sqrt(2), 1/np.sqrt(2)]; g1= [1/np.sqrt(2), 1/np.sqrt(2)] # Same coefficients
h2= [1/np.sqrt(2), -1/np.sqrt(2)]; g2 = [-1/np.sqrt(2), 1/np.sqrt(2)] # Complementary coefficients

# Analyze:-
a = convolution(x, h1); p = convolution(x, h2)
l_m = int(input("\nEnter the l- and m-factor expander: "))
b = down_sample(a, l_m); q = down_sample(p, l_m)

# Synthesize:-
c = up_sample(b, l_m); r = up_sample(q, l_m)
d = convolution(c, g1); s = convolution(r, g2)

# Add:-
y = np.add(d, s)
print(y)
