#(1.) PYTHON PROGRAM TO FIND AREA OF CIRCLE

rad=float(input("Input radius of circle: "))
area=3.1415*rad*rad
print("The Area of Circle with radius " + str(rad) + " is = " + str(area))


#(2.) PROGRAM TO ACCEPT FILENAME FROM USER & PRINT ITS EXTENSION

filename=str(input("Input the FileName: ")).split(".")
print("The Extension of File is: " + (filename[-1]))
