"""
Ani Avetian and Bradley Knorr
CSE 163 AC
Assignment: Final Project
Description:
"""
import math


class Habitable_Planets:
    def __init__(self, df):
        """
        Parameters:
          df - dataframe to determine if a planet is habitable
        """
        self._df = df

    def habitable_zone(self):
        return 0

    def find_life(self):
        return 0

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
                σSB*T^4 = F = L/(4πr^2)
            Solve for T:
                T = ∜(F/σSB)
            Luminosity Formula: (In this formula, T is effective tempurature
                                 of the star)
                L = R^2 * T^4
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

        # Stefan Boltzmann constant
        osb = 5.670367*10**(-8)

        # Convert solar radius and surface temperture to luminosity (L)
        L = R**2*T**4

        # Convert luminosity and orbital radius to Total Energy Flux (F)
        F = L/(4*math.pi*r**2)

        # Convert total energy flux to effective planet tempurature
        planet_T = (F/osb)**(1/float(4))

        # Convert Kelvin to Celcius
        planet_tempurature = planet_T + 273.15

        return planet_tempurature

    # Will be a private function after testing is done
    def isHabitable(self, tempurature, mass, radius, density, eccentricity):
        """
        Parameters:
          tempurature - calculated tempurature - calculate_planet_tempurature()
                        or
                        Equilibrium Temperature [K] converted to Celcius
          mass - Planet Mass [Earth mass]
          radius - Planet Radius [Earth radii]
          density - Planet Density Upper Unc. [g/cm**3]
          eccentricity - Eccentricity

        Description of function:
            This function takes the parameters as features to determine if a
            planet is habitable. If the planet passes every test that we have
            for habitability, returns true. Otherwise returns false if it
            fails one test

        Return Value:
            If the planet passes every test that we havefor habitability,
                returns True.
            Otherwise returns False if it fails one test

        Calculations made from this website:
            https://en.wikipedia.org/wiki/Planetary_habitability

        Written by: Bradley Knorr
        """

        # determine if the tempurature is correct for liquid water
        # return false if planet is not in habitable zone
        if(tempurature < 0 or tempurature > 100):
            return False

        # determine if it is a rocky (> 2.5) or gas (< 2.5) planet
        # return false if planet is not dense enough (not rocky)
        if(density < 2.5):
            return False

        # determine if radius of planet is the correct size for habitability
        # return false if planet is too small or too large
        if(radius < 0.5 or radius > 2.5):
            return False

        # determine if the planet has the correct mass for habitability
        # return false if planet is not massive enough or too massive
        if(mass < 0.3 or mass > 10):
            return False

        # determine if the planet has a reasonable eccentricity for life
        # Note: in reality the eccentricity is used to determine if
        #   a planet escapes the habitable zone during its orbit as
        #   well as if tempuratures can vary too widely during its orbit
        # We are only testing if tempurature can vary too widely
        # Return false if eccentricity is too large
        if(eccentricity > 0.25):
            return False

        # if the planet passes every test for life, return True, that it is
        #   deemed habitable for life
        return True
