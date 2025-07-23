# PROJECT 2 - AGE CALCULATOR APP

# 📅 Age Calculator App\

# HeroBoard Entry #2 - Day 2 Project 02A

print("📅 Age Calculator App")

print("👴 welcome to the Age Calculator! 👶")
print("Let me guess your age..\n")

# Step 1: Ask for user's name

name = input("What is your name? ")

# Step 2: Ask for birth year

birth_year = int(input("What year were you born? "))

# Step 3: Convert input to integer

birth_year = int(birth_year)

# Step 4: Calculate age

current_year = 2025
age = current_year - birth_year

# Step 5: Display result

print(f"\n🧾 Hello {name}!")
print(f"You were born in {birth_year}, so you are {age} years old in {current_year}.")

# Bonus flavor

if age < 13:
print("🍼 You're still a kid! keep dreaming big!")
elif age < 20:
print("🧑‍🎓 Teenage energy detected! Power up your lesrning>")
elif age < 35:
print("👨‍💼 Young adult on the rise! Build your empire.")
else:
print("👴 A wise soul. Share your wisdom!")
