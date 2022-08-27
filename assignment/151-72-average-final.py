n = 5

marks = [0] * n

for x in range(n):
    marks[x] = int(input("Enter one of five grades: "))

marks.sort()

marks.remove(marks[0])
marks.remove(marks[0])

avg = sum(marks) / len(marks)


print(f"Average grade: {avg:.2f}")
