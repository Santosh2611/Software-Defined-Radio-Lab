import matplotlib.pyplot as plt # Provides an implicit way of plotting
import numpy as np # Support for large, multi-dimensional arrays and matrices

# Compute DFT coefficients using linear transformation method:    
def DFT(x, plot_name):

    # Compute W(N) 1D Array:
    r1 = c1 = len(x)
    wn = []
    for i in range(r1):
        for j in range(c1):
            wn.append(np.exp(-2j * np.pi * i * j / len(x)))

    # numpy.reshape() is used to give a new shape to an array without changing its data.

    wn_multidim = np.reshape(wn, (r1, c1)) # An N*N W(N) matrix    
    r2 = len(x); c2 = 1
    x_multidim = np.reshape(x, (r2, c2)) # An N*1 x(N) matrix
    
    # Compute X(N) = W(N) * x(N), an N*1 matrix
    fourier_transform_multidim = [[0]*c2]*r1 # Null Multidimensional Array
    fourier_transform_l_t = [] # Convert Multidimensional Array to 1D
    for i in range(r1):
        for j in range(c2):
            fourier_transform_multidim[i][j] = 0
            for k in range(c1):
                fourier_transform_multidim[i][j] += wn_multidim[i][k] * float(x_multidim[k][j])
            fourier_transform_l_t.append(abs(fourier_transform_multidim[i][j]))
            
    print("\nThe Discrete Fourier Transform (DFT) Coefficients of the " + str(plot_name) + " obtained using Linear Transformation method are as follows: {}". format(fourier_transform_l_t))
        
    plt.xlabel("Frequency in Hertz")
    plt.ylabel("A(f) in Volts")
    plt.title("Spectral Analysis of " + str(plot_name) + " in Frequency Domain")
    plt.stem(np.arange(0, len(fourier_transform_l_t)), fourier_transform_l_t)
    plt.grid(True)
    plt.show()

def time_domain(signal, plot_name):
    
    plt.xlabel("Time in Seconds")
    plt.ylabel("A(t) in Volts")
    plt.title("Spectral Analysis of " + str(plot_name) + " in Time Domain")
    # plt.stem(np.arange(first_index, last_index), arr)
    plt.stem(np.arange(0, len(signal)), signal)
    plt.grid()
    plt.show()

    print("\nThe " + str(plot_name) + " coefficients in Time Domain are as follows: {}". format(signal))
    DFT(signal, plot_name) # Frequency Domain Analysis of Original Signal 

"""  
size_input = int(input("Enter the size of input x[n]: "))
arr = [0] * (size_input)
print("Enter the elements of the input x[n] one-by-one as follows: -")
for sample in range(0, size_input, 1):
    arr[sample] = input("Element " + str(sample+1) + ": ")
print("\nThe entered input x[n] is: - " + str(arr) + "\n")

index = int(input("Enter the element position that indicates n = 0 index: "))
first_index = 0 - index + 1
last_index = first_index + len(arr)
"""

title = "Original Signal"
arr = [2, 1, 3, 2, 1] # Toy Problem Array
time_domain(arr, title)

title = "Up-Sampler"
up_sampler = []
l = int(input("\nEnter the value of L-fold expander: "))
for i in range(len(arr)):
    up_sampler.append(arr[i]) # Copy the element value from toy problem to up sampler array
    if i != len(arr)-1:
        for k in range(l-1): 
            up_sampler.append(0) # Insert "l-1" zeros between the elements of the array
    else:
        break
time_domain(up_sampler, title)

title = "Down-Sampler"
down_sampler = []
m = int(input("\nEnter the value of M-fold expander: "))
# Copy the element value from toy problem to down sampler array with the increment value set to "m":
for i in range(0, len(arr), m):
    down_sampler.append(arr[i])
time_domain(down_sampler, title)
