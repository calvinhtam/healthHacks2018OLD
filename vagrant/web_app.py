from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from database_setup import Base, Patient, Record, Diagnosis, Immunization, Condition, Chart, Treatment, Hospital, Doctor

app = Flask(__name__)

engine = create_engine('sqlite:///patienthistory.db')
Base.metadata.bind = engine

session = scoped_session(sessionmaker(bind=engine))

@app.teardown_request
def remove_session(ex=None):
    session.remove()

@app.route('/')
@app.route('/portal/')
@app.route('/portal/login/')
def login():
    #return 'This page will show login portal'
    patients = session.query(Patient).all()
    return render_template('login.html')

@app.route('/portal/<int:patient_id>/')
def portal():
    patient = session.query(Patient).filter_by(id=patient_id).one()
    return render_template('portal.html', patient=patient)

@app.route('/portal/<int:patient_id>/records/')
def recordsList():
    patient = session.query(Patient).filter_by(id=patient_id).one()
    return render_template('recordsList.html', patient=patient)

@app.route('/portal/<int:patient_id>/record/<int:record_id>')
def record():
    patient = session.query(Patient).filter_by(id=patient_id).one()
    record = session.query(Record).filter_by(id=record_id).one()
    return render_template('record.html', patient=patient, record=record)



"""
#######
#used on doctors side
@app.route('/portal/<int:patient_id>/record/add/')
def newRecord():
    patient = session.query(Patient).filter_by(id=patient_id).one()
    return render_template('newRecord.html', patient=patient)

@app.route('/portal/<int:patient_id>/record/<int:record_id>/add/<int:diagnosis_id>/')
def editDiagnosis():
    patient = session.query(Patient).filter_by(id=patient_id).one()
    diagnosis = session.query().filter_by(id=diagnosis_id).one()
    return render_template('editRecord.html', patient=patient, diagnosis=diagnosis)

@app.route('/portal/<int:patient_id>/record/<int:record_id>/add/<int:immunization_id>/')
def editImmunization():
    patient = session.query(Patient).filter_by(id=patient_id).one()
    immunization = session.query().filter_by(id=immunization_id).one()
    return render_template('editRecord.html', patient=patient, immunization=immunization)


@app.route('/portal/<int:patient_id>/record/<int:record_id>/add/<int:condition_id>/')
def editCondition():
    patient = session.query(Patient).filter_by(id=patient_id).one()
    condition = session.query().filter_by(id=condition_id).one()
    return render_template('editRecord.html', patient=patient, condition=condition)


@app.route('/portal/<int:patient_id>/record/<int:record_id>/add/<int:chart_id>/')
def editChart():
    patient = session.query(Patient).filter_by(id=patient_id).one()
    chart = session.query().filter_by(id=chart_id).one()
    return render_template('editRecord.html', patient=patient, chart=chart)


@app.route('/portal/<int:patient_id>/record/<int:record_id>/add/<int:treatment_id>/')
def editTreatment():
    patient = session.query(Patient).filter_by(id=patient_id).one()
    treatment = session.query().filter_by(id=treatment_id).one()
    return render_template('editRecord.html', patient=patient, treatment=treatment)
"""

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = '5000')