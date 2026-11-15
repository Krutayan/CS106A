"""
Assignment: Fahrenheit to Celsius (Introduction to Python / Worked Example)
Course: Stanford CS106A
Filename: fahrenheit_to_celsius.py

Description:
A foundational Python program demonstrating floating-point console input, 
arithmetic calculations, and temperature conversion from Fahrenheit to Celsius[cite: 13].
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
    # this will take input from user in fahrenheit
    degrees_celsius = (fahrenheit_temperature - 32) * 5.0/9.0
    print("Temperature: "+str(fahrenheit_temperature)+"F"+ " = " +str(degrees_celsius)+"C")



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
