# ********************************************************************************************************************
# A programme for randomally generating a single data point for x deformation, y deformation and z deformation
# We want this random data to follow a normal distribution, so we just truncate it for the upper and lower bounds
# *******************************************************************************************************************

# Importing neccessary library
import scipy.stats

# Setting the upper bound and the lower bound
lower=0.9
upper=1.1

# Setting the mean value and standard deviation value, this will be based on a normal distribution
mu=0
sigma=1

# Truncating the normal distribution to take into account the upper and lower bound
samples = scipy.stats.truncnorm.rvs((lower-mu)/sigma, (upper-mu)/sigma, loc=mu, scale=sigma, size=(1,3))

# Printing off sample data
print(samples)