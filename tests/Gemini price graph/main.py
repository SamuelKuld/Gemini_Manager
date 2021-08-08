from fees import *
import matplotlib.pyplot as plot

x = []
y = []
for dollar in range(0,250):
  x.append(true_fee_value(dollar)["amount"])
  y.append(true_fee_value(dollar)["point"])


plot.plot(x, y)

plot.show()
# This example shows us the best value that you can put in and get the best
# Ratio of fee to value (fee/value * 10 is the output of point)

# The only confusion I have is when the fees are applied throughout the process.
# I'll probably have to spend a good amount in order to test it and I am not sure if I would like to.