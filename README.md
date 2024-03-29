# CSE163Project: Exoplanets

## Our Project:
> Our project is on Exoplanets and on informing the public about what lies ouside our solar
> system. Below are the steps on how to run our project.

## How to Download Our Data:
> 1. Go to this [website](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=planets).
>       * [Documentation](https://exoplanetarchive.ipac.caltech.edu/docs/API_exoplanet_columns.html)
>       for our dataset.
> 2. Before downloading the dataset from the link go to the dataset and click **'Select Columns'**
> at the top left corner.
> 3. A menu will pop up with extra columns to select. Scroll down untill you see **'Planet Columns'**.
> 4. Expand **'Planet Columns'** and you will see a list of more columns to add. Go through the list
> and select the columns listed below. (Note: Some columns can be expanded futher. For example,
> 'Time of Periastron' can be expanded to have 'Time of Periastron Upper Unc. [days]', 
> 'Time of Periastron Lower Unc. [days]', etc. For some of the columns listed you will need to expand
> the lists to get each column.)
> 5. Make sure to select the following columns:
>       * Time of Periastron [days]
>       * Time of Periastron Upper Unc. [days]
>       * Time of Periastron Lower Unc. [days]
>       * Time of Periastron Limit Flag
>       * Equilibrium Temperature [K]
>       * Equilibrium Temperature Upper Unc. [K]
>       * Equilibrium Temperature Lower Unc. [K]
>       * Equilibrium Temperature Limit Flag
>       * Planet Mass [Earth mass]
>       * Planet Mass Upper Unc. [Earth mass]
>       * Planet Mass Lower Unc. [Earth mass]
>       * Planet Mass Limit Flag
>       * Planet Radius [Earth radii]
>       * Planet Radius Upper Unc. [Earth radii]
>       * Planet Radius Lower Unc. [Earth radii]
>       * Planet Radius Limit Flag
>       * Transit Duration [days]
>       * Transit Duration Upper Unc. [days]
>       * Transit Duration Lower Unc. [days]
>       * Transit Duration Limit Flag
>       * Discovery Facility
> 6. Once everything is selected, click the **Update** button on top of the select columns menu.
> 7. Once updated you may close out the menu containing the columns.
> 8. Hover over **'Download Table'** in the top left corner. A menu should pop up and you can
>    click **'Download Table'** at the bottom of the list.
> 9. Place the downloaded dataset in the `data` folder. 
>       * Note: The datset will contain text at the top of the file talking about what the name
>         of earch column stands for. Our code handles skipping these lines and moving onto the dataset.
>         **DO NOT DELETE THIS TEXT**
> 10. **The datset is now ready to be used.**

## How to Run the Project:
> 1. Open up the `main.py` file.
> 2. Make sure to have the standard `cse163` environment.
>       * Environment includes libraries like pandas, seaborn, matplotlib, math and the
>           machine learning libraries.
> 2. Run that file
> 
> `main.py` will run each function from: `pandas_file.py`, `graphing_file.py`,
> `habitable_planets_file.py`, and `machine_learning.py`. The output will tell you which file is
> run and in what order. The results for the functions will be printed out. Some of our functions
> produce graphs. To view them, go into the `figures` folder and all the plots will be there.

## How to Interpret Results:
> Our `main.py` file outlines what each of the returned values mean and will let the client
> know which file it is testing. 

## Other Information:
> - The `Files` folder contains notes and manual caluclations we did.
> - The `data` folder contains our dataset.
> - The **'CSE 163 Project Part 2.pdf'** document contains the report for the project.