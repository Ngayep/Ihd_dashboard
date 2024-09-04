from flask import Blueprint, render_template, jsonify
import pandas as pd
import plotly.express as px
from . import db
from .models import Patient

main = Blueprint('main', __name__)


def populate():
    """Load data from the CSV file and populate the database."""
    csv_file = 'data/Malaria_data_1000.csv'
    df = pd.read_csv(csv_file)

    for _, row in df.iterrows():
        try:
            patient = Patient(
                sample_id=row['Sample ID'],
                dob=pd.to_datetime(row['Date of Birth'], format='%Y-%m-%d'),
                malaria_history=row['Has had malaria in the past x months?'],
                treatment=row['Has taken treatment'],
                status=row['Alive or dead from malaria?']
            )
            db.session.add(patient)
        except Exception as e:
            print(f"Error processing row: {row['Sample ID']} - {str(e)}")

    db.session.commit()
    return "Database populated successfully!"


def fetch_data():
    """Fetch data from the database for visualization or display."""
    patients = Patient.query.all()
    data = []
    for patient in patients:
        data.append({
            'sample_id': patient.sample_id,
            'dob': patient.dob.strftime('%Y-%m-%d'),
            'malaria_history': patient.malaria_history,
            'treatment': patient.treatment,
            'status': patient.status
        })

    df = pd.DataFrame(data)
    return df


@main.route('/')
def index():
    """Route for the index page."""
    data = fetch_data()
    return render_template('index.html', data=data)


@main.route('/visualizations')
def visualizations():
    """Route for data visualizations."""
    df = fetch_data()

    # Generate a bar chart for Malaria Incidence vs Status
    status_chart = px.bar(df, x='malaria_history', color='status', barmode='group',
                          title="Malaria History vs Status")

    # Generate a pie chart for Treatment Distribution
    treatment_chart = px.pie(df, names='treatment', title="Treatment Distribution")

    # Convert the figures to JSON for frontend rendering
    status_chart_json = status_chart.to_json()
    treatment_chart_json = treatment_chart.to_json()

    return jsonify({'status_chart': status_chart_json, 'treatment_chart': treatment_chart_json})


@main.route('/populate')
def trigger_population():
    """Route to manually trigger the population of the database."""
    result = populate()
    return result
