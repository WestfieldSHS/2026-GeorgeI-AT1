import random

score = 0
total_questions = 0

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    user_answer = int(input(f"What is {num1} + {num2}? "))
    total_questions += 1

    correct_answer = num1 + num2
    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. the right answer was {correct_answer}")
    choice = input("play again? (y/n): ")
    if choice == "n": break
print(f"Game over! Your final score is {score} out of {total_questions}.")