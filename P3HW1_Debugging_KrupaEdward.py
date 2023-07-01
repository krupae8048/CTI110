# CTI-110
# P3HW1_Debugging
#KrupaEdward
#27June2023


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]
# TO DO: determine lowest, highest , sum and average for grades

print ("-"*12, "Results", "-"*12)
low = min(grades)
high = max(grades)
sum_grades = sum(grades)
avg = sum(grades) / len(grades)

print("Lowest Grade: ", low)
print("Highest Grade: ", high)
print("Sum of Grades: ", format(sum_grades, ',.2f'))
print("Average: ", format(avg, ',.2f'))
print("-"*38)
# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')

    
elif avg > 80:
    print('Your grade is: B')


elif avg > 70:
    print('Your grade is: C')


elif avg > 65:
    print('Your grade is: D')

elif avg < 64:
    print('Your grade is: F') # TO DO: finish this





