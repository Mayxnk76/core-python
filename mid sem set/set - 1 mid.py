# Set - 1 
# ------Q - 1------

def count_vowel_words(words):
    count = 0
    
    for word in words:
        if word[0].lower() in "aeiou":
            count += 1
            
    print("Word starting with vowels:",count)
    

def reverse_words(words):
    reverse_dict = {}
    
    for word in words:
        reverse_dict[word] = word[::-1]
        
    print("Revesed words dictionary:",reverse_dict)
    

def longest_shortest(words):
    longest = max(words,key = len)
    shortest = min(words,key = len)
    
    print("Longest word:",longest)
    print("Shortest word",shortest)
    
def words_more_than_four(words):
    print("Words having more than 4 characters:")
    
    for word in words:
        if len(word) > 4:
            print(word)
            
#main program

sentence = input("Enter a sentence:")

words = sentence.split()

count_vowel_words(words)
reverse_words(words)
longest_shortest(words)
words_more_than_four(words)
 
# ---------Q - 2---------

# Funstion 1: Accept medicine details

def accept_medicines():
    medicines = []
    
    for i in range(5):
        print("\n Enter detrails of medicine",i + 1)
        
        mid = input("Enter Medicine ID:")
        name = input("Enter Medicine Name:")
        price = float(input("Enter Price of unit:"))
        quantity = int(input("Enter Quantity:"))
            
        stock_value = price * quantity
        
        medicine = {
            "id":mid,
            "name":name,
            "price":price,
            "quantity":quantity,
            "stock_value":stock_value
            }
        
        medicines.append(medicine)
        
    return medicines

# Funstion 2: Save medicine details in file

def save_medicines(medicines):
    
    with open("medical_store.txt","w")as file:
        
        for medicine in medicines:
            file.write(
                f"{medicine['id']}|{medicine['name']}|"
                f"{medicine['price']}|{medicine['quantity']}|"
                f"{medicine['stock_value']}\n"
                )
    print("\n Medicine details saved succesfully!")
    
# Function 3:Read file and display reports
def display_report():
    medicines = []
    
    with open("medical_store.txt","r") as file:
        
        for line in file:
            data = line.strip().split("|")
            
            medicine = {
                "id":data[0],
                "name":data[1],
                "price":float(data[2]),
                "quantity":int(data[3]),
                "stock_value":float(data[4])
                
            }
                
            medicines.append(medicine)
                
    highest = medicine[0]
    total_value = 0
    
    print("\n-----MEDICAL STORE REPORT-----")
    
    for medicine in medicines:
        
        total_value += medicine["stock_value"]
        
        if medicine["stock_value"] > highest["stock_value"]:
            highest = medicine
            
        if medicine["quantity"] < 10:
            print("Low stock medicine:",medicine["name"])
            
    print("\nmedicine with highest stock value:")
    print(highest["name"],"=",highest["stock_value"])
    
    print("\n Total value of all medicines:",total_value)
    
#main function

def main():
    medicine = accept_medicines()
    save_medicines(medicine)
    display_report()
    
main()