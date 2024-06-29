# Border Deaths and Mental Health Statistics Dashboard

This project visualizes various statistics related to border deaths and mental health conditions using Plotly and Dash. It includes different types of data visualizations such as line charts and scatter plots.

## Setup and Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/xmnlz/dash-python.git
    cd dash-python
    ```

2. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Dash app:**

    ```sh
    python ./src/app.py
    ```

## Project Files

- **data/**: This directory contains the CSV files with the data used for the visualizations.
  - `border_deaths_by_discoverer.csv`
  - `death_by_age.csv`
  - `deaths_by_gender.csv`
  - `deaths_nationality.csv`
  - `deathtype.csv`
  - `mental_health_conditions_research.csv`

- **src/**: This directory contains the Python scripts for the Dash app.
  - `app.py`: The main Dash application script.
  - `graphs.py`: Contains functions to create the Plotly graphs.

- **.gitignore**: Specifies files and directories to be ignored by git.

- **README.md**: Documentation for the project.

- **requirements.txt**: Lists the Python packages required to run the project.

## Usage

After running the Dash app, you can open it in your browser. The app includes multiple visualizations:

- **Border Deaths by Discoverer**
- **Deaths by Age**
- **Deaths by Gender**
- **Deaths by Nationality**
- **Types of Deaths**
- **Mental Health Conditions**

There is also a theme toggle button to switch between a black and white theme.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
