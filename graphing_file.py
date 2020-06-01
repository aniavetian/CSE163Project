"""
Ani Avetian
May 31, 2020
CSE 163 Section AA

Description: ADD
"""


# import matplotlib.pyplot as plt
# import seaborn as sns


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
        new_df = self._df[['pl_name', 'pl_masse']]
        # new_df['spot'] = ['log0' if x >= 0 & < 10 'log10' elif x >= 10 & x <
        #  100 for x in df['pl_masse']]
        new_df = new_df.dropna()
        print(new_df)

        # sns.kdeplot(new_df)
        # sns.catplot(col='pl_masse', data=new_df, kind='bar')
        # plot.set(xscale='log')

        # plt.xlabel('Planet Name')
        # plt.ylabel('Planet Mass [Earth Mass]')
        # plt.title('Distribution of Masses for Exoplanets')
        # plt.savefig('figures/mass_dist.png', bbox_inches='tight')

    def distribution_distance(self):
        new_df = self._df[['pl_hostname', 'orbsmax']]
        new_df = new_df.dropna()
