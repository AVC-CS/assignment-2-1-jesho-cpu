def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
# Input the number of males and females
num_males = int(input("Enter the number of males: "))
num_females = int(input("Enter the number of females: "))

# Calculate the total number of students
total_students = num_males + num_females

# Calculate the percentage of males and females
m_perc = (num_males / total_students) * 100
f_perc = (num_females / total_students) * 100

# Print the results
print("The total number of students:", total_students)
print("The number of males and females:", num_males, num_females)
print("The percentage of males and females: {:.2f}% {:.2f}%" .format(m_perc, f_perc))
"""
    ########################################
    # Do not delete the return statement
    ########################################
    
return m_perc, f_perc
"""

if __name__ == '__main__':
    main()
