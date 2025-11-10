#w -> overwrite
#a -> append. add the new line in the end.

f = open("writee.txt", "w")

f.write("Go studyyyyy....")

f.close()

f = open("writee.txt", "a")

f.write("hehehehehe...")

f.close()

# if the file is not present, it will create a new file. 
f = open("sample.txt", "a")
#f = open("sample.txt", "w")
f.close()

