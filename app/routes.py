from flask import Blueprint, render_template
import pandas as pd
""" The route module creates the main Blueprint
and a route for the index page.
The Blueprint is imported in the app/__init__.py module."""
main = Blueprint('main', __name__)


def fetch_data():
    """load data from the csv file"""
    csv_file = 'data/Malaria_data_1000.csv'
    df = pd.read_csv(csv_file)

    # convert the dataframe to a list of dictionaries
    data = df.to_dict(orient='records')
    return data


@main.route('/')
def index():
    """Route for the index page.
It returns the index.html template."""
    data = fetch_data()
    return render_template('index.html', data=data)
