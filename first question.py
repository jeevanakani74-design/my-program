def analyze_result(name, roll, marks):

    print(f"Student: {name} (Roll: {roll})")

    total = sum(marks)
    average = total / len(marks)

    print(f"Total: {total}")
    print(f"Average: {average:.1f}")

    # Grade Calculation
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print(f"Grade: {grade}")

    # Subjects below 40
    print("Subjects below 40:")

    found = False

    for i in range(len(marks)):
        if marks[i] < 40:
            print(f"Subject {i + 1}")
            found = True

    if not found:
        print("None")


# Main Program
name = "Aarav"
roll = 101
marks = [88.5, 35.0, 76.0, 92.5, 48.0]

analyze_result(name, roll, marks)
