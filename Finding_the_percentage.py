student_marks = {}
for _ in range(int(input())):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
avg=sum(student_marks[query_name])/3
print("%.2f"%avg)