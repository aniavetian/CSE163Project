"""
Ani Avetian
May 26, 2020
CSE 163 Section AA

Description: File contains Pandas class which computes answers to
questions 1 and 2.
"""

import matplotlib.pyplot as plt
import seaborn as sns


class Pandas:
    """
    Pandas class will give us information about our data on exoplanets.
    """
    def __init__(self, df):
        """
        Function takes in a dataframe and creates the Pandas class.
        """
        self._df = df

    def average_planets(self, plot):
        """
        Function takes in a boolean value to tell the function if it should
        plot a plot of number of planets per solar system vs. number of
        solar systems with that many planets. If True the plot will be plotted.
        The function also computes the average number of exoplanets for each
        solar system and returns that average.
        """
        solar_system = self._df.groupby('hostname')['pl_name'].count()

        if plot:
            sns.distplot(solar_system, kde=False)
            plt.title('Number of Planets Per Solar System')
            plt.xlabel('Number of Planets')
            plt.ylabel('Number of Solar Systems')
            plt.yscale('log')
            plt.savefig('figures/average_planets.png', bbox_inches='tight')

        average = solar_system.mean()
        return average

    def max_planets(self):
        """
        Function will return the max amount of planets the belong in a
        solar system.
        """
        max_mask = self._df['sy_pnum'] == self._df['sy_pnum'].max()
        new_df = self._df[max_mask]
        return new_df['sy_pnum'].max()

    def mean_mass_planets(self):
        """
        Function computes the mean mass for exoplanets for each solar
        system. The mass is measured in 'earth masses'. The function
        will return a dataframe with every solar system and its average
        mass.
        """
        new_df = self._df[['hostname', 'pl_bmasse']]
        new_df = new_df.dropna()
        mean_masses = new_df.groupby('hostname')['pl_bmasse'].mean()
        return mean_masses
