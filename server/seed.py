#!/usr/bin/env python3
# server/seed.py

import datetime
from app import app
from models import db, Employee, Review, Onboarding

with app.app_context():
    # Delete all rows in tables
    Employee.query.delete()
    Review.query.delete()
    Onboarding.query.delete()

    # Add model instances to database
    uri = Employee(name="Uri Lee", hire_date=datetime.datetime(2022, 5, 17))
    tristan = Employee(name="Tristan Tal", hire_date=datetime.datetime(2020, 1, 30))
    db.session.add_all([uri, tristan])
    db.session.commit()

    # 1..1 relationship between Employee and Onboarding

    uri_onboarding = Onboarding(
        orientation=datetime.datetime(2023, 3, 27),
        employee=uri)

    tristan_onboarding = Onboarding(
        orientation=datetime.datetime(2020, 1, 20, 14, 30),
        forms_complete=True,
        employee=tristan)

    db.session.add_all([uri_onboarding, tristan_onboarding])

    db.session.commit()

    # 1..1 relationship between Employee and Onboarding
    uri_onboarding = Onboarding(orientation=datetime.datetime(2023, 3, 27))
    tristan_onboarding = Onboarding(
        orientation=datetime.datetime(2020, 1, 20, 14, 30), forms_complete=True
    )
    db.session.add_all([uri_onboarding, tristan_onboarding])
    db.session.commit()
