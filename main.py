import math

unit_list = ["farad", "mikrofarad", "nanofarad", "pikofarad"]
pi = math.pi

print("""
======================================================================
Welcome to RLC Impedance calculator. Please follow the instructions.
======================================================================
""")

#Capacitor Input
while True:
    try:
        c = float(input("Please enter the value of the capacitor: "))
        break
    except Exception:
        print("Oops... Please enter a valid number...")

#Frequency Input
while True:
    try:
        f = float(input("Please enter the frequency of the system: "))
        break
    except Exception:
        print("Oops... Please enter a valid number...")

#Inductance Input
while True:
    try:
        l = float(input("Please enter the inductance value: "))
        break
    except Exception:
        print("Oops... Please enter a valid number...")

#Inductance Input
while True:
    try:
        r = float(input("Please enter the ohm value of the resistor: "))
        break
    except Exception:
        print("Oops... Please enter a valid number...")


while True:
    c_unit = input(
         """Please select and write one of the unit options given below:
         1. "Farad"
         2. "Mikrofarad" (10^-6)
         3. "Nanofarad" (10^-9)
         4. "Pikofarad" (10^-12)

         Value: """)

    if c_unit.lower() in unit_list:
        break
    else:
        print("Please enter a valid value.")

if c_unit.lower() == "farad":
    c = c
elif c_unit.lower() == "mikrofarad":
    c = c * pow(10, -6)
elif c_unit.lower() == "nanofarad":
    c = c * pow(10, -9)
elif c_unit.lower() == "pikofarad":
    c = c * pow(10, -12)

#Impedance Calculator Function
def calc_impedance(pi, c, f, l, r):
    # Capacitor Impedance Calculation
    xC = 1 / (2 * pi * f * c)
    # Bobbin Impedance Calculation
    xL = 2 * pi * f * l
    # System Impedance Calculation
    z = abs(math.sqrt(((xL - xC) ** 2) + (r ** 2)))

    return xC, xL, z

#Results
xC, xL, z = calc_impedance(pi, c, f, l, r)

print("\n")
print(f"Impedance value of the capacitor is: {xC:.2f} F")
print(f"Impedance value of the bobbin is: {xL:.2f} H")
print(f"Resistance of the system is: {r:.2f} Ω")
print(f"Impedance value of the system is: {z:.2f}")
