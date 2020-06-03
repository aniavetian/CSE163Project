"""
Ani Avetian and Bradley Knorr
CSE 163 AA and AC
Assignment: Final Project

Description: Tests every function in every file.
"""

# Python import
import pandas as pd

# File imports
from pandas_file import Pandas
from graphing_file import Graphing
from habitable_planets_file import Habitable_Planets
from machine_learning_file import Machine_Learning


def test_habitable_planets_file(df):
    """
    Function takes in a dataframe and tests the habitable plaents file.
    """
    print('_______Testing Habitable Planets File_______')
    # --- Testing habitable_planets_file --- #
    Hb = Habitable_Planets(df)

    # Tests the habitable_zone() method and find_life method.
    # Note: The find life method calculation was done manually
    # on dataframe. In folder 'Files' there is the manual
    # calulation.
    number_in_hb_zone = Hb.habitable_zone()
    life_df = Hb.find_life()
    print('Number of planets in habitable zone:', number_in_hb_zone)
    print('Names of planets that are cabable of having life:')
    print(life_df['pl_name'])
    print()

    print('\t_______Testing Temperature Calculation and Life Function_______')

    # Tests the calculate_planet_tempurature() method
    # comparing our tempurature predictions to NASA's
    print("\n  Compare our temperature predictions to NASA's:")
    # Hot Planets
    planet_temp = Hb.calculate_planet_tempurature(1.37, 6440, 0.0436)
    Hb.compare_temp_to_nasa(planet_temp, 1657)  # ~1657
    planet_temp = Hb.calculate_planet_tempurature(0.79, 5075, 0.1055)
    Hb.compare_temp_to_nasa(planet_temp, 600)  # ~600
    # Mild planets
    planet_temp = Hb.calculate_planet_tempurature(0.47, 3660, 0.05023)
    Hb.compare_temp_to_nasa(planet_temp, 496)  # ~496
    planet_temp = Hb.calculate_planet_tempurature(0.47, 3660, 0.11283)
    Hb.compare_temp_to_nasa(planet_temp, 331)  # ~331
    # Cold planets
    planet_temp = Hb.calculate_planet_tempurature(0.73, 4890, 1.89)
    Hb.compare_temp_to_nasa(planet_temp, 131)  # ~131
    planet_temp = Hb.calculate_planet_tempurature(1.53, 5794, 18)
    Hb.compare_temp_to_nasa(planet_temp, 171)  # ~171

    print("  TRAPPIST-1b:")
    TRAPPIST_1b = Hb.calculate_planet_tempurature(0.12, 2559, 0.01111)
    Hb.compare_temp_to_nasa(TRAPPIST_1b, 0)
    print("  TRAPPIST-1c:")
    TRAPPIST_1c = Hb.calculate_planet_tempurature(0.12, 2559, 0.01521)
    Hb.compare_temp_to_nasa(TRAPPIST_1c, 0)
    print("  TRAPPIST-1d:")
    TRAPPIST_1d = Hb.calculate_planet_tempurature(0.12, 2559, 0.02144)
    Hb.compare_temp_to_nasa(TRAPPIST_1d, 0)
    print("  TRAPPIST-1e:")
    TRAPPIST_1e = Hb.calculate_planet_tempurature(0.12, 2559, 0.02817)
    Hb.compare_temp_to_nasa(TRAPPIST_1e, 0)
    print("  Kepler-452b:")
    kepler_452b = Hb.calculate_planet_tempurature(1.11, 5757, 1.046)
    Hb.compare_temp_to_nasa(kepler_452b, 265.15)

    # testing the isHabitable() method
    # testing earth's habitability (should return true)
    habitable = Hb.isHabitable(15, 1, 1, 5.1, 0.02)
    print("  Earth's habitability: %s" % (habitable))
    print()


def test_machine_learning_file(df):
    """
    Function takes in a dataframe and tests the machine learning file.
    """
    print('_______Testing Machine Learning File_______')
    ml = Machine_Learning(df)
    print("  MAE: Close to 0 is good | r^2: Close to 1 is good")

    # testing the mass_of_planet() method
    mass_accuracy = ml.mass_of_planet()
    print("\tMass Accuracy: %f Earth masses (MAE), %f (r^2)"
          % (mass_accuracy[0], mass_accuracy[1]))

    # testing the distance_from_star() method
    distance_accuracy = ml.distance_from_star()
    print("\tDistance Accuracy: %f AU (MAE), %f (r^2)"
          % (distance_accuracy[0], distance_accuracy[1]))

    # testing the eccentricity() method
    eccentricity_accuracy = ml.eccentricity()
    print("\tEccentricity Accuracy: %f (MAE), %f (r^2)"
          % (eccentricity_accuracy[0], eccentricity_accuracy[1]))
    print()


def test_pandas_file(df, smaller_df):
    """
    Function takes in a dataframe and tests the pandas file.
    """
    print('_______Testing Pandas File_______')

    print('Testing Big DataFrame...')
    pandas = Pandas(df)
    average_planets = pandas.average_planets()
    max_planets = pandas.max_planets()
    average_mean = pandas.mean_mass_planets()
    print("Average number of planets per solar system: %f" % (average_planets))
    print("Max number of planets in a solar system: %d" % (max_planets))
    print("Mean mass planets in each solar system:")
    print(average_mean)

    print()
    print('Testing Smaller DataFrame...')
    pandas_smaller = Pandas(smaller_df)
    average_planets_s = pandas_smaller.average_planets()
    max_planets_s = pandas_smaller.max_planets()
    average_mean_s = pandas_smaller.mean_mass_planets()
    print("Average number of planets per solar system (smaller dataset): %f"
          % (average_planets_s))
    print("Max number of planets in a solar system (smaller dataset): %d"
          % (max_planets_s))
    print("Mean mass planets in each solar system (smaller dataset):")
    print(average_mean_s)


def test_graphing_file(df):
    """
    Function takes in a dataframe and a smaller subset of that
    dataframe and tests the graphing file.
    """
    print('_______Testing Graphing File_______')
    graphing = Graphing(df)
    graphing.distribution_mass()
    print("Created mass_dist.png")
    graphing.distribution_distance()
    print("Created distance_dist.png")
    print()


def main():
    """
    Calls all methods for the Final Project
    """
    df = pd.read_csv("data/Exoplanets_With_Column_Info.csv", skiprows=98)
    smaller_df = df.loc[0:9]

    test_graphing_file(df)
    test_habitable_planets_file(df)
    test_machine_learning_file(df)
    test_pandas_file(df, smaller_df)


if __name__ == '__main__':
    main()
