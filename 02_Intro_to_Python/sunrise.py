"""
Assignment: Sunrise Fill-in-the-Blanks (Introduction to Python)
Course: Stanford CS106A
Filename: sunrise.py

Description:
A foundational Python program demonstrating console input, string variables, 
and f-string template formatting to turn user inputs into a creative sentence story[cite: 13].
"""

"""
Example of a Fill in the Blank program, like the one from the lesson.
The user will enter three words (a color, an adjective and a goal).
We will then turn them into a one sentence story.
"""

def main():
    color = input("A color: ")
    adjective = input("An adjective:")
    goal = input("A goal you would like to achieve:")
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today i will finally {goal}.")


if __name__ == "__main__":
    main()
