from flask_sqlalchemy import SQLAlchemy

# Import the db instance from the create_app function
from . import db

# Define Patient Model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sample_id = db.Column(db.Integer, unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    malaria_history = db.Column(db.String(200), nullable=False)
    treatment = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    incidences = db.relationship('MalariaIncidence', backref='patient', lazy=True)
    hospitalizations = db.relationship('Hospitalization', backref='patient', lazy=True)


# Define MalariaIncidence Model
class MalariaIncidence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    diagnosis = db.Column(db.String(100), nullable=False)


# Define Hospitalization Model
class Hospitalization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    hospitalization_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
