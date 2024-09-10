Interactive Health Dashboard - Malaria Incidence and Prevalence in Cameroon
Project Overview

This project is an interactive health dashboard aimed at visualizing public health data, specifically focusing on Malaria incidence, prevalence, and mortality rates in Cameroon. The dashboard enables users to view real-time data trends through intuitive charts and graphs, making it a valuable tool for researchers, public health officials, and stakeholders in understanding and combating malaria.
Key Features

    Prevalence Visualization: Displays the percentage of individuals alive or affected by malaria over time.
    Incidence Tracking: Tracks the number of new malaria cases across different time periods.
    Mortality Distribution: Provides a visual breakdown of the mortality rate due to malaria.

Technologies Used

    Backend: Flask (Python) – for routing and server-side logic.
    Data Processing: Pandas – for manipulating and aggregating data.
    Data Visualization: Plotly Express – for generating interactive charts (line charts, bar charts, pie charts).
    Frontend: HTML, CSS, JavaScript – for creating user interfaces and displaying charts.

Project Structure

php

Ihd_dashboard/
│
├── app/
│   ├── routes.py        # Flask routes and logic for fetching and visualizing data
│   ├── static/
│   │   ├── css/         # Static CSS files
│   │   └── js/          # JavaScript files (if applicable)
│   └── templates/
│       ├── base.html    # Base HTML template
│       └── visualizations.html  # Template for rendering visualizations
├── data/
│   └── malaria_data.csv # Data used for visualizations
└── README.md            # Project documentation (this file)

How It Works

    Data Fetching: The application reads malaria-related data from a CSV file that includes columns such as Date of Birth (dob), malaria history (malaria_history), and the status of individuals (alive or dead).

    Prevalence Calculation: The prevalence chart is created by calculating how many individuals in the dataset are still alive over time, grouped by the date of birth.

    Incidence Calculation: Incidence is calculated by counting the number of new cases of malaria (based on malaria_history) in each time period (grouped by year and month).

    Mortality Distribution: A pie chart is generated to show the percentage of people who have died from malaria compared to those still alive.

    Visualization: The charts (prevalence, incidence, and mortality) are rendered using Plotly Express and displayed dynamically on the visualization page.

How to Run the Project
Prerequisites

    Python 3.12+
    Flask
    Pandas
    Plotly Express

Steps

    Clone the repository:

    bash

git clone https://github.com/yourusername/Ihd_dashboard.git
cd Ihd_dashboard

Set up a virtual environment and install dependencies:

bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run the Flask application:

bash

    flask run

    Open the dashboard in your browser at http://127.0.0.1:5000/visualizations.

Possible Improvements

    Data Source Integration: Currently, the dashboard uses a CSV file for data. In the future, it could pull data from APIs or live databases to provide real-time updates.

    Login and Authentication: Adding user authentication would allow users to save custom data views, making the dashboard more interactive and secure.

    Advanced Filtering: Allowing users to filter data by region, gender, or age would provide more granularity and insights into the malaria data.

    Additional Metrics: The dashboard could be expanded to visualize other health-related metrics such as hospitalization rates or treatment outcomes.

    Mobile Optimization: Improve the dashboard's responsiveness for mobile and tablet users.

Contributing

Feel free to open issues or pull requests if you would like to contribute to the project or suggest new features.
