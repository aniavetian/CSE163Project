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
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


class Machine_Learning:
    def __init__(self, df):
        """
        Parameters:
          df - dataframe to run machine learning models on
        """
        self._data = df

    def mass_of_planet(self):
        new_data = self.data[['pl_pnum', 'pl_orbper', 'pl_orbsmax',
                              'pl_masse', 'pl_orbeccen', 'pl_orbincl',
                              'pl_radj', 'pl_dens', 'st_teff',
                              'st_mass', 'st_rad']]
        new_data = new_data.dropna()

        features = new_data[['pl_pnum', 'pl_orbper', 'pl_orbsmax',
                             'pl_orbeccen', 'pl_orbincl',
                             'pl_radj', 'pl_dens', 'st_teff',
                             'st_mass', 'st_rad']]
        labels = new_data['pl_masse']

        features = pd.get_dummies(features)

        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=0.2)

        # Create an untrained model
        model = DecisionTreeClassifier()

        # Train it on the **training set**
        model.fit(features_train, labels_train)

        # Compute training accuracy
        train_predictions = model.predict(features_train)
        train_acc = accuracy_score(labels_train, train_predictions)
        print(train_acc)

        # Compute test accuracy
        test_predictions = model.predict(features_test)
        test_acc = accuracy_score(labels_test, test_predictions)
        print(test_acc)

        return test_acc

    def distance_from_star(self):
        new_data = self.data[['pl_pnum', 'pl_orbper', 'pl_orbsmax',
                              'pl_masse', 'pl_orbeccen', 'pl_orbincl',
                              'pl_radj', 'pl_dens', 'st_teff',
                              'st_mass', 'st_rad']]
        new_data = new_data.dropna()

        features = new_data[['pl_pnum', 'pl_orbper',
                             'pl_masse', 'pl_orbeccen', 'pl_orbincl',
                             'pl_radj', 'pl_dens', 'st_teff',
                             'st_mass', 'st_rad']]
        labels = new_data['pl_orbsmax']

        features = pd.get_dummies(features)

        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=0.2)

        # Create an untrained model
        model = DecisionTreeClassifier()

        # Train it on the **training set**
        model.fit(features_train, labels_train)

        # Compute training accuracy
        train_predictions = model.predict(features_train)
        train_acc = accuracy_score(labels_train, train_predictions)
        print(train_acc)

        # Compute test accuracy
        test_predictions = model.predict(features_test)
        test_acc = accuracy_score(labels_test, test_predictions)
        print(test_acc)

        return test_acc

    def eccentricity(self):
        new_data = self.data[['pl_pnum', 'pl_orbper', 'pl_orbsmax',
                              'pl_masse', 'pl_orbeccen', 'pl_orbincl',
                              'pl_radj', 'pl_dens', 'st_teff',
                              'st_mass', 'st_rad']]
        new_data = new_data.dropna()

        features = new_data[['pl_pnum', 'pl_orbper', 'pl_orbsmax',
                             'pl_masse', 'pl_orbincl',
                             'pl_radj', 'pl_dens', 'st_teff',
                             'st_mass', 'st_rad']]
        labels = new_data['pl_orbeccen']

        features = pd.get_dummies(features)

        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=0.2)

        # Create an untrained model
        model = DecisionTreeClassifier()

        # Train it on the **training set**
        model.fit(features_train, labels_train)

        # Compute training accuracy
        train_predictions = model.predict(features_train)
        train_acc = accuracy_score(labels_train, train_predictions)
        print(train_acc)

        # Compute test accuracy
        test_predictions = model.predict(features_test)
        test_acc = accuracy_score(labels_test, test_predictions)
        print(test_acc)

        return test_acc

    # Removing when these functions work
    def example_machine_learning(self):
        data = pd.read_csv('/home/mushrooms.csv')

        new_data = data[['pl_pnum', 'pl_orbper', 'pl_orbsmax', 'class']]
        new_data = new_data.dropna()

        features = new_data[['cap-shape', 'cap-surface', 'cap-color']]
        labels = new_data['class']

        features = pd.get_dummies(features)

        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=0.3, random_state=1)

        # Create an untrained model
        model = DecisionTreeClassifier()

        # Train it on the **training set**
        model.fit(features_train, labels_train)

        # Compute training accuracy
        train_predictions = model.predict(features_train)
        train_acc = accuracy_score(labels_train, train_predictions)
        print(train_acc)

        # Compute test accuracy
        test_predictions = model.predict(features_test)
        test_acc = accuracy_score(labels_test, test_predictions)
        print(test_acc)
