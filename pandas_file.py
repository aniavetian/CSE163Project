"""
Ani Avetian
May 26, 2020
CSE 163 Section AA

Description: File contains Pandas class which computes answers to
questions 1 and 2.
"""


class Pandas:

    def __init__(self, df):
        """
        Function takes in a dataframe and creates the Pandas class.
        """
        self._df = df

    def average_planets(self):
        """
        Function computes the average number of exoplanets for each
        solar system.
        """
        solar_system = self._df.groupby('pl_hostname')['pl_name'].count()
        average = solar_system.mean()
        return average

    def mean_mass_planets(self):
        """
        Function computes the mean mass for exoplanets for each solar
        system. The mass is measured in 'earth masses'.
        """
        new_df = self._df[['pl_hostname', 'pl_masse']]
        new_df = new_df.dropna()
        mean_masses = new_df.groupby('pl_hostname')['pl_masse'].mean()
        return mean_masses
