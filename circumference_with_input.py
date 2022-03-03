#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created March 2022
# This program calculates the circumference of
# a circle with user input, using a constant

import constants


def main():
    # this function calculates the perimeter and area

    # input
    radius = int(input("Enter the radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("The circumference will be {0} mm.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
