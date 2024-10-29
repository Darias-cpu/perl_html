num=int(input("Enter number:"))

if num%2==0:
     print(f"{num} is an even number")

else:
     print(f"{num} is an odd number")

     #if some one can vote
age=int(input("Enter age:"))
if age>=18:
     print("you can vote")
else:
    print("you can not vote")

#grade students
marks=int(input("Enter marks:"))

if marks<=100 and marks>=80:
    print("you have an A")
elif marks<=79 and marks>=60:
    print("you have a B")
elif marks<=40 and marks>=59:
    print("you have a C")
elif marks==0 and marks<=58:
    print("you have failed")
else:
    print("Invalid marks entered")

