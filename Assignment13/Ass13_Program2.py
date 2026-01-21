#WAP which accepts Radius of Circle and prints area of circle.
def CircleArea(Radius,PI=3.141592):
    return PI*Radius**2
def main():
    print("Enter the Radius of Circle : ")
    r=float(input())

    Area=CircleArea(r)
    print("Area of Circle is : ",Area)

if __name__=="__main__":
    main()