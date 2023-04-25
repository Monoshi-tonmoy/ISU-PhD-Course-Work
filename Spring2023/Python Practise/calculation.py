import Shape
import convert

def main():

    bool=True

    while bool:
        option=int(input("Press 1 to use shape, 2 for conver and 3 to exit:\n"))

        if option==1:
            a=int(input("Side of the square?"))
            print("Area of the square is:"+str(Shape.square(a)))
        elif option==2:
            kg=int(input("Please input kg:\n"))
            print("Kg to pound is"+str(convert.kgtopound(kg)))
        elif option==3:
            bool=False
        else:
            print("Error Input, Please try agian:\n")

if __name__=="__main__":
    main()