"""
Ani Avetian and Bradley Knorr
CSE 163 AC
Assignment: Final Project
Description:
"""
import math
import matplotlib.pyplot as plt
import seaborn as sns


class Habitable_Planets:
    def __init__(self, df):
        """
        Parameters:
          df - dataframe to determine if a planet is habitable
        """
        self._df = df

    def get_habitable_planets(self):
        """
        Function will return a dataframe that contains all exo-planets that
        are in the habitable zone.

        Written By: Ani Avetian
        """

        # Create column to store calculated values for temperature
        new_df = self._df
        new_df['calc_temp'] = self.calculate_planet_tempurature(
                new_df['st_rad'], new_df['st_teff'], new_df['pl_orbsmax'])

        # Count how many planets are in the Goldilocks zone based on
        # calculated temperature
        corr_temp = (new_df['calc_temp'] >= 0) & (new_df['calc_temp'] <= 100)
        planets_in_habitable_zone = new_df[corr_temp]
        return planets_in_habitable_zone

    def habitable_zone(self):
        """
        Function will compute the number of exoplanets that are in the
        habitable zone and return that value. Function will also plot
        the distance of the exoplanet(using the semi major axis [AU])
        to its host star vs. its stars size so we can visually see
        which planets are in the habitable zone.

        Written By: Ani Avetian
        """

        # Create new dataset with all planets in habitable zone
        new_df = self.get_habitable_planets()

        # Using the planets in the Habitable zone, we will plot their
        # distance to thier host star vs. their star size.
        # linear version
        sns.relplot(x='pl_orbsmax', y='st_mass', data=new_df, kind='line')
        plt.title('Exoplanet Distance From Star vs. Star Mass')
        plt.xlabel('Orbit Semi-Major Axis [AU]')
        plt.ylabel('Steller Mass [Solar Mass]')
        plt.savefig('figures/habitable_linear.png', bbox_inches='tight')
        plt.clf()

        # log version
        sns.relplot(x='pl_orbsmax', y='st_mass', data=new_df, kind='line')
        plt.title('Exoplanet Distance From Star vs. Star Mass')
        plt.xlabel('Orbit Semi-Major Axis [AU]')
        plt.ylabel('Steller Mass [Solar Mass]')
        plt.xscale('log')
        plt.yscale('log')
        plt.savefig('figures/habitable_log.png', bbox_inches='tight')
        plt.clf()

        # Scatter Plot
        fig, ax = plt.subplots(1)

        sns.regplot(x='pl_orbsmax', y='st_mass', data=self._df, color='r',
                    marker='o', label='Not in Habitable Zone',
                    fit_reg=False, scatter_kws={'s': 3}, ax=ax)
        sns.regplot(x='pl_orbsmax', y='st_mass', data=new_df, color='b',
                    marker='o', label='Habitable Zone',
                    fit_reg=False, scatter_kws={'s': 8}, ax=ax)

        plt.xscale('log')
        plt.yscale('log')
        plt.xlim(0.005, 100)
        plt.ylim(0.05, 10)

        plt.title("Exoplanet Distance From Star vs. Star Mass")
        plt.xlabel("Distance from Star (AU)")
        plt.ylabel("Mass of Star (Stellar Masses)")

        plt.legend()

        plt.savefig('figures/scatter_habitable.png', bbox_inches='tight')
        plt.clf()

        return len(new_df)

    def find_life(self):
        """
        Function will return a dataframe containing information about
        the planets that are capable of having life.

        Written By: Ani Avetian
        """
        df_habitable = self.get_habitable_planets()
        new_df = df_habitable[['pl_hostname', 'pl_name', 'calc_temp',
                               'pl_masse', 'pl_rade',
                               'pl_dens', 'pl_orbeccen', 'st_mass',
                               'pl_orbsmax']].dropna()
        new_df['have_life'] = self.isHabitable(new_df['calc_temp'],
                                               new_df['pl_masse'],
                                               new_df['pl_rade'],
                                               new_df['pl_dens'],
                                               new_df['pl_orbeccen'])

        data_planets = new_df[new_df['have_life']]

        # Scatter Plot
        fig, ax = plt.subplots(1)

        sns.regplot(x='pl_orbsmax', y='st_mass', data=self._df, color='r',
                    marker='o', label='Not in Habitable Zone',
                    fit_reg=False, scatter_kws={'s': 3}, ax=ax)
        sns.regplot(x='pl_orbsmax', y='st_mass', data=df_habitable, color='b',
                    marker='o', label='Habitable Zone',
                    fit_reg=False, scatter_kws={'s': 8}, ax=ax)
        sns.regplot(x='pl_orbsmax', y='st_mass', data=data_planets, color='g',
                    marker='o', label='Potential for Life',
                    fit_reg=False, scatter_kws={'s': 100}, ax=ax)

        plt.xscale('log')
        plt.yscale('log')
        plt.xlim(0.005, 100)
        plt.ylim(0.05, 10)

        plt.title("Exoplanet Distance From Star vs. Star Mass")
        plt.xlabel("Distance from Star (AU)")
        plt.ylabel("Mass of Star (Stellar Masses)")

        plt.legend()

        plt.savefig('figures/scatter_life.png', bbox_inches='tight')
        plt.clf()

        return data_planets

    # Will be a private function after testing is done
    def calculate_planet_tempurature(self, R, T, r):
        """
        Parameters:
          R - radius of star: Stellar Radius [Solar radii]
          T - tempurature of star: Effective Temperature [K]
          r - radius of orbit: Orbit Semi-Major Axis [au]

        Calculations:
            Formula: (In this formula, T is effective tempurature of the
                      planet)
                σT^4 = F = L/(4πr^2)
            Units = (W * m^(-2) * K^(-4)) * K^4 = W * m^(-2) = ((W * m^(-2) *
                     K^(-4)) * K^4 * m^2) * m^(-2)
            Solve for T:
                T = ∜(F/σ)
            Luminosity Formula: (In this formula, T is effective tempurature
                                 of the star)
                L = σT^4 * (4πr^2)
            Habitable Tempurature for a planet:
                0-100°C (273.15-373.15° Kelvin)

        Description of Function:
            This function takes the 3 parameters needed to estimate the
            tempurature of a planet: radius of the star (R), effective
            tempurature of the star's surface (T), and the distance of the
            planet to the star (r). The star's information is used to
            calculate the luminosity (total energy produced in one second)
            of the star. The luminosity calculation along with the orbital
            radius is used to calculate the total energy flux of the space
            where the planet would be located. Total energy flux is what
            connects luminosity and effective tempurature of an area of
            space. So once you have the total energy flux, you can then use
            that number to calculate the effective tempurature of the space
            that the planet will inhabit (tempurature of the planet). That
            tempurature is in Kelvin, and we know that water is liquid in
            tempurature between 0-100°C, so before returning the tempurature
            we convert the tempurature to Celcius

        Return Value:
            If this function returns a value between 0 and 100, the planet is
            in the habitable zone

        Written by: Bradley Knorr
        """
        # Stefan Boltzmann constant (σ or σsb)
        osb = 5.670367*10**(-8)  # W * m^(-2) * K^(-4)

        # convert to correct units

        # Solar radii (R) to meters
        R = R * (6.955 * 10**8)  # m
        # Astronomical Units (r) to meters
        r = r * (1.5 * 10**11)  # m

        # Convert solar radius and surface temperture to luminosity (L)
        L = osb * T**4 * (4*math.pi*R**2)  # (W * m^(-2) * K^(-4)) * K^4 * m^2

        # Convert luminosity and orbital radius to Total Energy Flux (F)
        F = L/(4*math.pi*r**2)  # ((W * m^(-2) * K^(-4)) * K^4 * m^2) * m^(-2)

        # Convert Total Energy Flux (F) to effective planet tempurature
        planet_T = (F/osb)**(0.25)

        # Earth is supposed to be around 15-20°C, but the math ended up
        #   being 100°C too high. That could be due to the light reflected
        #   off the water, the atmosphere absorbing heat, or an minor issue
        #   with the formula. All of the math checks out and all of the
        #   units cancel. It does seem to overestimate until very low
        #   tempuratures too. The NASA data provides planet tempuratures
        #   for select planets, and if I multiply our calculated
        #   tempurature my ~2/3, the numbers line up very close with NASA's.
        #   I trust NASA's math more than ours, so I'm multiplying our
        #   number by 200/308 so the tempuratures line up with NASA's
        #   within 1% or so (excluding very high or low tempuratures)
        planet_T = planet_T * (200/308)

        # Convert Kelvin to Celcius
        planet_tempurature = planet_T - 273.15

        return planet_tempurature

    def compare_temp_to_nasa(self, calculated, nasa):
        nasa -= 273.15
        difference = (calculated / nasa) * 100 - 100
        print_string =\
            "\tOur function: %f°C\n\tNASA: %d°C\n\tDifference: %f%s\n"\
            % (calculated, nasa, difference, '%')
        print(print_string)

    # Will be a private function after testing is done
    def isHabitable(self, tempurature, mass, radius, density, eccentricity):
        """
        Parameters:
          tempurature - calculated tempurature - calculate_planet_tempurature()
                        or
                        Equilibrium Temperature [K] converted to Celcius
          mass - Planet Mass [Earth mass]
          radius - Planet Radius [Earth radii]
          density - Planet Density [g/cm**3]
          eccentricity - Eccentricity
          s_mass - mass of star (only used to return column for dataframe)
          distance - distance from star (only used to return column for
                     dataframe)

        Description of function:
            This function takes the parameters as features to determine if a
            planet is habitable. If the planet passes every test that we have
            for habitability, then we know it is habitable. Otherwise the
            planet is not habitable.

        Return Value:
            If the planet passes every test that we have for habitability,
            the returned Series will have True values in it.
            Otherwise the values in the Series will be False if even one
            test fails.

        Calculations made from this website:
            https://en.wikipedia.org/wiki/Planetary_habitability

        Written by: Bradley Knorr and Ani Avetian
        """

        # Determine if the tempurature is correct for liquid water
        # Return false in Series if planet is not in habitable zone
        t = (tempurature >= 0) & (tempurature <= 100)

        # Determine if it is a rocky (> 2.5) or gas (< 2.5) planet
        # Return false in Sereis if planet is not dense enough (not rocky)
        d = (density >= 2.5)

        # Determine if radius of planet is the correct size for habitability
        # Return false in Series if planet is too small or too large
        r = (radius >= 0.5) & (radius <= 2.5)

        # Determine if the planet has the correct mass for habitability
        # Return false in Series if planet is not massive enough or too massive
        m = (mass >= 0.3) & (mass <= 10)

        # Determine if the planet has a reasonable eccentricity for life
        # Note: in reality the eccentricity is used to determine if
        #   a planet escapes the habitable zone during its orbit as
        #   well as if tempuratures can vary too widely during its orbit
        # We are only testing if tempurature can vary too widely
        # Return false in Series if eccentricity is too large
        e = eccentricity <= 0.25

        # Combines all series together. If the planet passed all the
        # tests for life the value stored in the Series will be True,
        # otherwise false.
        values = t & d & r & m & e
        return values
