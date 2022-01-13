# basically used to crate UDF data types
class student:
    def __init__(self, id, name, gpa, is_on_probation):
        self.id = id
        self.name = name
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honour_roll(self):
        if self.gpa >= 7.0:
            return True
        else:
            return False
