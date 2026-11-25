students = ["aarav","aaryan","arnav","shravan","aasharay"]
marks = [78,89,56,98,76]
gradebook = dict(zip(students,marks))
topper = max(str(students),int("marks"))


lowest = min(str(students),int("marks"))


avg = sum(marks) / len(marks)

input = str(input("Enter A Student Name : "))


if input == students:
    print(students)

else:
    print("Invalid!")

print("========SUMMARY========")
print("lowest",lowest)
print("topper",topper)
print("Average",avg)
print("========================")





