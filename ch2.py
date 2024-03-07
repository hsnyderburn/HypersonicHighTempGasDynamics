import numpy as np

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

M1 = 8
gamma = 1.4
beta = 12
p2_p1 = 1 + np.divide(2*gamma,gamma+1) * ((M1**2)*(np.sin(beta)**2))


print(p2_p1)
# t = 1
# rho =1
# basicCont = rho/t + np.gradient(rho*u)