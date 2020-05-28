"""
Bradley Knorr
CSE 163 AC
Assignment: Final Project
Description: We are using machine learning to answer questions, predict
    values, and predict the accuracy of our models. This is to see if machine
    learning is a viable option to predict missing values in our data. We will
    primarily focus on model accuracy. This object contains all of the
    functions that match a machine learning research question.
"""
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


class Machine_Learning:
    def __init__(self, df):
        """
        Parameters:
          df - dataframe to run machine learning models on
        """
        self._data = df

    def mass_of_planet(self):
        """
        Creates a regression model that predicts the mass of an exoplanet
            that returns the accuracy of the model in terms of a tuple
            in the form (mean absolute error, r^2)
        """
        new_data = self._data[['pl_pnum', 'pl_orbper', 'pl_orbsmax',
                               'pl_masse', 'pl_orbeccen', 'pl_orbincl',
                               'pl_radj', 'pl_dens', 'st_teff',
                               'st_mass', 'st_rad']]
        new_data = new_data.dropna()

        features = new_data[['pl_pnum', 'pl_orbper', 'pl_orbsmax',
                             'pl_orbeccen', 'pl_orbincl',
                             'pl_radj', 'pl_dens', 'st_teff',
                             'st_mass', 'st_rad']]
        labels = new_data['pl_masse']

        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=0.2)

        # Create an untrained model
        model = DecisionTreeRegressor()

        # Train it on the **training set**
        model.fit(features_train, labels_train)

        # Compute test accuracy
        test_predictions = model.predict(features_test)
        test_acc = mean_absolute_error(labels_test, test_predictions)
        test_acc_r2 = r2_score(labels_test, test_predictions)

        return (test_acc, test_acc_r2)

    def distance_from_star(self):
        """
        Creates a regression model that predicts the distance of an exoplanet
            from its host star that returns the accuracy of the model in terms
            of a tuple in the form (mean absolute error, r^2)
        """
        new_data = self._data[['pl_pnum', 'pl_orbper', 'pl_orbsmax',
                               'pl_masse', 'pl_orbeccen', 'pl_orbincl',
                               'pl_radj', 'pl_dens', 'st_teff',
                               'st_mass', 'st_rad']]
        new_data = new_data.dropna()

        features = new_data[['pl_pnum', 'pl_orbper',
                             'pl_masse', 'pl_orbeccen', 'pl_orbincl',
                             'pl_radj', 'pl_dens', 'st_teff',
                             'st_mass', 'st_rad']]
        labels = new_data['pl_orbsmax']

        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=0.2)

        # Create an untrained model
        model = DecisionTreeRegressor()

        # Train it on the **training set**
        model.fit(features_train, labels_train)

        # Compute test accuracy
        test_predictions = model.predict(features_test)
        test_acc = mean_absolute_error(labels_test, test_predictions)
        test_acc_r2 = r2_score(labels_test, test_predictions)

        return (test_acc, test_acc_r2)

    def eccentricity(self):
        """
        Creates a regression model that predicts the eccentricity of an
            exoplanet's orbit that returns the accuracy of the model in
            terms of a tuple in the form (mean absolute error, r^2)
        """
        new_data = self._data[['pl_pnum', 'pl_orbper', 'pl_orbsmax',
                               'pl_masse', 'pl_orbeccen', 'pl_orbincl',
                               'pl_radj', 'pl_dens', 'st_teff',
                               'st_mass', 'st_rad']]
        new_data = new_data.dropna()

        features = new_data[['pl_pnum', 'pl_orbper', 'pl_orbsmax',
                             'pl_masse', 'pl_orbincl',
                             'pl_radj', 'pl_dens', 'st_teff',
                             'st_mass', 'st_rad']]
        labels = new_data['pl_orbeccen']

        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=0.2)

        # Create an untrained model
        model = DecisionTreeRegressor()

        # Train it on the **training set**
        model.fit(features_train, labels_train)

        # Compute test accuracy
        test_predictions = model.predict(features_test)
        test_acc = mean_absolute_error(labels_test, test_predictions)
        test_acc_r2 = r2_score(labels_test, test_predictions)

        return (test_acc, test_acc_r2)
