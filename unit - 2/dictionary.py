emp = {
"E101": {"name": "Amit", "dept": "IT", "salary": 55000,
"skills": ["Python", "SQL"],
"contact": ("9998887001", "amit@company.com")},
"E102": {"name": "Bela", "dept": "HR", "salary": 48000,
"skills": ["Recruiting", "Excel"],
"contact": ("9998887002", "bela@company.com")},
"E103": {"name": "Chirag", "dept": "IT", "salary": 62000,
"skills": ["Python", "Java", "AWS"],
"contact": ("9998887003", "chirag@company.com")},
"E104": {"name": "Divya", "dept": "Finance", "salary": 51000,
"skills": ["Excel", "SAP"],
"contact": ("9998887004", "divya@company.com")},
"E105": {"name": "Esha", "dept": "IT", "salary": 58000,
"skills": ["Python", "Django"],
"contact": ("9998887005", "esha@company.com")},
}

# Queries:
# 1. Print the full record of employee "E103".
print(emp["E103"])
# 2. List the names of all employees in the "IT" department.
for k,v in emp.items():
    if v["dept"] == "IT":
        print(v["name"],"=",v["dept"])
# 3. Find and print the name of the employee with the highest salary.
mx = 0
for k,v in emp.items():
    if v["salary"] > mx:
        mx = v["salary"]
print(v["name"],"=", mx)
# 4. Print the email address (from the contact tuple) of employee
# "E102".
print(emp["E102"]["name"],"number is:","=", emp["E102"]["contact"][0])
print(emp["E102"]["name"],"email is :","=",emp["E102"]["contact"][1])
# 5. Count how many employees have "Python" listed in their skills.
for v in emp.values():
    if "Python" in v["skills"]:
        print(v["name"],"=",v["skills"])
# 6. Give employee "E104" a 10% raise — update their salary in place
# and print the updated record.
emp["E104"]["salary"]=emp["E104"]["salary"]+emp["E104"]["salary"]*0.10
print(emp["E104"])

stud = {
"S1": {"name": "Amit", "age": 16,
"marks": {"Math": 85, "Science": 90, "English": 78},
"guardian": ("Mr. Sharma", "9998887777")},
"S2": {"name": "Bela", "age": 15,
"marks": {"Math": 92, "Science": 88, "English": 95},
"guardian": ("Mrs. Verma", "9998888888")},
"S3": {"name": "Chirag", "age": 16,
"marks": {"Math": 65, "Science": 70, "English": 60},
"guardian": ("Mr. Patel", "9998889999")},
"S4": {"name": "Divya", "age": 14,
"marks": {"Math": 88, "Science": 91, "English": 84},
"guardian": ("Mrs. Rao", "9998880000")},
}

# # Queries:
# # 1. Print student "S2"’s marks in Science only.
# print(stud["S2"]["marks"]["Science"])
# # 2. Print the guardian’s name and phone number (the tuple) for
# # student "S3".
# print(stud["S3"]["guardian"][0],stud["S3"]["guardian"][1])
# # 3. Calculate and print each student’s total marks (sum of all 3
# # subjects).
# for k,v in stud.items():
#     total=sum(v["marks"].values())
#     print(k,v["name"],total)
# 4. Find and print the name of the student with the highest total
# marks.
# mx = 0
# l = []
# name = ""
# for k,v in stud.items():
#     total = sum(v["marks"].values())
#     l.append(total)
#     print(l)
#     for i in range(total + 1):
#         if i > mx:
#             mx = i
#             name = v["name"]
# print(name,"mark:",mx)
# l = []
# mx = 0
# name = ""
# for k,v in stud.items():
#     l.append(sum(v["marks"].values()))
#     print(l)
#     for i in range(len(l)):
#         if l[i] > mx:
#             mx = l[i]
#             name = v["name"]
#     print(name,":",mx)


# 5. List the names of all students who scored above 80 in Math.
l = []
for k,v in stud.items():
      if v["marks"]["Math"] > 80:
          print(v["name"],v["marks"]["Math"])
# 6. Add a new subject, "Computer": 95, to student "S1"’s marks
# dictionary.

stud["S1"]["marks"]["computer"] = "95"
print(stud["S1"])

prod = {
"P001": {"name": "Laptop", "price": 55000, "category":"Electronics",
"tags": ["computer", "portable"],"specs": ("Intel i5", "8GB RAM", "512GB SSD")},
"P002": {"name": "Office Chair", "price": 7500, "category":"Furniture",
"tags": ["ergonomic", "adjustable"],"specs": ("Mesh back", "Adjustable height", "360-degree swivel")},
"P003": {"name": "Smartphone", "price": 22000, "category":"Electronics",
"tags": ["mobile", "5G"],"specs": ("6.5-inch display", "128GB storage",
"5000mAh battery")},"P004": {"name": "Study Table", "price": 4200, "category":
"Furniture","tags": ["wooden", "compact"],"specs": ("120x60 cm", "Engineered wood", "2drawers")},
"P005": {"name": "Headphones", "price": 3000, "category":
"Electronics","tags": ["wireless", "noise-cancelling"],
"specs": ("Bluetooth 5.0", "30-hour battery", "Over-ear")},
}

# 1. Print the specs (the tuple) of product "P003".
print(prod["P003"]["specs"][0])
print(prod["P003"]["specs"][1])
# 2. List the names of all products in the "Electronics" category.
l = []
for k,v in prod.items():
    if v["category"] == "Electronics":
        l.append(v["name"])
print(l)
# 3. Find and print the name of the cheapest product overall.

name = ""
l = []
mn = 9999
for k,v in prod.items():
    l.append(v["price"])
    print(l)
    for i in range(len(l)):
        if l[i] < mn:
            mn = l[i]
            name = v["name"]
print(name,":",mn)
# 4. Print all the tags of product "P002".
print(prod["P002"]["tags"])
5. Count how many products are priced above Rs. 5000.
count = 0
l = []
l2 = []
count = 0
for k,v in prod.items():
      l.append(v["price"])

for j in range(len(l)):
      if l[j] > 5000:
            l2.append(l[j])
            count += 1
print(l2)
print("The total product above 5000 is :",count)
# 6. Apply a 15% discount to product "P001" — update its price in place
# and print the new price.
dis = (prod["P001"]["price"]-prod["P001"]["price"]*0.15)
prod["P001"]["price"] = dis
print(prod["P001"])