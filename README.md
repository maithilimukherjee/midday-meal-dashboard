# Midday Meal Dashboard

This project provides a simple data visualization dashboard for analyzing midday meal coverage across states.  
It uses Python with **pandas** and **matplotlib** to generate charts showing average coverage and distribution categories.

---

## Features

- **Bar Chart**: Displays the average meal coverage percentage by state.  
- **Pie Chart**: Shows the distribution of schools by coverage category (`Excellent`, `Good`, `Average`, `Poor`).  
- **Automatic Classification**: Each school is categorized based on coverage percentage.  

---

## Requirements

- Python 3.8+  
- pandas  
- matplotlib  


## Usage

Place your data file meals.csv in the working directory.
The dataset should contain the following columns:

state

meals_served

meals_required

Run the dashboard script:

python dashboard.py


The script will generate:

- A bar chart of average coverage by state.

- A pie chart showing distribution of coverage categories.

- Coverage Categories

- Coverage percentage is mapped to performance categories as follows:

Excellent: ≥ 90%

Good: 75% – 89%

Average: 50% – 74%

Poor: < 50%
