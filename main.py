"""
Ani Avetian and Bradley Knorr
CSE 163 AA and AC
Assignment: Final Project
Description: Tests every function in every file
"""

# Python import
import pandas as pd

# File imports
from pandas_file import Pandas  # Whatever you name the class
from graphing_file import Graphing  # Whatever you name the class
from habitable_planets_file import Habitable_Planets
from machine_learning_file import Machine_Learning


def main():
    """
    Calls all methods for the Final Project
    """
    df = pd.read_csv("data/Exoplanets.csv")

    # --- Testing habitable_planets_file --- #
    Hb = Habitable_Planets(df)

    # testing earth's tempurature
    #   earth's average tempurature is 15°C for comparison
    tempurature = Hb.calculate_planet_tempurature(1, 5780, 1)
    print(tempurature)

    # testing earth's habitability (should return true)
    habitable = Hb.isHabitable(15, 1, 1, 5.1, 0.02)
    print(habitable)

    # --- Testing machine_learning_file ---#
    ml = Machine_Learning(df)
    mass_accuracy = ml.mass_of_planet()
    print(mass_accuracy)
    distance_accuracy = ml.distance_from_star()
    print(distance_accuracy)
    eccentricity_accuracy = ml.eccentricity()
    print(eccentricity_accuracy)

    # --- Testing machine_learning_file --- #

    # --- Testing pandas_file --- #


if __name__ == '__main__':
    main()
