# nyc-doe-covid-interventions-analysis

The [Press NYC DOE COVID interventions](https://github.com/pressnyc/nyc-doe-covid-interventions) project will scrape data from the [NYC daily COVID case map](https://www.schools.nyc.gov/school-life/health-and-wellness/covid-information/daily-covid-case-map).

The [`schoolcase.json`](https://github.com/pressnyc/nyc-doe-covid-interventions/blob/main/schoolcases.json) file has cases from all schools, and is updated daily with new case counts.

The [`analysis.py`](https://github.com/jimgraham/nyc-doe-covid-interventions-analysis/blob/main/analysis.py) file will iterate over the _history_ (via `git`) of that file to build a historical record of cases per school.

## To Run

1. make sure you have `git` installed
    - `git --version`
2. make sure you have `python3` installed
    - `python3 --version`
3. In the `Terminal.app` (from the command line) clone the [Press NYC DOE COVID interventions](https://github.com/pressnyc/nyc-doe-covid-interventions) repository 
    - `git clone https://github.com/pressnyc/nyc-doe-covid-interventions.git`
    - This will unpack the data into a directory called `nyc-doe-covid-interventions/`
4. From the same directory, clone this repository
    - `git clone https://github.com/jimgraham/nyc-doe-covid-interventions-analysis.git`
    - This will unpack this code into a directory called `nyc-doe-covid-interventions-analysis/`
5. Change into the analysis directory
    - `cd nyc-doe-covid-interventions-analysis`
6. Run the analysis
    - `python3 analysis.py`

The output should be

```bash
Pulling all data

Finding schools in dataset

Writing 'cases.csv'
```

there will now be a `cases.csv` file with the data.
   