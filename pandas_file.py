"""
Ani Avetian
May 26, 2020
CSE 163 Section AA

Description: ADD
"""


class Pandas:

    def __init__(self, df):
        """
        Function takes in a dataframe and creates the Pandas class.
        """
        self.df = df

    def average_planets(self):
        """
        Function computes the average number of exoplanets for each
        solar system.
        """
        solar_system = df.groupby('pl_hostname')['pl_name'].count()
        filtered = df[solar_system]
        print(filtered)