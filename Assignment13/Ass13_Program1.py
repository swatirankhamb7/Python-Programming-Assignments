#WAP which accepts length and width of rectangle and prints area.
def AreaRectangle(Length,Width):
    return Length*Width
def main():
    print("Enter the length of Rectangle : ")
    len=float(input())

    print("Enter the width of Rectangle : ")
    wid=float(input())

    Area=AreaRectangle(len,wid)
    print("Area of Rectangle : ",Area)

if __name__=="__main__":
    main()