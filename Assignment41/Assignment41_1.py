import math
def EucDistance(P1,P2):
    Ans=math.sqrt(((P2['X']-P1['X'])**2)+((P2['Y']-P1['Y'])**2))
    return Ans

def KNearestNeighbor():
    Border="-"*40
    Data=[
        {'point':'A','X':1,'Y':2,"label":"Red"},
        {'point':'B','X':2,'Y':3,"label":"Red"},
        {'point':'C','X':3,'Y':1,"label":"Blue"},
        {'point':'D','X':6,'Y':5,"label":"Blue"},
    ]

    print(Border)
    print("Dataset For Traning : ")
    print(Border)
    for i in Data:
        print(i)
    print(Border)
    print(Border)

    New_point={}
    no_of_elements=2

    for i in range(0,no_of_elements):
        key=input("Enter the Key : ")
        Value=int(input(f"Enter {key} Coordinate : "))
        New_point[key]=Value
    print("Elements of new Point to calculate Distance : ")
    print(New_point)
    print(Border)

    print("Euclidian Distence of Each point with respect to Another Point : ")
    print(Border)

    for i in Data:
        i["Distance"]=EucDistance(i,New_point)

    for i in Data:
        print(i)
    print(Border)
    print(Border)
    print("Sorted Distances : ")
    print(Border)
    sorted_data=sorted(Data,key=lambda item:item["Distance"])
    for i in sorted_data:
        print(i)
    print(Border)
    print(Border)
    print("Nearest Neighbors are : ")
    k=3
    nearest_point=sorted_data[:k]
    for i in nearest_point:
        print(i)
    print(Border)
    print(Border)

    Votes={}

    for neighbor in nearest_point:
        label=neighbor["label"]
        Votes[label]=Votes.get(label,0)+1

    print("Measority Count of Each Label As follows : ")
    for d in Votes:
        print("Name : ",d,"Number : ",Votes[d])
    print(Border)
    print(Border)
    print("Predicted Class: ")
    print(Border)
    predicted_class=max(Votes,key=Votes.get)
    print(f"Predcited Class For Point is :({New_point['X']},{New_point['Y']}) is ",predicted_class)



def main():
     KNearestNeighbor()


if __name__=="__main__":
    main()