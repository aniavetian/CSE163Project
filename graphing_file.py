"""
Ani Avetian
May 31, 2020
CSE 163 Section AA

Description: File contains functions that answer questions 8
and 9. These questions all have to do with graphing.
"""


import matplotlib.pyplot as plt
import seaborn as sns


class Graphing:
    """
    Graphing class contains functions that give us information
    about exoplanets visually, by plotting them.
    """
    def __init__(self, df):
        """
        Function takes in a dataframe and initalizes a Graphing class.
        """
        self._df = df

    def distribution_mass(self):
        """
        Function graphs the distribution of masses for all the exoplanets.
        """
        # Select columns we need and drop NA values
        new_df = self._df[['pl_name', 'pl_masse']]
        new_df = new_df.dropna()

        # Plot distribution
        sns.distplot(new_df['pl_masse'], kde=False)

        # Label axis and save graph
        plt.xlabel('Planet Mass [Earth Mass]')
        plt.ylabel('Number of Planets')
        plt.title('Distribution of Masses for Exoplanets')
        plt.savefig('figures/mass_dist.png', bbox_inches='tight')
        plt.clf()

    def distribution_distance(self):
        """
        Function graphs the distribution of distance for all exoplants.
        """
        # Select columns we need and drop NA values
        new_df = self._df[['pl_hostname', 'pl_orbsmax']]
        new_df = new_df.dropna()

        # Plot distribution
        sns.distplot(new_df['pl_orbsmax'], kde=False)

        # Label axis and save graph
        plt.xlabel('Planet Orbit Semi-Major Axis [AU]')
        plt.ylabel('Number of Planets (log scale)')
        plt.title('Distribution of Distance of Exoplanet to Star')
        plt.yscale('log')
        plt.savefig('figures/distance_dist.png', bbox_inches='tight')
        plt.clf()
