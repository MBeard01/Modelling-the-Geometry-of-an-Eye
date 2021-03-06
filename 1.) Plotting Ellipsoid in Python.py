# Imports necessary modules
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats


def random_noise(m, n, bound):
    """
    A function that generates 3 mxn matrices representing the random noise for each x y and z coordinate respectively
    the random noise is generated using the normal distribution, and is anywhere between 1-bound and 1+bound
    The smaller bound is, the less variation due to noise there is.
    """

    # Defining the lower bound as being 1-bound
    lower = 1 - bound

    # Defining the upper bound as being 1+bound
    upper = 1 + bound

    # Setting the mean equal to zero, so that the random data will follow a standard normal distribution
    mu = 0

    # Setting the standard variation as being 1, so that the random data will follow a standard normal distribution
    sigma = 1

    # Setting the random x matrix to follow a standard normal distribution, by truncating it according to the bounds,
    # and setting the other parameters according to what we have already defined
    xrandom = scipy.stats.truncnorm.rvs((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size=(m, n))

    # Setting the random y matrix to follow a standard normal distribution, by truncating it according to the bounds,
    # and setting the other parameters according to what we have already defined
    yrandom = scipy.stats.truncnorm.rvs((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size=(m, n))

    # Setting the random z matrix to follow a standard normal distribution, by truncating it according to the bounds,
    # and setting the other parameters according to what we have already defined
    zrandom = scipy.stats.truncnorm.rvs((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size=[m, n])

    return xrandom, yrandom, zrandom


def plot_ellipsoid(xlength, ylength, zlength, xrandom, yrandom, zrandom,
                   elevation, azimuth):
    """
    A function that takes three parameters representing the x, y and z lengths of an ellipsoid, three matrices of
    random noise for the x y and z coordinates, and two parameters representing the elevation and azimuth angle
    the ellipsoid is viewed from.
    It then plots a 3D graph of the ellipsoid with the origin at its centre viewed from that angle,
    with random noise distorting the shape
    the elevation and azimuth should be between 0 and 360
    """

    # Determines the size of the image created and automatically scales the graph appropriately, otherwise you will be
    # unable to even see the deformations when you change the parameters
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    # Creates a 3D figure, using the idea of a subplot and projecting it so it will be 3D
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Temporary radius value for now, this will be called to make sure that the axes have an even scale
    radius = 100

    # Creates a matrix of angles u and v, where u represents the azimuth angle and v represents the polar angle
    # about the origin
    u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]

    # Calculates the matrix of x coordinates, with the parameterised formula for an ellipsoid, multiplied by the random
    # noise matrix for x
    x = xrandom * xlength * np.cos(u) * np.sin(v)

    # Calculates the matrix of y coordinates, with the parameterised formula for an ellipsoid, multiplied by the random
    # noise matrix for y
    y = yrandom * ylength * np.sin(u) * np.sin(v)

    # Calculates the matrix of z coordinates, with the parameterised formula for an ellipsoid, multiplied by the random
    # noise matrix for z
    z = zrandom * zlength * np.cos(v)

    # Makes sure the axes have an even scale, so we can see the deformation clearly
    plt.xlim(xmin=-1 * radius, xmax=radius)
    plt.ylim(ymin=-1 * radius, ymax=radius)
    ax.set_zlim(zmin=-1 * radius, zmax=radius)

    # Labels the axes X, Y and Z, as this seems appropriate
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Positions the camera, to allow us to navigate around the ellipsoid
    ax.view_init(elev=elevation, azim=azimuth)

    # Plots the x y and z coordinates with the surface shaded with whatever colour map style
    # The centre of the ellipsoid is (0,0,0) at current
    # Obviously more consideration will need to be make for how to adapt the code when the centre is not at the origin
    ax.plot_surface(x, y, z, cmap='magma')
    plt.show()
    return x, y, z


# We need to now define xrandom, y random and zrandom as being generated by the function random_noise
# Parameters of your choosing can be inserted
# Remember that the first parameter is m for the matrix, the second parameter is n for the matrix, and the last
# parameter is the bound (pick a bound according to the amount of variation expected)
xrandom, yrandom, zrandom = random_noise(30, 20, 0.03)

# Here we need to define x, y and z after it was returned in the function
# We do this by calling the function plot_ellipsoid, and feeding in parameters for x_length, y_length, z_length
# xrandom (you don't need to define here), yrandom (you don't need to define here), zrandom (you don't need to define
# here), the elevation and the azimuth
x, y, z = plot_ellipsoid(80, 100, 100, xrandom, yrandom, zrandom, 45, 20)

# In order to work with the linear algebra least square solver, we must flatten the x, y, z arrays into one-
# dimensional arrays, otherwise Python would fire an error that a three-dimensional array was given when a two-
# dimensional array must be given in order for the least square solver to work
x = x.flatten()
y = y.flatten()
z = z.flatten()

# We begin the code for extracting the parameters of the sphere/ellipsoid by defining a matrix A
# It is formed into a matrix using the numpy array function, and we square each of our x, y, z so that it is a matrix
# of squared data components
A = np.array([x ** 2, y ** 2, z ** 2]).T

# Forming a vector containing only entries of ones, we make the size of this vector equal to the length of x
O = np.ones(len(x))

# Using the least square solver in numpy, this will return the solution to Ax=B
# We define B to be the vector of the parameters of the ellipsoid which we will solve for
B, resids, rank, s = np.linalg.lstsq(A, O, rcond=None)

# Here we are solving for a, b, c (where a, b, c are the coefficents which respectivley divide x^2, y^2 and z^2
# in the equation of a sphere/ ellipsoid
# This just involves a rearrangement by square-rooting 1/the first component in B vector to get a,
# square-rooting 1/the second component in B vector to get b, and then square-rotting 1/the third component in B to get vector b
a = np.sqrt(1 / B[0])
b = np.sqrt(1 / B[1])
c = np.sqrt(1 / B[2])

# Printing the values of a, b and c
print(a, b, c)

print(x)
