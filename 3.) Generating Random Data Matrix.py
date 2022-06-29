# ********************************************************************************************************************
# A programme for randomally generating a matrix each for x-deformation, y-deformation and z-deformation
# This random data will follow a normal distribution
# *******************************************************************************************************************

#--------------------------------------------------------------------------------------------------------------------
# X-DEFORMATION
#--------------------------------------------------------------------------------------------------------------------
import scipy.stats
import numpy as np
import math
PI = math.pi
import geomdl.fitting
lower=0.9
upper=1.1
mu=0
sigma=1
xdeformation = scipy.stats.truncnorm.rvs((lower-mu)/sigma, (upper-mu)/sigma, loc=mu, scale=sigma, size=(30,20))

#----------------------------------------------------------------------------------------------------------------------
# Y-DEFORMATION
#----------------------------------------------------------------------------------------------------------------------

ydeformation = scipy.stats.truncnorm.rvs((lower-mu)/sigma, (upper-mu)/sigma, loc=mu, scale=sigma, size=(30,20))

#----------------------------------------------------------------------------------------------------------------------
# Z-DEFORMATION
#----------------------------------------------------------------------------------------------------------------------

zdeformation = scipy.stats.truncnorm.rvs((lower-mu)/sigma, (upper-mu)/sigma, loc=mu, scale=sigma, size=[30,20])

#----------------------------------------------------------------------------------------------------------------------
# PRINTING OFF THE MATRICES FOR X-DEFORMATION, Y-DEFORMATION AND Z-DEFORMATION
#----------------------------------------------------------------------------------------------------------------------
def frange(x, maximum, step):
    while x < maximum:
        yield x
        x += step # Step counter


def get_points(A, B, C, x0, y0, z0):
    centre = (x0, y0, z0)
    theta_steps = PI/8
    phi_steps  = PI/8
    points = []
    for theta in frange(0, 2*PI, theta_steps):
        for phi in frange(-PI/2, PI/2, phi_steps):
            point_one = (x0 + A * math.cos(theta) * math.cos(phi), y0 + B * math.sin(theta) *
                         math.cos(phi), z0 + C * math.sin(phi))
            point_two = (x0 + A * math.cos(theta + theta_steps) * math.cos(phi + phi_steps), y0 + B *
                         math.sin(theta + theta_steps) * math.cos(phi + phi_steps), z0 + C * math.sin(phi + phi_steps))
            points.append([centre, point_one, point_two])
    return points
points = get_points(80,100,100, 0, 0, 0)
