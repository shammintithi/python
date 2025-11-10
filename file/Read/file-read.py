"""1. 
f = open("demo.txt" , "r")
#data = f.read() #read entire file
#data = f.read(5) #read some characters

data = f.readline() #read one line at a time
print(data)
print(type(data))
f.close() 
*/"""


#2.
f = open("demo.txt" , "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()


#f = open("filename", "mode")-> filename = .txt, .docs... mode = r: read mode, w: write mode, a: append mode