import shelve
from datetime import datetime

from patient import Patient

with shelve.open('patients') as db:
    name = input("name: ")
    lastname = input("lastname")
    birthday = datetime.strptime(input("birthday: "), '%d.%m.%Y').date()
    address = input("address: ")
    height = input("height: ")
    weight = input("weight: ")

    patients = db['patients']
    patients.append(Patient(name, lastname, birthday, address, height, weight))
    db['patients'] = patients

    db.close()
