import math
def EucDistance(P1,P2):
    Ans=math.sqrt(((P2['Study Hours']-P1['Study Hours'])**2)+((P2['Attendance']-P1['Attendance'])**2))
    return Ans

def KNearestNeighbor():
    Border="-"*40
    Data=[
        {'Study Hours':2,'Attendance':60,"Result":"Fail"},
        {'Study Hours':5,'Attendance':80,"Result":"Pass"},
        {'Study Hours':6,'Attendance':85,"Result":"Pass"},
        {'Study Hours':1,'Attendance':50,"Result":"Fail"},
        
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

    print("Euclidian Distance of Each point with respect to Another Point : ")
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
        Result=neighbor["Result"]
        Votes[Result]=Votes.get(Result,0)+1

    print("Measority Count of Each Label As follows : ")
    for d in Votes:
        print("Name : ",d,"Number : ",Votes[d])
    print(Border)
    print(Border)
    print("Predicted Class Output: ")
    print(Border)
    predicted_class=max(Votes,key=Votes.get)
    print(f"Predcited Class For Study Hours :{New_point["Study Hours"]} and Attendance : {New_point["Attendance"]} is ",predicted_class)
   



def main():
     KNearestNeighbor()


if __name__=="__main__":
    main()