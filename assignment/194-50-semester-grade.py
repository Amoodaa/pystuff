def semesterGrade(mid, final):
    total = (mid + (final * 2)) / 3

    if total >= 90:
        return 'A'
    if total >= 80:
        return 'B'
    if total >= 70:
        return 'C'
    if total >= 60:
        return 'D'
    return 'F'


mid = int(input("Enter grade on midterm: "))
if mid > 100:
    print("Mid is between 0-100")
    exit(-1)

final = int(input("Enter grade on final exam: "))
if final > 100:
    print("Final is between 0-100")
    exit(-1)

grade = semesterGrade(mid, final)
print(f"Semester Grade: {grade}")
