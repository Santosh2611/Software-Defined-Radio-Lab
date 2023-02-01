import matplotlib.pyplot as plt # Provides an implicit way of plotting
import numpy as np # Support for large, multi-dimensional arrays and matrices
import scipy.fftpack as sf # Module to calculate discrete fast Fourier transform 
import sounddevice as sd # Play and record NumPy arrays containing audio signals

# Sketch the spectrum of the signal in frequency domain:
def plot_frequency_domain(signal, plot_name):
    
    print("\n"); signal_fft = np.fft.fft(signal)
    plt.xlabel("Frequency in Hertz")
    plt.ylabel("A(f) in Volts")
    plt.title("" + str(plot_name) + " in Frequency Domain")
    plt.stem(np.arange(0, len(signal_fft)), signal_fft)
    plt.grid(True)
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
        if i != len(signal):
            for k in range(l-1): 
                up_sampler.append(0) # Insert "l-1" zeros between the elements of the array
        else:
            break
    return up_sampler

# Driver Code: main(); Execution starts here.

# Details for Sound Recording:-
Fs = int(input("\nEnter the sampling frequency in kilo-hertz: "))
Fs = Fs * 1000 # Fs = 48,000 Hz
t = int(input("Enter the time duration in seconds: "))
n = np.arange(0, t, 1/Fs) # Return evenly spaced values within a given interval

# Give information about available devices and find the default input/output device(s):-
print("\nThe list of audio devices connected to your system is as follows:\n" + str(sd.query_devices()))
print("\nNote: > indicates the default input device and < indicates the default output device respectively - " + str(sd.default.device))

# Record audio data from your sound device into a NumPy array:-
print("\nRecording has started.")
x = sd.rec(int(t*Fs), Fs, 1, blocking = 'True') 
#sd.wait()
x = x.flatten(); # Return a copy of the array (matrix) collapsed into one dimension.
#t = np.arange(0,d,1/Fs)
#x = np.sin(2*3.14*2000*t)
print("Recording has stopped.")

# Play back a NumPy array containing audio data:-
print("Recording is being played...")
sd.play(x,Fs)

title = "Recorded Sound"
# Plot the Recorded Wave:-
plt.xlabel('Number of Frames (Sampling Frequency * Time Duration)')
plt.ylabel('Amplitude')
plt.title(title)
plt.plot(x)
plt.grid(True)
plt.show()
plot_frequency_domain(x, title)

decomposition = int(input("\nEnter the number of levels of decomposition: "))

# Generate a Noise:- (Draw random samples from a normal distribution)
y = np.random.normal(0, 0.2, np.size(x)); # Additive Wired Gaussian Noise
x = x + y
plt.title('Histogram Representation - Gaussian Noise')
plt.hist(y) # Plot a Histogram
plt.grid(True) # Configure the grid lines
plt.show()
print("Noisy signal is being played...")
sd.play(x,Fs)

# Plot the Noisy Signal:-
plt.subplot(2,1,1)
plt.xlabel('Time (in Seconds)') 
plt.ylabel('Amplitude')
plt.title('Noisy Sinusoidal Wave')
plt.plot(n, x) 
plt.tight_layout() # Adjust the padding between and around subplots
plt.grid(True) # Configure the grid lines

# Perform Spectral Analysis:-
X_f = abs(sf.fft(x)) # Return the absolute value of the fast Fourier transform
l = np.size(x)
fr = (Fs/2)*np.linspace(0,1,int(l/2))
xl_m = (2/l)*abs(X_f[0:np.size(fr)]); # Compute Magnitude Spectrum

# Plot Magntiude Spectrum:
plt.subplot(2,1,2)
plt.title('Spectrum of Noisy signal')
plt.xlabel('Frequency (in Hertz)')
plt.ylabel('Magnitude (in dB)')
plt.plot(fr,20*np.log10(xl_m))
plt.tight_layout() # Adjust the padding between and around subplots
plt.grid(True) # Configure the grid lines

plt.show() # Display all open figures

h1= [1/np.sqrt(2), 1/np.sqrt(2)]; g1= [1/np.sqrt(2), 1/np.sqrt(2)] # Same coefficients
h2= [0, 0]; g2 = [0, 0] # Complementary coefficients
l_m_factor_expander = 2

for i in range(decomposition):
    # Analyze:-
    a = np.convolve(x, h1); p = np.convolve(x, h2)
    b = down_sample(a, l_m_factor_expander); q = down_sample(p, l_m_factor_expander)
    
    # Synthesize:-
    c = up_sample(b, l_m_factor_expander); r = up_sample(q, l_m_factor_expander)
    d = np.convolve(c, g1); s = np.convolve(r, g2)
    
    # Add:-
    x = np.add(d, s)

title = "Denoised Audio"
plt.xlabel('Number of Frames (Sampling Frequency * Time Duration)')
plt.ylabel('Amplitude')
plt.title(title); 
plt.plot(x)
plt.grid(True)
plt.show()

print("Denoised audio is being played...")
sd.play(x,Fs)
plot_frequency_domain(x, title)
