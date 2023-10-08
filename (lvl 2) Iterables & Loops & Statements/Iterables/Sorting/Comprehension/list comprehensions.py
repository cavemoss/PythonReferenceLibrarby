# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list comprehensions

squares = []
for i in range(1, 11):
    squares.append(i*i)
print(squares)

squares = [i*i for i in range(1, 11)]
print(squares)

student_results = [100, 90, 80, 70, 60, 50, 40, 30, 0]

passed_students = list(filter(lambda x: x >= 60, student_results))
print(passed_students)

passed_students = [i for i in student_results if i >= 71]
print(passed_students)

passed_students = [i if i >= 40 else 'FAILED' for i in student_results]
print(passed_students)
