print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

# input
weight = float(input("Input Waeight: (kg)"))
height = float(input("Input Height: (m)"))

# process
BMI = weight / height ** 2

# output
print("bmi_User = ", BMI)

