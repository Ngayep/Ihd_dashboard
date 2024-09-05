from flask import Blueprint, render_template, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from flask import Flask
from . import db
from .models import Patient, MalariaIncidence, Hospitalization
import plotly.express as px

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Route for the index page with basic data rendering."""
    data = fetch_data()
    return render_template('index.html', data=data)


@main.route('/visualizations')
def visualizations():
    """Route for displaying all visualizations."""
    # Data for prevalence and incidence
    patients = Patient.query.all()
    hospitalizations = Hospitalization.query.all()

    # Prevalence Chart: Patients who are alive
    alive_count = Patient.query.filter_by(status="Alive").count()
    dead_count = Patient.query.filter_by(status="Dead").count()

    fig_prevalence = plot_prevalence(alive_count, dead_count)

    # Incidence Chart: Malaria occurrences
    malaria_positive_count = Patient.query.filter(Patient.malaria_history.contains("Yes")).count()
    malaria_negative_count = Patient.query.filter(Patient.malaria_history.contains("No")).count()

    fig_incidence = plot_incidence(malaria_positive_count, malaria_negative_count)

    # Hospitalization Chart: Frequency of hospitalizations
    fig_hospitalization = plot_hospitalization(hospitalizations)

    return render_template(
        'visualizations.html',
        fig_prevalence=fig_prevalence,
        fig_incidence=fig_incidence,
        fig_hospitalization=fig_hospitalization
    )


def plot_prevalence(alive_count, dead_count):
    """Generate a bar chart for prevalence of alive vs dead patients."""
    fig, ax = plt.subplots()
    ax.bar(['Alive', 'Dead'], [alive_count, dead_count], color=['green', 'red'])
    ax.set_title('Prevalence of Alive vs Dead Patients')

    return save_plot(fig)


def plot_incidence(positive_count, negative_count):
    """Generate a bar chart for malaria incidence (Yes/No history)."""
    fig, ax = plt.subplots()
    ax.bar(['Malaria History', 'No Malaria History'], [positive_count, negative_count], color=['blue', 'gray'])
    ax.set_title('Malaria Incidence')

    return save_plot(fig)


def plot_hospitalization(hospitalizations):
    """Generate a bar chart for hospitalizations."""
    dates = [h.hospitalization_date for h in hospitalizations]
    status = [h.status for h in hospitalizations]

    df = pd.DataFrame({'date': dates, 'status': status})
    fig = px.histogram(df, x="date", color="status", title="Hospitalization Over Time")

    return fig.to_html(full_html=False)


def save_plot(fig):
    """Save the plot as a base64 encoded string for rendering."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return f"data:image/png;base64,{image_base64}"


def fetch_data():
    """Fetch all the patient and malaria-related data."""
    patients = Patient.query.all()
    malaria_incidences = MalariaIncidence.query.all()

    return {
        "patients": patients,
        "incidences": malaria_incidences
    }
