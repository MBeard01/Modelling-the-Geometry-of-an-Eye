# IMPORTANT INFORMATION!
# You must have stlwrite, a handwritten module, saved in the same directory as Ellipsoid STL in order for it to work



"""
    Importing the libraries that we need for this program, in this case we will need the math module and the
    stlwrite module which is saved in the same directory. stlwrite Is not a library on Python, it is a handwritten module
"""
import math                        # The math library is needed to use sin, cos and pi
import stlwrite as stl             # stlwrite is called, which should be saved in the same directory
PI = math.pi






""" 
    Defining frange, which we will need for iterating within the parameters defined in this function
    It means that we will only iterate though x while it is less than the maximum number of steps defined
    We define a counter for step too, so that we can count how many steps there are in the iterations, and add one
    each time that we iterate 
"""

def frange(x, maximum, step):
    while x < maximum:
        yield x
        x += step                   # Step counter for keeping track of how many iterations have been done





"""
   Defining get_ellipsoid which will take the parameters A, B, C, x0, y0, z0 (if not at origin then x0, y0, z0 will not
   be 0)
   We create an empty list for faces, which we can add entries to 
   The centre is defined as (x0, y0, z0), which may or may not be the origin
   theta_step and phi_step are defined, which can be changed depending on what the difference in theta and phi is
   desired to be after each iteration
"""

def get_ellipsoid(A,B,C,x0,y0,z0):
    faces = []                     # Creating an empty list of faces
    center = (x0, y0, z0)          # Defining the center as being the coordinate (x0, y0, z0)
    theta_steps = PI / 100         # Defining the size of theta steps, the smaller it is, the more iterations there will be
    phi_steps = PI / 100           # Defining the size of phi steps, the smaller it is, the more iterations there will be

    """
       This for loop will iterate the points given a range
       It will use the information from the frange defined previous, and will calculate the points using the equations
       of an ellipsoid, and adding the difference in theta each time within the equations
       This can be acheived by using a nested loop
    """
    # Defining the range of theta values, it must be between 0 and 2pi, going up in steps of theta_steps
    for theta in frange(0, 2 * PI, theta_steps):
        # Defining the range of phi values, it must be between -pi/2 and pi/2, going up in steps of phi_steps
        for phi in frange(-PI/2, PI/2, phi_steps):

            # Calculating the first point, by using the parametric equations of an ellipsoid
            point_one = (x0 + A * math.cos(theta) * math.cos(phi), y0 + B * math.sin(theta) *
                         math.cos(phi), z0 + C * math.sin(phi))

            # Calculating the next point, by using the parametric equations of an ellipsoid, adding theta step and
            # phi step to each of them
            point_two = (x0 + A * math.cos(theta + theta_steps) * math.cos(phi+phi_steps), y0 + B *
                         math.sin(theta + theta_steps) * math.cos(phi+phi_steps), z0 + C * math.sin(phi+phi_steps))

            # Appending the points to the faces list, startin with the centre and then the iterated points
            faces.append([center, point_one, point_two])
    return faces





""" 
    Here we define example_ellipsoid, with a number of intentions.  First being that we create an STL file from the code.
    Next being that we can write this file, using the ASCII STL writer, where we then input the parameters we desire
    into the get_ellipsoid defined previous. These are user inputted, so can be whatever is desired.  Finally we print 
    'Wrote' followed by the file name, to get confirmation that the file has been written
"""
def example_ellipsoid():
    # Naming the file ellipsoid, this can be changed as desired, making sure it is .stl so that it saves as an stl file
    filename = 'ellipsoid.stl'

    # Here we are using the stil ASCII writer, which we call from the stl writer document
    with open(filename, 'wb') as fp:
        writer = stl.ASCII_STL_Writer(fp)
        writer.add_faces(get_ellipsoid(100, 80, 80 , 0, 0, 0))
        writer.close()
    print('Wrote ' + filename)





"""
    This boiler plate code is important because we are importing from an externally created programme
    We need this because otherwise the importing module would all be run before this module, which could be a problem
"""

if __name__ == '__main__':
    example_ellipsoid()