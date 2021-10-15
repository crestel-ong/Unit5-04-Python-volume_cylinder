#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# This Volume of Cylinder program in Python
# This program uses functions with multiple parameters

import math


def calculate_volume(radius, height):
    # this function calculates the volume of a cylinder

    # process
    volume = round(math.pi * radius ** 2 * height, 2)

    return volume


def main():
    # this function gets the radius and height

    # tell the user what the program does
    print("This program calculates the volume of a cylinder.")
    print("Please enter the radius and height.")
    print("")

    # input
    radius = input("The radius is (cm): ")
    height = input("The height is (cm): ")
    print("")

    try:
        # convert from string to float
        radius_from_user = float(radius)
        height_from_user = float(height)
        # call functions
        returned_volume = calculate_volume(radius_from_user, height_from_user)
        # output
        print("The volume of this cylinder with the radius ", end="")
        print(
            "of {0} cm and height {1} cm is {2} cm³.".format(
                radius_from_user, height_from_user, returned_volume
            )
        )
    except Exception:
        print("Invalid input.")
    print("\nDone.")


if __name__ == "__main__":
    main()
