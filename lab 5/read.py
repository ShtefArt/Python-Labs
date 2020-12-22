import shelve
from datetime import datetime

from patient import Patient

db = shelve.open('patients')

patients = db['patients']
if len(patients) == 0:
    print("db is empty!")
    db.close()
else:
    highest_patient = max(patients, key=lambda s: int(s.height))
    total_weight = sum(int(patient.weight) for patient in patients)
    print("The highest patient: ", highest_patient)
    print("Total weight: ", total_weight)
    db.close()
