"""
Assignment: Hello Name (Introduction to Python)
Course: Stanford CS106A
Filename: hello_name.py

Description:
A foundational Python program demonstrating console input and output, 
prompting the user for their name and greeting them dynamically using f-strings[cite: 16].
"""

def main():
    name = input('What is your name?')
    print(f"Hello {name}")

if __name__ == '__main__':
    main()
