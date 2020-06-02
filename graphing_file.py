"""
Ani Avetian
May 31, 2020
CSE 163 Section AA

Description: ADD
"""


import matplotlib.pyplot as plt
import seaborn as sns


class Graphing:

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

    def distribution_distance(self):
        """
        Function graphs the distribution of distance for all exoplants.
        """
        new_df = self._df[['pl_hostname', 'pl_orbsmax']]
        new_df = new_df.dropna()
