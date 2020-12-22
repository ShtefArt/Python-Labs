from datetime import datetime


class Patient:
    name = "name"
    lastname = "lastname"
    birthday = datetime.today()
    address = "Golovna 1"
    height = 190
    weight = 100

    def __init__(self, name, lastname, birthday, address, height, weight):
        self.name = name
        self.lastname = lastname
        self.birthday = birthday
        self.address = address
        self.height = int(height)
        self.weight = int(weight)

    def __str__(self):
        return '{}, {}, {}, {}, {}' \
            .format(self.name, self.lastname, self.birthday, self.address,
                    self.height, self.weight)
