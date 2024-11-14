'''1)	Гра з комп’ютером: камінь, ножиці, папір. Програма виконує запит від користувача
на введення одного із значень ["stone", "scissor", "paper"]. Наступним кроком, використовуючи 
модуль random, програма у випадковому порядку вибирає одне із значень ["stone", "scissor", "paper"]. 
В залежності від умови, що камінь перемагає ножиці, ножиці перемагають папір, а папір перемагає камінь визначити переможця.'''

import random

def getComputerChoice():
    return random.choice(["stone", "scissor", "paper"])

def winner(computerChoice, userChoice):
    if computerChoice == userChoice:
        return "It's a tie!"
    elif (userChoice == "stone" and computerChoice == "scissor") or \
         (userChoice == "scissor" and computerChoice == "paper") or \
         (userChoice == "paper" and computerChoice == "stone"):
        return "You win!"
    else:
        return "Computer wins!"

# Запитуємо вибір користувача
userChoice = input("Enter your choice (stone, scissor, paper): ")

# Отримуємо вибір комп'ютера
computerChoice = getComputerChoice()

print(f"Computer choice - {computerChoice}")

# Визначаємо результат
result = winner(computerChoice, userChoice)
print(result)

