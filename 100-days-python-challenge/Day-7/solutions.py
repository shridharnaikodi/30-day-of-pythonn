names = ["Rahul", "Amit", "Sneha", "Priya"]

for index, name in enumerate(names):
    print(index, name)














names = ["Rahul", "Amit", "Sneha"]
marks = [85, 72, 91]

result = dict(zip(names, marks))

print(result)
















def check_marks(marks):

    any_failed = any(mark < 40 for mark in marks)
    all_passed = all(mark >= 40 for mark in marks)

    print("Any failed:", any_failed)
    print("All passed:", all_passed)


marks = [78, 85, 92, 67, 88]

check_marks(marks)