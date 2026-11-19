# 1)
f = open("data.txt","w")

f.write("Hello Python")
f.close()

print("Data written successfully")

# 2)
f = open("data.txt","r")

print(f.read())

f.close()

# 3)
f = open("data.txt","a")
f.write("\n Welcome to Python")
f.close()
print("Data appended successfully")
 
# 4)

with open("data.txt","r") as f:
    for line in f:
        print(line.strip())
    
# 5)

fruits = ["Apple","Mango","Banana"]

with open("fruits.txt","w") as f:
    f.write(",".join(fruits))
    
with open("fruits.txt","r") as f:
    data = f.read().split(",")
    
print(data)

# 6)

data = bytes([76,108,108,111,101])

with open("data.bin","wb") as f:
    f.write(data)

with open("data.bin","rb") as f:
    print(f.read())
    
# 7)

with open("data.bin","rb") as src:
    with open("copy.bin","wb") as dst:
        dst.write(src.read())
        
print("File copied succecfully")

employees = ["mayank","manav","hemangi","nisita"]

file_path = "output.txt"
try:
    with open(file_path,"a") as file:
        for employee in employees:
            file.write("\n"+employee)
        print(f"txt file '{file_path}' was created")
    
except FileExistsError:
    print("That file already exists!")
