# This program aims to solve the coupled differential equations associated with an SIR model
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def SIR(variables, t):
    #Introduces the variables, Living, Zombie, and Deceased
    #D is not needed bit we include it for clarity, as we use its initial condition
    L, Z, D= variables
    #Initiates the constants
    alpha = 0.1
    beta = 0.1
    gamma = 1
    delta = 0.6

    #Initiates the differential equations
    dLdt = (alpha - beta)*L -gamma*L*Z
    dZdt = (gamma-delta)*L*Z
    dDdt = (beta+delta*Z)*L

    return [dLdt, dZdt, dDdt]

# Set initial conditions
initial_conditions = [199, 1, 0]


# Define time points
t = np.linspace(0, 0.4, 100)

# Solve the equations
solution = odeint(SIR, initial_conditions, t)

# Plot the results
plt.plot(t, solution[:, 0], label='Living', color='blue')
plt.plot(t, solution[:, 1], label='Zombie', color='r')
plt.plot(t, solution[:, 2], label='Deceased', color='black')
plt.xlabel('Time')
plt.ylabel('Population ')
plt.legend()
plt.savefig(r'c:\Users\Kartik\Desktop\Masters Project\figures\LZD_1\\LZDplotoneone.png')
plt.show()