N=int (input("Enter the number of students: "))
marks=[]
valid_count=0
fail_count=0
for i in range(N):
    marks.append(int(input("Enter the marks: ")))
for mark in marks:
    if mark >= 90 and mark <= 100:
        valid_count+=1
        print(mark,"-> Excellent")
    elif mark >= 75 and mark <= 89:
        valid_count+=1
        print(mark,"-> Very Good")
    elif mark >= 60 and mark <= 74:
        valid_count+=1
        print(mark,"-> Good")
    elif mark >= 40 and mark <= 59:
        valid_count+=1
        print(mark,"-> Average")
    elif mark >= 0 and mark <= 39:
        valid_count+=1
        fail_count+=1
        print(mark,"-> Fail")
    else:
        print(mark,"-> Invalid")

print("Total Valid students:",valid_count)
print("Total Failed students:",fail_count)