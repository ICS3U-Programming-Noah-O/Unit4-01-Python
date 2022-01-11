#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 5, 2022
# This program allows a user to enter a positive number and then see
# the sum of all whole numbers up to that number.


def main():

    number_counter = 0
    total = 0

    # Print introduction message and get user input
    print("This program will calculate the sum of all of the whole" +
          "numbers up to a chosen number.")
    print(" ")
    user_num = input("Enter a positive number: ")
    print(" ")

    try:
        # Make sure user input is an integer
        user_num_int = int(user_num)

        # Makes sure that user number is positive
        if user_num_int >= 0:
            # Loop that calculates the sum of all of the whole numbers up to
            # and including the user number
            while number_counter <= user_num_int:
                total = total + number_counter
                print("Tracking {} times through the loop".format(number_counter))
                number_counter = number_counter + 1
                print(" ")

            # Print final result
            print("The sum of all whole numbers from 0 to {}".format(user_num)
                  + " is {}.".format(total))
        else:
            print("{} is not a positive number.".format(user_num_int))

    except Exception:
        # Prevent crash by displaying error message if user
        # input is not an integer
        print("'{}' is not a number".format(user_num))


if __name__ == "__main__":
    main()
