# USING GEOMDL FOR SURFACE FITTING

"""
    This programme is going to make use of 'geomdl' a Python library. This is a pure Python, object-oriented B-spline
    and NURBS library. It is useful for us to use because it works on the principle of curve and surface-fitting via
    interpolation and least squares approximation. All you need to do to achieve the plot using this programme is to
    input the points which you have to fit the surface to.
"""

# Importing the necessary libraries

from geomdl import construct                   # The construct module in the geomdl library will be used
from geomdl import fitting                     # The fitting part of the geomdl library will be needed
from geomdl.visualization import VisMPL as vis # Visualization will be needed for visualizing the surface





# Inputting the data set that you have
points =                                       # Here you input the points that you have to fit the surface to
size_u = 5                                     # The number of points in the u-direction
size_v = 7                                     # The number of points in the v-direction
degree_u = 2                                   # The degree of the output surface for the u-direction
degree_v = 3                                   # The degree of the output surface for the v-direction





# Do global surface approximation, which approximates the surface using least squares method with a fixed number of
# control points
# It uses an algorithm to interpolate the corner control points, and approximates the remaining control points
surf = fitting.approximate_surface(points, size_u, size_v, degree_u, degree_v)







# Extract curves from the approximated surface
surf_curves = construct.extract_curves(surf)
plot_extras = [
    dict(
        points=surf_curves['u'][0].evalpts,
        name="u",                              # This refers to the u-direction, you can change the name as appropriate
        color="cyan",                          # Change the colours according to that desired
        size=5                                 # Change the colour of the curves according to the thickness desired
    ),
    dict(
        points=surf_curves['v'][0].evalpts,
        name="v",                              # This refers to the v-direction, you can change the name as appropriate
        color="magenta",                       # Change the colours according to that desired
        size=5                                 # Change the colour of the curves according to the thickness desired
    )
]






# Plot the interpolated surface
surf.delta = 0.05
surf.vis = vis.VisSurface()
surf.render(extras=plot_extras)
