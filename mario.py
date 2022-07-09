

height = int(input("Please Enter the Height of the Pyramid to be Printed (Range 1 to 60): "))

while height > 60 or height < 1:
    print("User Input is not within the Valid Range (1 to 23), Please enter a valid height:")
    height = int(input("Please Enter the Height of the Pyramid to be Printed (Range 1 to 60): "))

if height == 1:
    print("#  #")

else:
    for i in range(0,height,1):

        for j in range (0, (height-i), 1):
            print(" ", end="")

        for k in range(i+1):
            print("#", end="")

        print("  ", end="")

        for l in range(i+1):
            if l == i:
                print("#")
            else:
                print("#", end="")