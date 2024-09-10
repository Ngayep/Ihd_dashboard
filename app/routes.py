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
    df.columns = df.columns.str.strip()

    print(df.columns)  # Check column names
    print(df.head())   # Check first few rows

    for _, row in df.iterrows():
        try:
            # Check if all required fields are present and valid
            if pd.notna(row['Sample ID']) and pd.notna(row['Date of Birth']):
                patient = Patient(
                    sample_id=row['Sample ID'],
                    dob=pd.to_datetime(row['Date of Birth'], format='%Y-%m-%d'),
                    malaria_history=row['Has had malaria in the past x months?'],
                    treatment=row['Has taken treatment'],
                    status=row['Alive or dead from malaria?']
                )
                db.session.add(patient)
            else:
                print(f"Skipping row with missing data: {row['Sample ID']}")
        except Exception as e:
            print(f"Error processing row: {row['Sample ID']} - {str(e)}")

    db.session.commit()
    print("Database populated successfully!")
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

    if df is None or df.empty:
        return "Error: No data available for visualization", 500

    # Convert 'dob' to datetime and calculate 'prevalence'
    df['date'] = pd.to_datetime(df['dob'])  # Assuming 'dob' is the closest representation of the date
    df['prevalence'] = df['status'].apply(lambda x: 1 if x == 'Alive' else 0)

    # Generate the Prevalence Chart
    fig_prevalence = px.line(df, x='dob', y='prevalence', title="Prevalence Over Time")
    prevalence_html = fig_prevalence.to_html(full_html=False)

    # Calculate the incidence based on 'malaria_history'
    df['has_malaria'] = df['malaria_history'].apply(lambda x: 1 if x == "yes" else 0)
    df['year_month'] = pd.to_datetime(df['date']).dt.to_period('M').astype(str)  # Group by year and month
    incidence_df = df.groupby('year_month').agg(incidence=('has_malaria', 'sum')).reset_index()

    # Generate the Incidence Chart
    fig_incidence = px.bar(incidence_df, x='year_month', y='incidence', title="Malaria Incidence Over Time")
    incidence_html = fig_incidence.to_html(full_html=False)

    # Calculate the mortality (based on status)
    df['mortality'] = df['status'].apply(lambda x: 'Alive' if x == 'Alive' else 'Dead')

    # Generate the Mortality Chart
    fig_mortality = px.pie(df, names='mortality', title="Mortality Distribution")
    mortality_html = fig_mortality.to_html(full_html=False)

    # Pass the charts as HTML snippets to the template
    return render_template('visualizations.html',
                           prevalence_html=prevalence_html,
                           incidence_html=incidence_html,
                           mortality_html=mortality_html)


@main.route('/populate')
def trigger_population():
    """Route to manually trigger the population of the database."""
    result = populate()
    return result
