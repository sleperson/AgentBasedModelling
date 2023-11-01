# This program aims to solve the coupled differential equations associated with an SIR model
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def SIR(variables, t):
    #Introduces the variables, Living, Zombie, and Deceased
    #D is not needed bit we include it for clarity, as we use its initial condition
    S, I, R= variables
    #Initiates the constants
    gamma =1
    delta = 1

    #Initiates the differential equations
    dSdt = -gamma*S*I
    dIdt = (gamma*S-delta)*I
    dRdt = delta*I

    return [dSdt, dIdt, dRdt]

# Set initial conditions
initial_conditions = [100, 100, 0]


# Define time points
t = np.linspace(0, 4, 100)

# Solve the equations
solution = odeint(SIR, initial_conditions, t)

# Plot the results
plt.plot(t, solution[:, 0], label='Susceptible', color='blue')
plt.plot(t, solution[:, 1], label='Infected', color='r')
plt.plot(t, solution[:, 2], label='Removed', color='black')
plt.xlabel('Time')
plt.ylabel('Population ')
plt.legend()
plt.savefig(r'C:\\Users\\Kartik\Desktop\\Masters Project\\figures\\SIRplotoneone.png')
plt.show()
