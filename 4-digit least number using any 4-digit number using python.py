""" Question of this assignment:-
If the user gives a 4-digit number and asks the least 4-digit number.
For example By General Mathematics:-If a number 4391 is a 4-digit number, then convert it into 
least 4- digit numbers using the given number .The answer is "1349" """

print("+++++Least 4-digit generator using any 4-digit Number+++++")

#Here we are usimg Python to do the sum by using any 4-digit number.
enter_4_digit_number =input("ENTER 4-digit number:- ")
if len(enter_4_digit_number)==4:

    least_4_digit_number=""

    for i in "0123456789":
        for j in enter_4_digit_number:
            if i == j:
                least_4_digit_number = least_4_digit_number + j

    print("Least 4-digit number is:", least_4_digit_number)

else:
    print("xxxPlease enter a valid 4-digit number.xxx")



print("THANKYOU FOR USING 4_DIGIT LEAST GENERATOR. :) ")
print("< MADE BY UVK >")



