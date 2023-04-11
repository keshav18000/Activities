'''
Complete the Exercises - Representing Abstraction Through Code 
In programming, we deal with two kinds of elements: functions and data. 

Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. 

By the concept of abstraction create functions representing abstracting principles through function 

Think and design a user-defined function that should provide the result by mare passing few arguments by the calling function.
Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
Factor:  Calculate temperature that a person feels because of the wind (Python3)
Note: Naming Convention Files: Crate files based on the purpose of the exercise eg: If calculating factor then use function_factor.py  Submission Guidelines: File Upload (Notepad File, Python File, Console Output Pasted) 
'''

# Arithmetic function
def perform_arithmetic(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

# Conversion function
def perform_conversion(value, unit):
    if unit == 'miles':
        return value * 1.60934
    elif unit == 'pounds':
        return value * 0.453592
    elif unit == 'inches':
        return value * 2.54
    else:
        return "Invalid unit"

# Earthquake impact function
def calculate_earthquake_impact(magnitude, distance):
    return magnitude * (10 ** (1.5 * magnitude - 4.5)) / (distance ** 2)

# Wind chill factor function
def calculate_wind_chill(temp, wind_speed):
    return 35.74 + 0.6215 * temp - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp * (wind_speed ** 0.16)
