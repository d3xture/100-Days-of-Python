student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


# student_heights = [180, 124, 165, 173, 189, 169, 146]

#length
count = 0
for students in student_heights:
    count += 1
print(f"The length is: {count}") 

#sum

total_height = 0

for height in student_heights:
   total_height += height
print(f"The sum is: {total_height}")

average = round(total_height / count)

print(f"The average is: {average}")

