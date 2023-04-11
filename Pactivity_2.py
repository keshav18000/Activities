'''
Complete the Following Exercises.
You are free to use any IDE.

Steps Involved:
1. Understand a Problem (Make it clear through Instructor)

2. Understand Inputs

3. Understand Output 

4.Understand the Constraints

5.Code 

6. Validate  

 

Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
Factor:  Calculate temperature that a person feels because of the wind (Python3)
Note: Naming Convention Files: Crate files based on the purpose of the exercise eg: If calculating factor then use factor.py  
'''

#Arithmetic
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operations = {"Addition": a + b,
              "Subtraction": a - b,
              "Multiplication": a * b,
              "Division": a / b,
              "Modulus": a % b}

for operation, result in operations.items():
    print(f"{operation}: {result}")


#Conversion
num = float(input("Enter a number: "))
unit = input("Enter the unit of measurement for the number: ")
target_unit = input("Enter the unit of measurement to convert to: ")

factors = {"feet": 0.3048, "miles": 1609.34, "inches": 0.0254}

if unit in factors and target_unit in factors:
    converted_num = num * factors[unit] / factors[target_unit]
    print(f"{num} {unit} is equal to {converted_num} {target_unit}")
else:
    print("Unsupported unit conversion")



#Earthquake Impact
magnitude = float(input("Enter the magnitude of the earthquake: "))

impact = 10**(1.5*magnitude - 5.75)

print("The potential impact of the earthquake is", impact)



#Factor
wind_speed = float(input("Enter the wind speed in miles per hour: "))
temperature = float(input("Enter the temperature in degrees Fahrenheit: "))
factor = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16
print(f"The wind chill factor is {factor} degrees Fahrenheit.")
