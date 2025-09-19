# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: John Blair
# Assignment Number: 2
# Due Date: 09/19/2025
# Purpose: Average scores in a file
from os.path import split

with open("Assignment2input.txt") as x:
    lines=x.read().splitlines()
    for i in lines:
        student=i.split(" ")
        sname=student[0]
        sscore1=float(student[1])
        sscore2=float(student[2])
        sscore3 = float(student[3])
        sscore4 = float(student[4])
        sscore5 = float(student[5])
        sscore6 = float(student[6])
        ssum=sscore1+sscore2+sscore3+sscore4+sscore5+sscore6
        savg=round(ssum/6,2)
        print(sname,savg)