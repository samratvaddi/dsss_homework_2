import random


def integer(minimum, maximum):
    """
    Generate a random integer within the range
    """
    return random.randint(min, max)


def operation():
    """
    Generate a random operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])


def solution(num1, num2, operation):
    """
    Calculate the result of an arithmetic operation.
    """
  if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return result

def math_quiz():
    """
    Conduct a math quiz game with the user.
    """
    score = 0
    total_number_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_number_questions):
       num1 = integer(1, 10)
        num2 = integer(1, 5)
        operator = operation()

        question, correct_solution = solution(num1, num2, operator)
        print(f"\nQuestion: {question}")
        
        try:
            user_solution = int(input("Your answer: "))
        except ValueError:
            print("Wrong input, please enter a valid input.")
            user_solution = 0

        if user_solution == correct_solution:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_solution}.")

    print(f"\nGame over! Your score is: {score}/{total_number_questions}")

if __name__ == "__main__":
    math_quiz()
