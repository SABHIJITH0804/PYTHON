import numpy as n
import pandas as p
import matplotlib.pyplot as pd
df1=p.read_csv("D:\\my folder\\IP class 12\\PROJECT\\table 1\\top 10  batsman details.csv")
df2=p.read_csv("D:\\my folder\\IP class 12\\PROJECT\\table 2\\top 10 batsman.csv")
df3=p.read_csv("D:\\my folder\\IP class 12\\PROJECT\\table 3\\top 10 bowlers details.csv")
df4=p.read_csv("D:\\my folder\\IP class 12\\PROJECT\\table 4\\top 10 Bowler.csv")

print("IPL 2020 EDITION",end="\n\n")

print("Do you want to run queries based on a batsman list or bowler list ?",end="\n\n")
print("1 : Batsman")
print("2 : Bowler")
print(end="\n\n")
x=int(input("Enter your preference as 1 or 2 : "))
print(end="\n\n")

if x==1 :
    print("1 : Top 10 batsman")
    print("2 : Stats of particular batsman")
    print("3 : Top 3 batsman with the highest batting average in IPL 2020 edition")
    
    print("4 : Top 3 batsman most runs in IPL 2020 edition")
    print("5 : Graphical representation")
    print(end="\n\n")

    y=int(input("Enter your preference as the number assigned to your choice : "))
    print(end="\n\n")
    if y==1 :
        print(df1)
    elif y==2 :
        print("Stats of a particular batsman among the top 10,If the top 10 are :",end="\n")
        print("KL Rahul","Shikhar Dhawan","David Warner","Shreyas Iyer","Ishan Kishan",
              "Quinton de kock","Suryakumar Yadav","Devdutt Padikkal","Virat Kohli","AB de Villiers",sep="\n")
        print(end="\n\n")
        m=str(input("enter the name of the batsman : "))
        for p in range(len(df2)):
            if df2.at[p,"Name"]==m :
                k=p
        print(end="\n\n")
        print(df2.loc[k,],end="\n\n")
        print(m," plays for ",df1.at[k,"Team"])
    elif y==3 :
        m=df2.loc[:,"Avg"]
        n=m.sort_values(ascending=False)
        o=n.head(3).index
        print("Top 3 batsman with the highest batting average in IPL 2020 edition are")
        for i in o :
            print(df2.iat[i,1])
    elif y==4 :
        m=df2.loc[:,"Runs"]
        n=m.sort_values(ascending=False)
        o=n.head(3).index
        print("Top 3 batsman with the most runs in IPL 2020 edition are ")
        for i in o :
            print(df2.iat[i,1])
    elif y==5 :
        df2.plot(x="Name",y="Avg",kind="bar")
        pd.show()
        
        
        
if x==2 :
    print("1 : Top 10 bowler")
    print("2 : Stats of a particular bowler")
    print("3 : Graphical representation")
    print("4 : player with the best economy")
    print(end="\n\n")
    y=int(input("Enter your preference as the number assigned to your choice  : "))
    print(end="\n\n")
    if y==1 :
        print(df3)
    elif y==2 :
        print("Stats of a particular bowler among the top 10,If the top 10 are :",end="\n")
        print("Kagiso Rabada","Jasprit Bumrah","Trent Boult","Anrich Nortje","Yuzvendra Chahal",
              "Rashid Khan","Jofra Archer","Mohammed Shami","Varun Chakravarthy","T Natarajan",sep="\n")
        print(end="\n\n")
        m=str(input("enter the name of the bowler : "))
        for p in range(len(df4)):
            if df4.at[p,"Name"]==m :
                k=p
        print(end="\n\n")
        print(df4.loc[k,],end="\n\n")
        print(m," plays for ",df3.at[k,"Team"])
    elif y==3 :
        df4.plot(x="Name",y="Economy",kind="bar")
        pd.show()
    elif y==4 :
        b=df4.sort_values(by="Economy",ascending=True)
        a=b.head(1).index
        for x in a :
            print("player with the best economy",df4.loc[x,"Name"],sep="\n")
        
        
        
        



        
        
        






    










    

  
    

