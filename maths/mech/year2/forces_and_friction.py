#todo Get criteria completed; Angle, side of object force is being applied, the force (n), mass of object, push or pull

from sympy import *

# criteria
angle_of_force = float(input('What direction is the force being applied from: \t'))
strength_of_force = float(input('How many newtons is the force:\t'))
strength_of_friction = float(input('How much friction is present <<0 for smooth surface>>:\t'))
mass_of_object = float(input('What is the mass of the object:\t'))
side_of_force = input('What side is the force being applied from <<left/right>>:\t')
type_of_force = input('What type of force is it <<push/pull>>:\t')