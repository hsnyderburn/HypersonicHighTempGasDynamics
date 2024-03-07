import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#Problem 2.1

#basic continuity, momentum, energy equations for flow across oblique shock waves (ex 4)
#deriv equations 2.6 and 2.8

#is there a python capablity to derive equations for us? 

#u2 and v2 are velocity components behind shck parallel and perpendicular to the upstream velocity.
#(not parallel and perpendicular to shock wave, as is usally taken in most standard shock wave derivations)
#following equations for oblique shock waves:
#upstream = 1, downstream = 2, beta = wave angle, M = mach number
#assumptions: calorically perfect gas - constant speciic heats
#M1 goes to infinity, M1^2 * sin^2(beta) >> 1. So M1^2 * sin^2(beta) - 1 = M1^2 * sin^2(beta)

M1 = np.zeros(50,6.0)
print(M1)
M1[0] = [5, 6, 7, 8, 9, 10]
print(M1)

gamma = 1.4
beta = np.linspace(0,1.5708) #angle of the wedge.
print(type(beta))
beta_deg = beta * np.divide(180,np.pi)

p2_p1 = []
p2_p1 = [1 + np.divide(2*gamma,gamma+1) * ((M1[0]**2)*(np.sin(beta)**2))]
print(np.size(p2_p1))
p2_p1[1] = [1 + np.divide(2*gamma,gamma+1) * ((M1[1]**2)*(np.sin(beta)**2))]
print(p2_p1)

    # p2_p1_Matrix = np.empty(size(p2_p1),size(M1))
    # print(p2_p1_Matrix)
    # p2_p1_Matrix(i) = p2_p1(i)

# rho2_rho1 = np.divide(gamma + 1, gamma - 1)
# T2_T1 = np.divide(2 * gamma * (gamma - 1), (gamma + 1)**2)* M1**2 * (np.sin(beta)**2)
# u2_V1 = 1 - np.divide(2* np.sin(beta)**2, gamma + 1)
# v2_V1 = np.divide(np.sin(2*beta),gamma + 1)

#now i want to plot to observe the data and see how wedge angle affects our flow ratios.
plt.plot(beta_deg, p2_p1, label='wedge angle')
plt.show()

# t = 1
# rho =1
# basicCont = rho/t + np.gradient(rho*u)