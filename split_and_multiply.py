#!/usr/bin/env python3

# Created by: Santiago Hewett
# Created on: Jan 11, 2023
# This program allows users to input a list of numbers, 
# specify a multiplier, multiply each element by the multiplier, 
# and view the resulting split list, with the option to repeat the process


def split_and_multiply(input_list, multiplier):
    # Multiply each element in the input list by the multiplier
    multiplied_list = [num * multiplier for num in input_list]

    # Find the midpoint of the multiplied list
    mid = len(multiplied_list) // 2

    # Split the multiplied list into two halves
    first_half = multiplied_list[:mid]
    second_half = multiplied_list[mid:]

    # Return the two halves
    return first_half, second_half


def main():
    while True:
        try:
            # Take user input for a list of numbers separated by commas
            user_input = input("Enter a list of numbers separated by commas: ")

            # Convert the user input to a list of integers
            input_list = [int(num) for num in user_input.replace(" ", "").split(",")]
        except ValueError:
            print("Error: Please enter valid integers separated by commas.")
            continue  # Continue the loop if an error occurs

        try:
            # Take user input for the multiplier, handling the possibility of a string input
            multiplier = float(input("Enter a multiplier: "))
        except ValueError:
            print("Error: Please enter a valid number for the multiplier.")
            continue  # Continue the loop if an error occurs

        # Call the split_and_multiply function with user inputs
        first_half, second_half = split_and_multiply(input_list, multiplier)

        # Print the results
        print("The first half of the multiplied list is:", first_half)
        print("The second half of the multiplied list is:", second_half)

        # Ask if the user wants to try again
        try_again = input("Do you want to try again? (yes/no): ").lower()
        if try_again != "yes":
            break  # Exit the loop if the user doesn't want to try again


if __name__ == "__main__":
    main()
