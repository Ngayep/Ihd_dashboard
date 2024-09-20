Interactive Health Dashboard :Visualizing Malaria Data in Cameroon

Introduction

Inspiration is often born from necessity. In my case, the necessity was clear: the need for accessible and interactive malaria data to support public health decision-making in Cameroon. As a data enthusiast with a passion for health, I embarked on this project to create a user-friendly dashboard that visualizes real-time data about malaria. This project started as a personal curiosity but quickly evolved into something much larger. I wanted to build a tool that could help researchers, healthcare workers, and policymakers understand trends and act on real data.


Project Overview

This project is an interactive health dashboard aimed at visualizing public health data, specifically focusing on Malaria incidence, prevalence, and mortality rates in Cameroon. The dashboard enables users to view real-time data trends through intuitive charts and graphs, making it a valuable tool for researchers, public health officials, and stakeholders in understanding and combatting malaria.

Inspiration & Vision

The concept of this project came from my fascination with how data can be used to tackle real-world problems. The burden of malaria in my home country, Cameroon, was my driving force. I envisioned a tool that could break down large data, enable analysis, and make sense of malaria trends to support health professionals.

But there were challenges, of course.
Challenges I Faced:

    Data Collection and Cleaning: The malaria data I had was scattered across multiple CSV files, each with different structures and inconsistencies. Handling missing data and ensuring accuracy was a major part of my early process.
    Choosing the Right Visualization Tools: I experimented with various libraries—Plotly, Seaborn, and finally Matplotlib—before settling on static image rendering. Though dynamic charts were appealing, I learned that sometimes simplicity (and performance) wins.
    Backend-Frontend Integration: Ensuring the smooth integration between my Flask app and the frontend was tricky at first. Passing data from the backend to the frontend and rendering accurate, real-time visualizations took many iterations.

Technology & Architecture
Technology Stack:

    Backend: Flask – Python-based web framework that serves data from CSV files for real-time analysis.
    Data Processing: Pandas – Used for data manipulation.
    Visualization: Matplotlib – Generates static images of charts (e.g., incidence, prevalence, and hospitalization rates).
    Frontend: HTML5, CSS3, Bootstrap – For building a responsive and clean interface.
    Database: CSV files – Malaria data is stored in CSV files, which are processed using Pandas.

Application Architecture:

The application’s architecture is designed for simplicity and efficiency. Here’s how data flows through the app:

    CSV Data Ingestion: CSV files containing malaria data are uploaded.
    Data Cleaning & Transformation: Using Pandas, the data is cleaned and structured into usable formats. This includes handling missing values, filtering by date etc. I chose Pandas for its powerful data manipulation capabilities.
    Flask Backend: The Flask app serves the cleaned data and responds to API requests for visualization.
    Visualization Generation: Matplotlib generates static charts from the data, which are then rendered in the frontend. Initially, I considered using dynamic visualizations with Plotly, but after testing, I found that static images using Matplotlib provided the best performance and clarity. This trade-off was necessary for a fast and smooth user experience.
    Frontend Rendering: HTML and CSS display the static images, ensuring smooth performance without the overhead of dynamic charts.

Key Features:

    Prevalence Visualization: Displays the percentage of individuals alive or affected by malaria over time.
    Incidence Tracking: Tracks the number of new malaria cases across different time periods.
    Mortality Distribution: Provides a visual breakdown of the mortality rate due to malaria.


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

The dashboard allows users to explore malaria data with the following:

    Prevalence of Malaria: Number of malaria cases over time.
    Incidence Rate: Number of new malaria cases within a specified period.
    Mortality Rate: Deaths due to malaria over time.

Note: To update the data, simply upload new CSV files containing malaria statistics, and the application will automatically process and display the updated data.


Features:

    Static visualizations generated from real-time data.
    CSV-based data input for easy updates.
    Filter and explore data by date and region.
   
    ![Ihdasboard](https://github.com/user-attachments/assets/9f33a2ff-cfbd-4ea2-b103-a61f007a2dae)

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
Project Blog article: https://link.medium.com/lCth1eVyZMb
linkedIn: https://www.linkedin.com/in/jessica-chancel-tcheumadji-ngayep-1a7a8372/
Twitter: https://x.com/CourtesyofJess
