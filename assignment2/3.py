# Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error message. If the score is between 0.0
# and 1.0, print a grade using the following table:
# &gt;= 0.9 A
# &gt;= 0.8 B
# &gt;= 0.7 C
# &gt;= 0.6 D
# &lt; 0.6 F

# Abhinav Agarwal
# Roll 01
# CSE - 2nd Year

score = float(input('Enter Score: '))
if score <= 0.6:
    print('Grade F')
elif score <= 0.7:
    print('Grade D')
elif score <= 0.8:
    print('Grade C')
elif score <= 0.9:
    print('Grade B')
elif score <= 1.0:
    print('Grade A')
else:
    print('Error')