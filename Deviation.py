import csv 
import math

with open("random.csv",newline='') as f :
    read = csv.reader(f)
    fileData = list(read)

data = fileData[0]

n = len(data)

sum = 0
for i in data :
    sum += int(i)

mean =  sum/n

print("The mean is ",mean)

squareList = []

for i in data :
    x = int(i) - mean
    x = x ** 2
    squareList.append(x)

total = 0

for x in squareList :
    total += x

result = total/(n-1)

stdev = math.sqrt(result)
print("whatever this is idk why u wanted this but here this stupid value :",stdev)