import pandas as pd 
import math
data = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/Standard_deviation/master/graphs/class1.csv")
marks = data["Marks"].tolist()
sum = 0
for i in marks :
    sum = sum+i 
mean = sum/len(marks)

squares = []
for i in marks :
    x = i-mean
    x = x**2
    squares.append(x)

sum = 0
for i in squares :
    sum = sum+i 

result = sum/(len(marks)-1)
sd = math.sqrt(result)

print(sd)

import statistics
print (statistics.stdev(marks))
