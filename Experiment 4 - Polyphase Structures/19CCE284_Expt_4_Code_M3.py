import matplotlib.pyplot as plt # Provides an implicit way of plotting
import numpy as np # Support for large, multi-dimensional arrays and matrices
import time # Handle time-related tasks

# Plot time-domain spectrum of given signal:-
def time_domain(signal, plot_name):
    
    plt.xlabel("Time in Seconds")
    plt.ylabel("A(t) in Volts")
    plt.title(str(plot_name) + " in Time Domain")
    plt.stem(np.arange(0, len(signal)), signal)
    plt.grid()
    plt.show() 

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
        if i != len(signal)-1:
            for k in range(l-1): 
                up_sampler.append(0) # Insert "l-1" zeros between the elements of the array
        else:
            break
    return up_sampler

# Perform convolution, x[n]*h[n]:-
def convolution(x, h):
    
    """
    String padding refers to adding, usually, non-informative characters to a string to one or both ends of it. This is most often done for output formatting and alignment purposes, but it can have useful practical applications. numpy.pad() function is used to pad the numpy arrays.
    """

    size = (len(x) + len(h)) - 1 # Compute the size of system response
    x = np.pad(x,(0,size - len(x)),'constant')
    h = np.pad(h,(0,size - len(h)),'constant')
    y = np.zeros(size, dtype = int) # Returns a new array of given shape and type, with zeros.
    
    for i in range (size):
        for j in range (size):
            if i >= j:
                y[i] = int(y[i] + (int(x[i-j])*int(h[j])))
                
    return y # System Response y[n]

# Driver Code: main(); Execution starts here.
    
# Generate the original signal:-
title = "Original Signal"
original_signal = [1, 2, 3, 4, 5, 6, 7, 8]
print("The original signal is: ", original_signal)
time_domain(original_signal, title)

# Generate the frequency response:-
title = "Frequency Response"
frequency_response = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("The frequency response is: ", frequency_response)
time_domain(frequency_response, title)

print("The order of the filter is 3.")
m = 3

# Case - I:-
start = time.time()
title_I = "Traditional Filter - Direct Representation"
output_I = convolution(original_signal, frequency_response)
print("\nThe system response after convolution for '" + str(title_I) + "' is: ", output_I) 
time_domain(output_I, title_I)
end = time.time()
print("The time of execution of '" + str(title_I) + "' is (in seconds):", end-start)

print("\n")

# Case - II:-
start = time.time()

title_II = "Polyphase Filter Representation"
down_sampler_0 = down_sample(original_signal, m)
up_sampler_0 = up_sample(down_sampler_0, m)
for i in range(m-1):
    up_sampler_0.append(0)
print("E0[n]: ", up_sampler_0) 

pad_frequency_response = np.pad(frequency_response, (m-1, 0), 'constant', constant_values = 0)
down_sampler_1 = down_sample(pad_frequency_response, m)
up_sampler_1 = up_sample(down_sampler_1, m)
for i in range(m-1):
    up_sampler_1.remove(up_sampler_1[i])
size_up_sampler_1 = len(up_sampler_0) - len(up_sampler_1)
for i in range(size_up_sampler_1):
    up_sampler_1.append(0)
print("E1[n]: ", up_sampler_1)

pad_frequency_response = np.pad(frequency_response, (m-2, 0), 'constant', constant_values = 0)
down_sampler_2 = down_sample(pad_frequency_response, m)
up_sampler_2 = up_sample(down_sampler_2, m)
for i in range(m-2):
    up_sampler_2.remove(up_sampler_1[i])
print("E2[n]: ", up_sampler_2) 

convolve_I = convolution(original_signal, up_sampler_0)
convolve_II = convolution(original_signal, up_sampler_1)
convolve_III = convolution(original_signal, up_sampler_2)
output_II = convolve_I + convolve_II + convolve_III
print("\nThe system response after summing up the individual convolutions' for '" + str(title_II) + "' is: ", output_II) 
time_domain(output_II, title_II)
end = time.time()
print("The time of execution of '" + str(title_II) + "' is (in seconds):", end-start)
