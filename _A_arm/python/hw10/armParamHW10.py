# Single link arm Parameter File
import numpy as np
# import control as cnt
import sys
sys.path.append('..')  # add parent directory
import armParam as P

Ts = P.Ts  # sample rate of the controller
sigma = 0.05  # cutoff freq for dirty derivative
tau_max = P.tau_max  # limit on control signal

#  tuning parameters
#tr = 0.8 # part (a)
tr = 0.6  # tuned for fastest possible rise time before saturation.
zeta = 0.90
ki = 0.1  # integrator gain

# desired natural frequency
wn = 0.5*np.pi/(tr*np.sqrt(1-zeta**2))
alpha1 = 2.0*zeta*wn
alpha0 = wn**2

# compute PD gains
kp = alpha0*(P.m*P.ell**2)/3.0
kd = (P.m*P.ell**2)/3.0*(alpha1-3.0*P.b/(P.m*P.ell**2))

print('kp: ', kp)
print('ki: ', ki)
print('kd: ', kd)



