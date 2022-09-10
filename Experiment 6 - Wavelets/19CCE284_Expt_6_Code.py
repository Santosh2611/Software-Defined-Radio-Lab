import matplotlib.pyplot as plt # Provides an implicit way of plotting
import numpy as np # Support for large, multi-dimensional arrays and matrices
import scipy.fftpack as sf # Module to calculate discrete fast Fourier transform 

# Compute DFT coefficients using linear transformation method:-    
def DFT(x, plot_name):

    # Compute W(N) 1D Array:-
    r1 = c1 = len(x)
    wn = []
    for i in range(r1):
        for j in range(c1):
            wn.append(np.exp(-2j * np.pi * i * j / len(x)))

    # numpy.reshape() is used to give a new shape to an array without changing its data.

    wn_multidim = np.reshape(wn, (r1, c1)) # An N*N W(N) matrix    
    r2 = len(x); c2 = 1
    x_multidim = np.reshape(x, (r2, c2)) # An N*1 x(N) matrix
    
    # Compute X(N) = W(N) * x(N), an N*1 matrix:-
    fourier_transform_multidim = [[0]*c2]*r1 # NULL Multidimensional Array Declaration
    fourier_transform_l_t = [] # Convert Multidimensional Array to 1D
    for i in range(r1):
        for j in range(c2):
            fourier_transform_multidim[i][j] = 0
            for k in range(c1):
                fourier_transform_multidim[i][j] += wn_multidim[i][k] * float(x_multidim[k][j])
            fourier_transform_l_t.append(abs(fourier_transform_multidim[i][j]))
                   
    plt.xlabel("Frequency (in Hertz)")
    plt.ylabel("Amplitude (in Volts)")
    plt.title("" + str(plot_name) + " in Frequency Domain")
    plt.stem(np.arange(0, len(fourier_transform_l_t)), fourier_transform_l_t)
    plt.grid(True)
    plt.show()

# Down-sample the given signal by a factor of "m":-
def down_sample(signal, m):
    down_sampler = []
    # Copy the element value from original signal to down sampler array with the increment value set to "m":-
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

# Driver Code:- main(); Execution starts here.

# Generate the sine signal:-
fs = int(input("Enter the desired sampling frequency (in Hertz): "))  
time_axis = np.arange(0, 1, 1/fs) # Define the time axis
sine_frequency = int(input("Enter the frequency of the sine signal (in Hertz): "))
original_signal = np.sin(2 * np.pi * sine_frequency * time_axis)

title = "Original Signal"
plt.xlabel("Time in Seconds")
plt.ylabel("A(t) in Volts")
plt.title("" + str(title) + " in Time Domain")
plt.stem(time_axis, original_signal)
plt.grid(True)
plt.show()

DFT(original_signal, title)
print("\nThe spectral analysis of the original signal in time and frequency domain is shown in the above plots.")

# Generate a Noise:- (Draw random samples from a normal distribution)
y = np.random.normal(0, 0.2, np.size(original_signal)); # Additive Wired Gaussian Noise
original_signal = np.add(original_signal, y)

plt.title("Histogram Representation - Gaussian Noise")
plt.hist(y) # Plot a histogram
plt.grid(True)
plt.show()

# Plot the Noisy Signal:-
plt.ylabel('Amplitude (in Volts)')
plt.title('Noisy Sinusoidal Wave')
plt.stem(original_signal) 
plt.grid(True)
plt.show()

# Perform Spectral Analysis:-
X_f = abs(sf.fft(original_signal)) # Return the absolute value of the fast Fourier transform
l = np.size(original_signal)
fr = (fs/2)*np.linspace(0,1,int(l/2))
xl_m = (2/l)*abs(X_f[0:np.size(fr)]); # Compute Magnitude Spectrum

# Plot Magntiude Spectrum:-
plt.title('Spectrum of Noisy Signal')
plt.xlabel('Frequency (in Hertz)')
plt.ylabel('Magnitude (in dB)')
plt.stem(fr,20*np.log10(xl_m))
plt.grid(True)
plt.show()

print("\n\nThe spectral analysis of the noisy signal in time and frequency domain is shown in the above plots.")

h1 = [1/np.sqrt(2), 1/np.sqrt(2)]; h2 = [1/np.sqrt(2), 1/np.sqrt(2)] # Same coefficients
g1 = [1/np.sqrt(2), -1/np.sqrt(2)]; g2 = [-1/np.sqrt(2), 1/np.sqrt(2)] # Complementary coefficients
l_m_factor_expander = 2

decomposition = int(input("\nEnter the number of levels of decomposition: "))
scaling_level = int(input("Enter at which scaling level, the wavelet noise should be removed (< level of decomposition): "))
for i in range(decomposition):
    
    # Analyze:-
    a = convolution(original_signal, h1); p = convolution(original_signal, g1)
    b = down_sample(a, l_m_factor_expander); q = down_sample(p, l_m_factor_expander)
        
    # Synthesize:-
    c = up_sample(b, l_m_factor_expander); r = up_sample(q, l_m_factor_expander)
    d = convolution(c, h2); s = convolution(r, g2)
        
    # Add:-
    denoised_signal = np.add(d, s)
    
    if i == (decomposition - scaling_level):
        denoised_signal = d

title = "Denoised Signal"
plt.ylabel('Amplitude (in Volts)')
plt.title(title); 
plt.stem(denoised_signal)
plt.grid(True)
plt.show()

DFT(denoised_signal, title)
print("\nThe spectral analysis of the denoised signal in time and frequency domain is shown in the above plots.")
