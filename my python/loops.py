# count=0
# mynumber=19
# while(count<mynumber):
#     print(f"counts value is{count}")
#     count+=1

# for loop
# number = [1,2,3,4,5,]

# for no in number:
#     if (no > 3):
#       print(no *4)


students =[
    {"name": "cheta","result": 80},
    {"name": "miami","result": 90},
    {"name": "jite","result": 100},
    {"name": "emma","result": 100}
]
total=0

for student in students:
    total+=student["result"]
    print(total)
mean = total / len(students)
print(mean)