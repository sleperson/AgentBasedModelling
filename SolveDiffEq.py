# This program aims to solve the coupled differential equations associated with an SIR model
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

plt.clf()

def SIR(variables, t):
    #Introduces the variables, Living, Zombie, and Deceased
    #D is not needed bit we include it for clarity, as we use its initial condition
    L, Z, D= variables
    #Initiates the constants
    alpha = 0
    beta = 0
    gamma = 1
    delta = 0.6
    rho = 1

    #Initiates the differential equations
    dLdt = (alpha - beta)*L - gamma *L*Z
    dZdt = rho*beta*L + (gamma-delta)*L*Z
    dDdt = (1-rho)*beta*L + delta*L*Z

    return [dLdt, dZdt, dDdt]

# Set initial conditions
initial_conditions = [199, 1, 0]

# Define time points
t = np.linspace(0, 10, 100)

# Solve the equations
solution = odeint(SIR, initial_conditions, t)

# Plot the results
plt.plot(t, solution[:, 0], label='Living')
plt.plot(t, solution[:, 1], label='Zombie')
plt.plot(t, solution[:, 2], label='Deceased')
plt.xlabel('Time')
plt.ylabel('Population ')
plt.legend()
plt.show()