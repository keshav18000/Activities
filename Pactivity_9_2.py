'''
Problem -II
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:
Radio Waves Less than 3 × 10^9
Microwaves 3 × 10^9 to less than 3 × 10^12
Infrared Light 3 × 10^12 to less than 4.3 × 10^14
Visible Light 4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
X-Rays 3 × 10^17 to less than 3 × 10^19
Gamma Rays 3 × 10^19 or more
Write a program that reads the frequency of some radiation from the user and
displays name of the radiation as part of an appropriate message.
'''

f = float(input("Enter Frequency: "))
if f < 3e9:
    print("Radio Waves")
elif 3e9 <= f < 3e12:
    print("Microwaves")
elif 3e12 <= f < 4.3e14:
    print("Infrared Light")
elif 4.3e14 <= f < 7.5e14:
    print("Visible Light")
elif 7.5e14 <= f < 3e17:
    print("Ultraviolet Light")
elif 3e17 <= f < 3e19:
    print("X-Rays")
else:
    print("Gamma Rays")