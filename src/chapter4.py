import pandas as pd
import numpy as np


# Section 4.5: Determining treasury zero rates
# 3 month calibration
t = 0.25
pv = 97.5
fv = 100.0
rc_3 = -np.log(pv/fv)/0.25

# 6-month calibration
t = 0.5
pv = 94.9
fv = 100.0
rc_6 = -np.log(pv/fv)/0.5

# 1-year calibration
t = 1.0
pv = 90.0
fv = 100.0
rc_1y = -np.log(pv/fv)/1.0

# 1.5-year calibration
# with semiannual compounding, the 1.5 year spot rate can be calibrated using formula:
# 4e^(rc_6*0.5) + 4e^(-rc_1*1.0) + 104e^(-rc_1.5*1.5) = 96
rc_1_5 = -np.log((96 - 4*np.exp(-rc_6*0.5) - 4*np.exp(-rc_1y*1))/104)/1.5

# 2.0-year calibration
# with semiannual compouding, the 2.0 year spot rate can be calibrated using the formula:
# 6e^(rc_6*0.5) + 6e^(-rc_1*1.0) + 6e^(-rc_1.5*1.5) + 106e^(-rc_2_0*2.0) = 101.6
rc_2_0 = -np.log((101.6 - 6*np.exp(-rc_6*0.5) - 6*np.exp(-rc_1y*1) - 6*np.exp(-rc_1_5*1.5))/106)/2.0

print(rc_3)
print(rc_6)
print(rc_1y)
print(rc_1_5)
print(rc_2_0)


# Section 4.6: Forward Rates
"""
### Table 4.5: Calculation of forward LIBOR rates

| Year (n) | Zero rate for an n-year investment (% per annum) | Forward rate for nth year (% per annum) |
|----------|---------------------------------------------------|-----------------------------------------|
| 1        | 3.0                                               |                                         |
| 2        | 4.0                                               | 5.0                                     |
| 3        | 4.6                                               | 5.8                                     |
| 4        | 5.0                                               | 6.2                                     |
| 5        | 5.3                                               | 6.5                                     |

"""
# Formula: R_F = (R2*T2 - R1*T1)/(T2 - T1)
# Formula2: R_F = R2 + (R2 - R1)*T1/(T2-T1)
# Calculate forward rate of year 3 (starting from year 2, ending year 3)
f_2_3 = (4.6*3 - 4.0*2)/(3-2)
print(f_2_3)
f_3_4 = (5.0*4 - 4.6*3)/(4-3)
print(f_3_4)


# Section 4.8: Duration
"""
- The duration of a bond as its name implied, is a measure of how long on average the holder of the bond has to wait before receiving
cash payments.
- A zero-coupon bond that lasts n years has a duration of n years
- A coupon-bearing bond lasting n years has a duration of less than n years, because the holder receives some of the cash payments prior
to year n



"""








# Question 1



