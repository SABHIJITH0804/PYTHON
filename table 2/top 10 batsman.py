import pandas as pt
import matplotlib.pyplot as p
df=pt.read_csv("D:\\my folder\\IP class 12\\PROJECT\\table 2\\top 10 batsman.csv")
print(df)
df.plot(x="Name",y="Avg")
p.show()
