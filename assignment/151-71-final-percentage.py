import io

file = io.FileIO('./final.txt')


lines = list(file.readall().splitlines())

marks = list(map(int, lines))


avg = sum(marks) / len(marks)

above_avg = 0

for mark in marks:
    if mark > avg:
        above_avg += 1

percentage_above_avg = above_avg / len(marks) * 100
print(f"Number of grades: {len(marks)}")
print(f"Average grade: {avg:.2f}")
print(f"Percentage of grades above average: {percentage_above_avg:.2f}%")
