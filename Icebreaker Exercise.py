[10:05 pm, 10/04/2023] Raman Pal: '''
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

wl = int(input("Enter the Wavelength: "))
if (380<=wl<450):
    print("Violet")
elif (450<=wl<495):
    print("Blue")
elif (495<=wl<570):
    print("Green")
elif (570<=wl<590):
    print("Yellow")
elif (590<=wl<620):
    print("Orange")
elif (620<=wl<750):
    print("Red")
else:
    print("Wavelength entered is outside of the visible spectrum")
Footer
[10:05 pm, 10/04/2023] Raman Pal: # Prompt user to enter wavelength
wavelength = float(input("Enter wavelength in nanometers (nm): "))

# Check if wavelength is within visible spectrum
if wavelength < 380 or wavelength > 750:
    print("Error: Wavelength is outside of the visible spectrum!")
else:
    # Determine color based on wavelength range
    if 380 <= wavelength < 450:
        color = "Violet"
    elif 450 <= wavelength < 495:
        color = "Blue"
    elif 495 <= wavelength < 570:
        color = "Green"
    elif 570 <= wavelength < 590:
        color = "Yellow"
    elif 590 <= wavelength < 620:
        color = "Orange"
    else: # wavelength is between 620 and 750
        color = "Red"

    # Print the color corresponding to the wavelength
    print(f"The color corresponding to {wavelength} nm is {color}.")
[10:05 pm, 10/04/2023] Raman Pal: Problem -II
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
[10:05 pm, 10/04/2023] Raman Pal: # Prompt user to enter frequency
frequency = float(input("Enter frequency in Hertz (Hz): "))

# Determine radiation category based on frequency range
if frequency < 3e9:
    category = "Radio Waves"
elif 3e9 <= frequency < 3e12:
    category = "Microwaves"
elif 3e12 <= frequency < 4.3e14:
    category = "Infrared Light"
elif 4.3e14 <= frequency < 7.5e14:
    category = "Visible Light"
elif 7.5e14 <= frequency < 3e17:
    category = "Ultraviolet Light"
elif 3e17 <= frequency < 3e19:
    category = "X-Rays"
else: # frequency is 3e19 or greater
    category = "Gamma Rays"

# Print the radiation category corresponding to the frequency
print(f"A frequency of {frequency} Hz corresponds to {category}.")
