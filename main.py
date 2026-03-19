import random

# 1. Choose Difficulty
print("Choose your difficulty:")
print("1. Easy (1-10)")
print("2. Medium (1-50)")
print("3. Hard (1-100)")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    limit = 10
elif choice == "2":
    limit = 50
else:
    limit = 100  # Defaults to Hard if they type anything else

num_rounds = int(input("\nHow many questions would you like? "))
score = 0

for i in range(num_rounds):
    # 2. Use the 'limit' variable here
    num1 = random.randint(1, limit)
    num2 = random.randint(1, limit)
    
    print(f"\nQuestion {i + 1} of {num_rounds}:")
    user_answer = int(input(f"What is {num1} + {num2}? "))

    if user_answer == (num1 + num2):
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The answer was {num1 + num2}")

print(f"\nGame over! Your final score is {score} out of {num_rounds}.")