import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patient"

    id = Column(String(50), primary_key=True)
    language = Column(String(32))
    doc = relationship()

class Record(Base):
    __tablename__ = "record"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    patient_id = Column(String(50), ForeignKey('patient.id'))
    med_record = relationship(Patient)

class Diagnosis(Base):
    __tablename__ = "diagnosis"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(50), nullable=False)
    diagnosis_desc = Column(String(250))
    patient_id = Column(String(50), ForeignKey('patient.id'))
    record = relationship(Record)

class Immunization(Base):
    __tablename__ = "immunization"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(50), nullable=False)
    status = Column(String(50), nullable=False)
    patient_id = Column(String(50), ForeignKey('patient.id'))
    record = relationship(Record)

class Condition(Base):
    __tablename__ = "condition"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(50), nullable=False)
    status = Column(String(80), nullable=False)
    patient_id = Column(String(50), ForeignKey('patient.id'))
    record = relationship(Record)

class Chart(Base):
    __tablename__ = "chart"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(50), nullable=False)
    value = Column(String(80), nullable=False)
    patient_id = Column(String(50), ForeignKey('patient.id'))
    record = relationship(Record)

class Treatment(Base):
    __tablename__ = "treatment"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(50), nullable=False)
    treatment_desc = Column(String(250), nullable=False)
    diagnosis_id = Column(Integer, ForeignKey('diagnosis.id'))
    patient_id = Column(String(50), ForeignKey('patient.id'))
    record = relationship(Record)

class Hospital(Base):
    __tablename__ = "hospital"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    location = Column(String(250), nullable=False)
    zip_code = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    patient_id = Column(String(50), ForeignKey('patient.id'))
    nearest_hospital = relationship(Patient)

class Doctor(Base):
    __tablename__ = "doctor"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    location = Column(String(250), nullable=False)
    date = Column(DateTime(50))
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    patient_id = Column(String(50), ForeignKey('patient.id'))
    hospital = relationship(Hospital)
    patient = relationship(Patient)


engine = create_engine('sqlite:///patienthistory.db')
Base.metadata.create_all(engine)