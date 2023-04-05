# Modelling the Geometry of an Eye
This is an example of a project I worked on, involving developing some code to model the geometry of the eye by fitting data to an ellipsoid. I worked on initial objectives for this (where no data was available), with the aim that researchers in the department would develop this further (when real data involving MRI scans of the eye become available).

Initially this involved developing some code to model an ellipsoid, where the user can input various parameters. This piece of code then plots the ellipsoid in three-dimensions, and uses a 'camera' to allow the user to navigate around the model.

To progress this further, there is additional modifications to this which take into account some fake data. The aim of this is to generate 'noise' to make the ellipsoid model more accurate to something we would expect when actually working with real data involving the eye. In order to generate this random data, we use a standard normal distribution.

Consideration was then taken about how we could convert the ellipsoid model over to STL (Standard Tessellation Language), which would provide opportunity for 3D printing, and further converting the model over to MatLab. In order to do this, you will see a completely different program for the ellipsoid, because there were no clear-cut convertors for a Python model.

Then to develop a more accurate model which would better reflect what we can expect for the eye, the Geomdl library was used. This would allow the plotting of a surface, when points are fed into it, by using the method of interpolation.
