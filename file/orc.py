#Open, read and close file

f = open("demo.txt", "r")

data = f.read()
print(data)
print(type(data))
f.close()