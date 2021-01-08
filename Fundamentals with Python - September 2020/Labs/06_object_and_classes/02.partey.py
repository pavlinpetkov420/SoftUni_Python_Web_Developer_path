class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def name_of_attendees(self):
        return ", ".join([person.name for person in self.people])

    def guests_count(self):
        return len(self.people)


party = Party()

command = input()
while command != "End":
    name = command
    person = Person(name)
    party.invite(person)
    command = input()

print(f"Going: {party.name_of_attendees()}\n"
      f"Total: {party.guests_count()}")
