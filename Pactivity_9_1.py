'''
Problem -I 
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

Violet 380 to less than 450
Blue 450 to less than 495
Green 495 to less than 570
Yellow 570 to less than 590
Orange 590 to less than 620
Red 620 to 750

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.
'''

# Define wavelength ranges and corresponding colors
color_ranges = [(380, 450, "Violet"), 
                (450, 495, "Blue"), 
                (495, 570, "Green"), 
                (570, 590, "Yellow"), 
                (590, 620, "Orange"), 
                (620, 750, "Red")]

# Prompt user to enter wavelength
wavelength = float(input("Enter wavelength in nanometers (nm): "))

# Check if wavelength is within visible spectrum
if wavelength < 380 or wavelength > 750:
    print("Error: Wavelength is outside of the visible spectrum!")
else:
    # Determine color based on wavelength range
    for range_min, range_max, color in color_ranges:
        if range_min <= wavelength < range_max:
            break

    # Print the color corresponding to the wavelength
    print(f"The color corresponding to {wavelength} nm is {color}.")
