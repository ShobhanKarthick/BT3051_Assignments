import numpy as np

r = input("Enter the radius: ")  # Get radius from the user
try:
    r=int(r)
except:
    print ("Enter valid radius")
    raise SystemExit

def circle_sqaure():
    circleArea = np.pi*r**2      # Calculate circle area
    squareArea = 4*r*r           # Calculate smallest square area outside the circle 
    return [circleArea, squareArea]

def sphere_cube():
    sphereVolume = (4/3)*(np.pi)*(r**3)     # Calculate sphere volume
    cubeVolume = 8*(r**3)                   # Calculate smallest cube volume outside the sphere
    return [sphereVolume, cubeVolume]

circleArea, squareArea = circle_sqaure()
sphereVolume, cubeVolume = sphere_cube()

print("Circle area is " + str(circleArea))
print("Sqaure area is " + str(squareArea))
print("Sphere volume is " + str(sphereVolume))
print("Cube volume is " + str(cubeVolume))
