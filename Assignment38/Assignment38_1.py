
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    #1.
    df=pd.read_csv("student_performance_ml.csv")

    #For printing first 5 Records
    print("First Five Records : ")
    print(df.head())

    #For printing last 5 Records
    print("Last Five Records : ")
    print(df.tail())

    #For Showing no of rows and columns
    print("No of Rows and Columns : ")
    print(df.shape)

    #For list of column names 
    print("List of Columns : ")
    print(list(df.columns))

    #2.
    #No of Students :
    print("No of Students are : ",len(df))

    #Count of pass and fail students :
    counts=df["FinalResult"].value_counts()
    passed_count = counts.get(1)
    failed_count = counts.get(0)

    print(f"Number of passed students (1): {passed_count}")
    print(f"Number of failed students (0): {failed_count}")

    #3.
    print("Avg study Hours : ",df["StudyHours"].mean())
    print("Avg Attendance : ",df["Attendance"].mean())
    print("Maximum Previous Score : ",df["PreviousScore"].max())
    print("Minimum Sleep Hours : ",df["SleepHours"].min())

    #4.
    print("Pass Percentage : ",(passed_count/len(df))*100)
    print("Fail Students : ",(failed_count/len(df))*100)
    """
    Given dataset is not balanced the most measority if of passed students .
    Here 60% Students are pass and 40% students are fail
    """

    #5.
    """
    1.Yes Higher Study Hours increase the chance of passing.
    2.Yes Higher Attendance improves the Final Result.

    By observing the given dataset,
    For Students  Final Result Study Hours,Attendance,Assignment Completion and Sleep these factors are Affected.
    Students with Good Attendace,attendance,Assignmets Completion and good sleep hours are having ggod chances
    to pass
    Studens not with above things are having most Probability to fail
    """

    #6 . Histogram For Study Hours

    plt.hist(x=df["StudyHours"])
    plt.show()
    """It Helps to understand freqency of students lies between diff Study Hours """

    #7.Scatter Plot Study hours vs Previous Courses
    sns.scatterplot(x=df["StudyHours"],y=df["PreviousScore"],hue=df["StudyHours"])
    plt.grid()
    plt.show()

    #8.Boxplot For Attendance 
    sns.boxplot(x=df["Attendance"])
    plt.grid()
    plt.title("Boxplot For Attendance")
    plt.show()
    """
    In the Given dataset outliers are not present because given data is in specified range.
    """

    #9.
    """9. Create a plot showing relationship between AssignmentsCompleted and FinalResult.
     Explain your observation."""
    sns.scatterplot(x=df["AssignmentsCompleted"],y=df["FinalResult"],hue=df["AssignmentsCompleted"])
    plt.grid()
    plt.xlabel("Assignments Completed")
    plt.ylabel("Final Result")
    plt.title("Relationship between AssignmentsCompleted and FinalResult")
    plt.show()

    """
    By Observing the plot it is been observed that students who completed more than 5 
    assignmets are pass and less than that failed 
    """

    #10.
    """10. Plot SleepHours against FinalResult.
    Does sleeping more guarantee success? Explain."""
    sns.scatterplot(x=df["SleepHours"],y=df["FinalResult"],hue=df["SleepHours"])
    plt.grid()
    plt.xlabel("Sleep Hours")
    plt.ylabel("Final Result")
    plt.title("Relationship between Sleep hours and Final Result")
    plt.show()
    """ yes More than 6 hrs sleep enough to get the Success """


if __name__=="__main__":
    main()