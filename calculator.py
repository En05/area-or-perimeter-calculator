equation = input("would you like the Perimeter or Area of your rectangle in CM?")

#if equation is area
if equation == ("Area") :


    Validheight = False
    while Validheight == False:
        try:
            height = input("What is the height of your rectangle?")
            height = float(height)
            if height>0:
                Validheight = True
        except:
            print("sorry, the height must be an integer!")




    Validwidth = False
    while Validwidth == False:
        try:
            width = input("What is the width of your rectangle?")
            width = float(width)
            if width>0:
                Validwidth = True
        except:
            print("sorry, the width must be an integer!")



    area = (float(height)*float(width))
    print(area,"units^2")


#if equation is perimeter
elif equation == "Perimeter":
    equation = "Perimeter"




    Validheight = False
    while Validheight == false:
        try:
            height = input("what is the height of your rectangle?")
            height = float(height)
            if height>0:
                Validheight = True
        except:
            print("Sory, The height must be an integer!")



    Validwidth = False
    while Validwidth == False:
        try:
            width = input("What is the width of your rectangle?")
            width = float(width)
            Validwidth = True
        except:
            print("sorry! the width must be an integer.")


    preperimeter = (float(height+width))
    perimeter = (preperimeter**2)
    print(perimeter)

#if neither
else:
    print("please ensure you have selected a valid choice!")
