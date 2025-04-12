with open("go.txt") as a:
    data1=a.read()

with open("bow.txt") as m:
    data2=m.read()

data1+="\n"
data1+=data2

print("merging the file.......")

with open("done.txt","w") as f:
    f.write(data1)
