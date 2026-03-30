import random

# 1. Choose Difficulty (Keeping your existing logic)
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
    limit = 100

num_rounds = int(input("\nHow many questions would you like? "))
score = 0

# 2. The Game Loop
for i in range(num_rounds):
    num1 = random.randint(1, limit)
    num2 = random.randint(1, limit)
    
    # NEW: Pick a random operation
    operation = random.choice(['+', '-', '*'])
    
    # Calculate the answer based on the operation
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        # This makes sure you don't get negative numbers
        if num1 < num2:
            num1, num2 = num2, num1 
        correct_answer = num1 - num2
    else: # Multiplication
        # For multiplication, we use smaller numbers so it's not impossible!
        num1 = random.randint(1, 12) 
        num2 = random.randint(1, 12)
        correct_answer = num1 * num2

    print(f"\nQuestion {i + 1} of {num_rounds}:")
    
    # Use the 'operation' variable in the input prompt
    user_answer = int(input(f"What is {num1} {operation} {num2}? "))

    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The answer was {correct_answer}")

print(f"\nGame over! Your final score is {score} out of {num_rounds}.")