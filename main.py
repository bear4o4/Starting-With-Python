import math



def treasure_island_game():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")


    choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
    if choice1 == "left":

        choice2 = input( "You've come to a lake. There is an island in the middle of the lake. Type 'swim' to swim across or 'wait' to wait for a boat: ").lower()
        if choice2 == "wait":
            choice3 = input("You arrive at the island unharmed. There is a house with three doors: one red, one yellow, and one blue. Which door do you choose? ").lower()
            if choice3 == "yellow":
                print("You found the treasure! You Win!")
            elif choice3 == "red":
                print("It's a room full of fire. Game Over.")
            elif choice3 == "blue":
                print("You enter a room of beasts. Game Over.")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You got attacked by an angry trout. Game Over.")
    else:
        print("You fell into a hole. Game Over.")


def calculate_split_bill():
    print("\nTask: Split the Bill")

    total_bill = float(input("Enter the total bill amount: "))
    tip_percentage = float(input("Enter the percentage tip you would like to give: "))
    num_people = int(input("Enter the number of people splitting the bill: "))


    tip_amount = (tip_percentage / 100) * total_bill
    total_amount = total_bill + tip_amount

    amount_per_person = total_amount / num_people

    print(f"Each person should pay: ${amount_per_person:.2f}")


def calculate_factorial():
    print("\nTask: Factorial Calculation")


    num = int(input("Enter a number to calculate its factorial: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = math.factorial(num)
        print(f"The factorial of {num} is: {factorial}")


def sum_of_digits():
    print("\nTask: Sum of Digits Until a Single Digit")


    num = int(input("Enter a number: "))


    while num >= 10:
        num = sum(int(digit)
                  for digit in str(num))

    print(f"Sum of digits until a single digit: {num}")




def main_menu():
    print("\nMain Menu:")
    print("1. Play Treasure Island Game")
    print("2. Split the Bill")
    print("3. Factorial")
    print("4. Sum of digits")
    print("5. Exit")
    while True:
        choice = input("\nChoose an option : ")

        if choice == "1":
            treasure_island_game()
        elif choice == "2":
            calculate_split_bill()
        elif choice =="3":
            calculate_factorial()
        elif choice =="4":
            sum_of_digits()
        elif choice == "5":
            print("Exiting the program. ")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
