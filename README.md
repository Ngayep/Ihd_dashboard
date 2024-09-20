Interactive Health Dashboard - Malaria Incidence and Prevalence in Cameroon


Project Overview

This project is an interactive health dashboard aimed at visualizing public health data, specifically focusing on Malaria incidence, prevalence, and mortality rates in Cameroon. The dashboard enables users to view real-time data trends through intuitive charts and graphs, making it a valuable tool for researchers, public health officials, and stakeholders in understanding and combatting malaria.

Key Features:

    Prevalence Visualization: Displays the percentage of individuals alive or affected by malaria over time.
    Incidence Tracking: Tracks the number of new malaria cases across different time periods.
    Mortality Distribution: Provides a visual breakdown of the mortality rate due to malaria.

Technologies Used:

    Backend: Flask (Python) – for routing and server-side logic.
    Data Processing: Pandas – for manipulating and aggregating data.
    Data Visualization: Plotly Express – for generating interactive charts (line charts, bar charts, pie charts).
    Frontend: HTML, CSS, JavaScript – for creating user interfaces and displaying charts.

How It Works:

    Data Fetching: The application reads malaria-related data from a CSV file that includes columns such as Date of Birth (dob), malaria history (malaria_history), and the status of individuals (alive or dead).

    Prevalence Calculation: The prevalence chart is created by calculating how many individuals in the dataset are still alive over time, grouped by the date of birth.

    Incidence Calculation: Incidence is calculated by counting the number of new cases of malaria (based on malaria_history) in each time period (grouped by year and month).

    Mortality Distribution: A pie chart is generated to show the percentage of people who have died from malaria compared to those still alive.

    Visualization: The charts (prevalence, incidence, and mortality) are rendered using Plotly Express and displayed dynamically on the visualization page.

How to Run the Project locally, follow these steps:
Prerequisites
    Python 3.8+
    Flask
    Pandas
    Plotly Express
Steps
Clone the repository:
git clone https://github.com/Ngayep/Ihd_dashboard.git
cd Ihd_dashboard

Set up a virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run the Flask application:
flask run

Open the dashboard in your browser at http://127.0.0.1:5000.
Live Demo: https://ihd-dashboard.onrender.com
Possible Improvements

  Data Source Integration: Currently, the dashboard uses a CSV file for data. In the future, it could pull data from APIs or live databases to provide real-time updates.
  Login and Authentication: Adding user authentication would allow users to save custom data views, making the dashboard more interactive and secure.
    Advanced Filtering: Allowing users to filter data by region, gender, or age would provide more granularity and insights into the malaria data.
    Additional Metrics: The dashboard could be expanded to visualize other health-related metrics such as hospitalization rates or treatment outcomes.
    Mobile Optimization: Improve the dashboard's responsiveness for mobile and tablet users.
    Beautiful interface: Improve the design of the dashboard

Usage

The dashboard provides visualizations for:

    Prevalence of Malaria: Number of malaria cases over time.
    Incidence Rate: Number of new malaria cases within a specified period.
    Mortality Rate: Deaths due to malaria over time.

Features:

    Static visualizations generated from real-time data.
    CSV-based data input for easy updates.
    Filter and explore data by date and region.
    
Contributing

Feel free to open issues or pull requests if you would like to contribute to the project or suggest new features.
 If you want to contribute to this project, here’s how you can do it:

    Fork the repository.
    Create a feature branch: 
        git checkout -b my-new-feature
        git commit -m "Add some feature"
        git push origin my-new-feature
    Then create a pull request

AUTHOR: Tcheumadji Ngayep Jessica Chancel
linkedIn: https://www.linkedin.com/in/jessica-chancel-tcheumadji-ngayep-1a7a8372/
Twitter: https://x.com/CourtesyofJess
